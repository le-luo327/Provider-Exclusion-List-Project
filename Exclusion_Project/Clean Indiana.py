import pandas as pd
from sqlalchemy import create_engine

# Read Indiana file
df = pd.read_excel('Indiana list.xlsx', skiprows=1)

# Rename columns
df.columns = ['provider_name', 'npi', 'service_location', 'termination_date']

# Convert dates, then back to text since column is VARCHAR now
df['termination_date'] = pd.to_datetime(df['termination_date'], errors='coerce')
df['termination_date'] = df['termination_date'].dt.strftime('%Y-%m-%d')

# Convert NPI to string to avoid decimal issues
df['npi'] = df['npi'].astype(str).str.replace('.0', '', regex=False)
df['npi'] = df['npi'].replace('nan', None)

# Add state column
df['state'] = 'IN'

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
df.to_sql('indiana_exclusions', engine, if_exists='append', index=False)

print("\nDone! Indiana data loaded successfully.")