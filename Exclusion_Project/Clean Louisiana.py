import pandas as pd
from sqlalchemy import create_engine

# Read Louisiana file - skip first row (title)
df = pd.read_excel('Louisiana list.xlsx', skiprows=1)

# Strip whitespace from column names (Louisiana has leading spaces)
df.columns = df.columns.str.strip()

print("Columns:", df.columns.tolist())

# Rename columns
df.columns = ['first_name', 'last_name', 'birthdate', 'affiliated_entity',
              'provider_type', 'npi', 'reason_exclusion', 'period_exclusion',
              'reason_termination', 'exclusion_type', 'enrollment_prohibition_period',
              'effective_date', 'reinstate_date', 'state_zip', 'program_office']

# Convert all date columns, then back to text since columns are VARCHAR now
df['birthdate'] = pd.to_datetime(df['birthdate'], errors='coerce')
df['birthdate'] = df['birthdate'].dt.strftime('%Y-%m-%d')

df['effective_date'] = pd.to_datetime(df['effective_date'], errors='coerce')
df['effective_date'] = df['effective_date'].dt.strftime('%Y-%m-%d')

df['reinstate_date'] = pd.to_datetime(df['reinstate_date'], errors='coerce')
df['reinstate_date'] = df['reinstate_date'].dt.strftime('%Y-%m-%d')

# Convert NPI to string
df['npi'] = df['npi'].astype(str).str.replace('.0', '', regex=False)
df['npi'] = df['npi'].replace('nan', None)

# Add state column
df['state'] = 'LA'

# Remove empty rows
df = df.dropna(how='all')

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# Must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Check results
print("\n=== MISSING DATA ===")
print(df.isnull().sum())
print("\nTotal rows:", len(df))
print("\nSample:")
print(df.head(3))

# Load into Postgres
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('louisiana_exclusions', engine, if_exists='append', index=False)

print("\nDone! Louisiana data loaded successfully.")