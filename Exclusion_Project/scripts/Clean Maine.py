import re
import pandas as pd
import pdfplumber
from sqlalchemy import create_engine

COLUMNS = [
    "last_name", "first_name", "middle_initial",
    "alias_last_name_1", "alias_first_name_1",
    "alias_last_name_2", "alias_first_name_2",
    "alias_last_name_3", "alias_first_name_3",
    "alias_last_name_4", "alias_first_name_4",
    "provider_type", "exclusion_start_date",
]

NAME_COLUMNS = {c for c in COLUMNS if c not in ("provider_type", "exclusion_start_date")}

review_log = []


def normalize_header(text):
    return re.sub(r"\s+", " ", (text or "")).strip().lower()


def clean_cell(value, col_name, page_num, row_num):
    if value is None:
        return None
    text = value.strip()

    if text.upper() == "N/A" or text == "":
        return None

    if "\n" in text:
        parts = [p.strip() for p in text.split("\n") if p.strip()]
        joined = "".join(parts) if col_name in NAME_COLUMNS else " ".join(parts)

        review_log.append({
            "page": page_num, "row": row_num, "column": col_name,
            "raw": repr(text), "joined": joined,
        })
        text = joined

    return re.sub(r"\s+", " ", text).strip() or None


# Extract tables from all pages of the PDF
records = []
with pdfplumber.open('Maine list.pdf') as pdf:
    for page_num, page in enumerate(pdf.pages, start=1):
        tables = page.extract_tables()
        for table in tables:
            for row_num, row in enumerate(table, start=1):
                if not row:
                    continue
                if normalize_header(row[0]).startswith("provider last name"):
                    continue  # repeated header row on each page

                cells = list(row) + [None] * (len(COLUMNS) - len(row))
                cells = cells[:len(COLUMNS)]
                cleaned = [clean_cell(cells[i], COLUMNS[i], page_num, row_num)
                           for i in range(len(COLUMNS))]

                if not any(cleaned):
                    continue  # fully blank row (page boundary artifact)

                records.append(cleaned)

# Create dataframe
df = pd.DataFrame(records, columns=COLUMNS)

# Clean up: remove any stray header repeats or fully empty rows
df = df.dropna(how='all')
df = df[df['last_name'].notna()]

# Convert exclusion_start_date (Maine prints full 4-digit years, unlike HI/ID)
# Then convert back to text since column is VARCHAR now
df['exclusion_start_date'] = pd.to_datetime(df['exclusion_start_date'], format='%m/%d/%Y', errors='coerce')
df['exclusion_start_date'] = df['exclusion_start_date'].dt.strftime('%Y-%m-%d')

# Add state
df['state'] = 'ME'

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# Must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Check results
print("=== MISSING DATA ===")
print(df.isnull().sum())
print("\nTotal rows:", len(df))
print("\nSample:")
print(df.head(10))

if review_log:
    review_df = pd.DataFrame(review_log)
    review_df.to_csv('maine_review.csv', index=False)
    print(f"\n{len(review_log)} wrapped cells were auto-joined -> spot-check maine_review.csv")

# Load into Postgres
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('maine_exclusions', engine, if_exists='append', index=False)

print("\nDone! Maine data loaded successfully.")