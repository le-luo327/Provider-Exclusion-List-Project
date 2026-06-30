import pandas as pd
from sqlalchemy import create_engine

# Read Iowa file - skip first row (title row)
df = pd.read_excel('Iowa list.xlsx', skiprows=1)

# Rename columns
df.columns = ['enrollment_type', 'specialty', 'npi', 'affiliated_npi',
              'last_name', 'first_name', 'business_name', 'sanction_type',
              'effective_date', 'sanction_end_date', 'eligible_reapply_date',
              'authority', 'license_type', 'license_number']

# Convert dates, then back to text since columns are VARCHAR now
df['effective_date'] = pd.to_datetime(df['effective_date'], errors='coerce')
df['effective_date'] = df['effective_date'].dt.strftime('%Y-%m-%d')

df['sanction_end_date'] = pd.to_datetime(df['sanction_end_date'], errors='coerce')
df['sanction_end_date'] = df['sanction_end_date'].dt.strftime('%Y-%m-%d')

df['eligible_reapply_date'] = pd.to_datetime(df['eligible_reapply_date'], errors='coerce')
df['eligible_reapply_date'] = df['eligible_reapply_date'].dt.strftime('%Y-%m-%d')

# Convert NPI to string
df['npi'] = df['npi'].astype(str).str.replace('.0', '', regex=False)
df['npi'] = df['npi'].replace('nan', None)

# Add state column
df['state'] = 'IA'

# Remove empty rows
df = df.dropna(how='all')

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# Must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Check results
print("=== MISSING DATA ===")
print(df.isnull().sum())
print("\nTotal rows:", len(df))
print("\nSample:")
print(df.head(3))

# Load into Postgres
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('iowa_exclusions', engine, if_exists='append', index=False)

print("\nDone! Iowa data loaded successfully.")