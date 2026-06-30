import pandas as pd
import pdfplumber
from sqlalchemy import create_engine

all_rows = []
with pdfplumber.open('Idaho list.pdf') as pdf:
    for page_num in range(1, len(pdf.pages)):  # skip page 1 (intro page)
        page = pdf.pages[page_num]
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                clean_row = [cell for cell in row if cell is not None and cell.strip() != '']
                if clean_row:
                    all_rows.append(clean_row)

# Remove header rows that repeat on each page
all_rows = [r for r in all_rows if r[0] not in ('Name', 'Date')]

# Build records: if row has 5 items -> name, start, eligible, reinstated, info
# if row has 4 items -> name, start, eligible, info (no reinstated date)
records = []
for row in all_rows:
    name = row[0].replace('\n', ' ')
    start_date = row[1]
    eligible_date = row[2]
    if len(row) == 5:
        date_reinstated = row[3]
        info = row[4].replace('\n', ' ')
    else:
        date_reinstated = None
        info = row[3].replace('\n', ' ') if len(row) > 3 else None
    records.append([name, start_date, eligible_date, date_reinstated, info])

df = pd.DataFrame(records, columns=['full_name', 'start_date', 'eligible_for_reinstatement',
                                      'date_reinstated', 'additional_information'])

# Convert dates, then back to text since columns are VARCHAR now
df['start_date'] = pd.to_datetime(df['start_date'], format='%m/%d/%y', errors='coerce')
df['start_date'] = df['start_date'].dt.strftime('%Y-%m-%d')

df['eligible_for_reinstatement'] = df['eligible_for_reinstatement'].replace('Indefinite', None)
df['eligible_for_reinstatement'] = pd.to_datetime(df['eligible_for_reinstatement'], format='%m/%d/%y', errors='coerce')
df['eligible_for_reinstatement'] = df['eligible_for_reinstatement'].dt.strftime('%Y-%m-%d')

df['date_reinstated'] = pd.to_datetime(df['date_reinstated'], format='%m/%d/%y', errors='coerce')
df['date_reinstated'] = df['date_reinstated'].dt.strftime('%Y-%m-%d')

# Add state
df['state'] = 'ID'

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# Must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Check results
print("=== MISSING DATA ===")
print(df.isnull().sum())
print("\nTotal rows:", len(df))
print("\nSample:")
print(df.head(10))

# Load into Postgres
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('idaho_exclusions', engine, if_exists='append', index=False)

print("\nDone! Idaho data loaded successfully.")