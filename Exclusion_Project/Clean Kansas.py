import pandas as pd
from sqlalchemy import create_engine

# Read Kansas file - skip first row (title row)
df = pd.read_excel('Kansas list.xlsx', skiprows=1)

# Rename columns
df.columns = ['termination_date', 'business_name', 'provider_name',
              'provider_type', 'kmap_provider_number', 'npi', 'comments']

# Dates already in datetime format; convert back to text since column is VARCHAR now
df['termination_date'] = pd.to_datetime(df['termination_date'], errors='coerce')
df['termination_date'] = df['termination_date'].dt.strftime('%Y-%m-%d')

# Convert NPI to string to avoid decimal issues
df['npi'] = df['npi'].astype(str).str.replace('.0', '', regex=False)
df['npi'] = df['npi'].replace('nan', None)

# Add state column
df['state'] = 'KS'

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
df.to_sql('kansas_exclusions', engine, if_exists='append', index=False)

print("\nDone! Kansas data loaded successfully.")