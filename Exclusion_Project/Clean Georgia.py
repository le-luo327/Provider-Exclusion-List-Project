import pandas as pd
from sqlalchemy import create_engine

# Read the Georgia file
df = pd.read_excel('Georgia List.xlsx', skiprows=2)

# Rename all 9 columns including the extra empty one
df.columns = ['last_name', 'first_name', 'middle_name', 'business_name', 
              'general', 'state', 'exclusion_date', 'npi', 'extra']

# Drop the extra empty column
df = df.drop(columns=['extra'])

# Convert date from number format (19820415) to proper date, then back to string
df['exclusion_date'] = pd.to_datetime(df['exclusion_date'], format='%Y%m%d', errors='coerce')
df['exclusion_date'] = df['exclusion_date'].dt.strftime('%Y-%m-%d')

# Remove empty rows
df = df.dropna(how='all')

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# This must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Connect to your local Postgres database
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')

# Load data into georgia_exclusions table
df.to_sql('georgia_exclusions', engine, if_exists='append', index=False)

print("Done! Georgia data loaded successfully.")
print("Total rows loaded:", len(df))