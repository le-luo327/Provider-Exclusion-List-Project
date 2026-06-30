import pandas as pd
from sqlalchemy import create_engine, text

engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')

def classify_name(name):
    name = name.strip()

    if ',' in name:
        parts = [p.strip() for p in name.split(',')]
        last = parts[0]
        rest = parts[1].split() if len(parts) > 1 else []
        first = rest[0] if len(rest) > 0 else ''
        middle = ' '.join(rest[1:]) if len(rest) > 1 else ''
        return {'first': first, 'middle': middle, 'last': last, 'status': 'comma_split'}

    words = name.split()
    if len(words) == 1:
        return {'first': '', 'middle': '', 'last': words[0], 'status': 'one_word'}
    elif len(words) == 2:
        return {'first': words[0], 'middle': '', 'last': words[1], 'status': 'two_word'}
    elif len(words) == 3:
        return {'first': words[0], 'middle': words[1], 'last': words[2], 'status': 'three_word'}
    else:
        # 4+ words: assume first word = first name, last word = last name, middle = everything between
        return {'first': words[0], 'middle': ' '.join(words[1:-1]), 'last': words[-1], 'status': 'four_plus_word'}


# Fetch rows where full name was dumped into last_name (these 4 tables only)
with engine.connect() as conn:
    result = conn.execute(text("""
        SELECT id, source_table, last_name
        FROM main_exclusions
        WHERE source_table IN ('idaho_exclusions', 'illinois_exclusions', 'indiana_exclusions', 'kansas_exclusions')
    """))
    rows = result.fetchall()

print(f"Total rows to process: {len(rows)}")

review_log = []
updates = []

for row in rows:
    row_id, source_table, full_name = row
    if not full_name or full_name.strip() == '':
        continue

    classified = classify_name(full_name)

    updates.append({
        'id': row_id,
        'first_name': classified['first'],
        'middle_name': classified['middle'],
        'last_name': classified['last']
    })

    # Log anything unusual for spot-checking later (one-word and four+ word cases are riskiest)
    if classified['status'] in ('one_word', 'four_plus_word'):
        review_log.append({
            'id': row_id, 'source_table': source_table,
            'original_name': full_name, 'status': classified['status'],
            'split_result': f"{classified['first']} | {classified['middle']} | {classified['last']}"
        })

print(f"Rows updated: {len(updates)}")
print(f"Flagged for spot-check: {len(review_log)}")

# Apply updates
with engine.begin() as conn:
    for u in updates:
        conn.execute(text("""
            UPDATE main_exclusions
            SET first_name = :first_name,
                middle_name = :middle_name,
                last_name = :last_name
            WHERE id = :id
        """), u)

print("Updates applied successfully.")

# Save flagged rows for manual review
if review_log:
    review_df = pd.DataFrame(review_log)
    review_df.to_csv('name_split_review.csv', index=False)
    print(f"Review file saved: name_split_review.csv ({len(review_log)} rows)")