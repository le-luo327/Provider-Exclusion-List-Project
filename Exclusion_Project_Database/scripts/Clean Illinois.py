import pandas as pd
from sqlalchemy import create_engine

# Read Illinois file with calamine engine
df = pd.read_excel('Illinois list.xlsx', sheet_name='Active Sanctions', engine='calamine')

# Rename columns
df.columns = ['provider_name', 'license_number', 'npi', 'provider_type',
              'affiliation', 'action_date', 'action_type', 'address',
              'address2', 'city', 'state', 'zip_code']

# Dates already converted by calamine; convert back to text since column is VARCHAR now
df['action_date'] = pd.to_datetime(df['action_date'], errors='coerce')
df['action_date'] = df['action_date'].dt.strftime('%Y-%m-%d')

# Drop columns we don't need
df = df.drop(columns=['affiliation', 'address2'])

# Remove empty rows
df = df.dropna(how='all')

# Convert NPI to string to avoid decimal issues
df['npi'] = df['npi'].astype(str).str.replace('.0', '', regex=False)
df['npi'] = df['npi'].replace('nan', None)

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# Must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Connect to Postgres and load
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('illinois_exclusions', engine, if_exists='append', index=False)

print("Done! Illinois data loaded successfully.")
print("Total rows loaded:", len(df))