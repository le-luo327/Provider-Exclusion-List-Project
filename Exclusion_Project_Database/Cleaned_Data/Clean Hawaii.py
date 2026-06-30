import pandas as pd
import pdfplumber
from sqlalchemy import create_engine

# Extract tables from all pages of the PDF
all_rows = []
with pdfplumber.open('Hawaii list.pdf') as pdf:
    for page_num, page in enumerate(pdf.pages):
        tables = page.extract_tables()
        for table in tables:
            for row in table:
                all_rows.append(row)

# First row is the header
header = all_rows[0]
data_rows = [row for row in all_rows[1:] if row != header]  # skip repeated headers on other pages

# Create dataframe
df = pd.DataFrame(data_rows, columns=['last_name', 'first_name', 'middle_initial',
                                        'medicaid_provider_id', 'provider_type',
                                        'exclusion_date', 'reinstatement_date'])

# Clean up: remove rows that are header repeats or empty
df = df[df['last_name'] != 'Last Name or Business Name']
df = df.dropna(how='all')
df = df[df['last_name'].str.strip() != '']

# Convert exclusion_date (handle missing/dash values), then back to text
df['exclusion_date'] = df['exclusion_date'].replace('-', None)
df['exclusion_date'] = pd.to_datetime(df['exclusion_date'], format='%m/%d/%y', errors='coerce')
df['exclusion_date'] = df['exclusion_date'].dt.strftime('%Y-%m-%d')

# Keep reinstatement_date as text since it contains "Indefinite"
df['reinstatement_date'] = df['reinstatement_date'].str.strip()

# Replace 'NONE' with actual None for medicaid_provider_id
df['medicaid_provider_id'] = df['medicaid_provider_id'].replace('NONE', None)

# Add state
df['state'] = 'HI'

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
df.to_sql('hawaii_exclusions', engine, if_exists='append', index=False)

print("\nDone! Hawaii data loaded successfully.")