import pandas as pd
from sqlalchemy import create_engine

# Read Kentucky file - skip first 2 rows (title + blank)
df = pd.read_excel('Kentucky list.xlsx', skiprows=2)

# Rename columns
df.columns = ['first_name', 'last_name', 'npi', 'license',
              'effective_date', 'reason', 'timeframe']

# Convert dates, then back to text since column is VARCHAR now
df['effective_date'] = pd.to_datetime(df['effective_date'], errors='coerce')
df['effective_date'] = df['effective_date'].dt.strftime('%Y-%m-%d')

# Convert NPI and license to string
df['npi'] = df['npi'].astype(str).str.replace('.0', '', regex=False)
df['npi'] = df['npi'].replace('nan', None)

df['license'] = df['license'].astype(str).str.replace('.0', '', regex=False)
df['license'] = df['license'].replace('nan', None)

# Add state column
df['state'] = 'KY'

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
print(df.head(5))

# Load into Postgres
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('kentucky_exclusions', engine, if_exists='append', index=False)

print("\nDone! Kentucky data loaded successfully.")