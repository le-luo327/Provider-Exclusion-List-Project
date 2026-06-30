import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('LEIE database.csv', dtype=str, keep_default_na=False)

# Match the schema's column names
df = df.rename(columns={
    'LASTNAME': 'last_name',
    'FIRSTNAME': 'first_name',
    'MIDNAME': 'mid_name',
    'BUSNAME': 'business_name',
    'GENERAL': 'general',
    'SPECIALTY': 'specialty',
    'UPIN': 'upin',
    'NPI': 'npi',
    'DOB': 'dob',
    'ADDRESS': 'address',
    'CITY': 'city',
    'STATE': 'state',
    'ZIP': 'zip',
    'EXCLTYPE': 'excl_type',
    'EXCLDATE': 'excl_date',
    'REINDATE': 'rein_date',
    'WAIVERDATE': 'waiver_date',
    'WVRSTATE': 'waiver_state',
})

text_cols = ['last_name', 'first_name', 'mid_name', 'business_name', 'general',
             'specialty', 'upin', 'address', 'city', 'state', 'zip',
             'excl_type', 'waiver_state']
df[text_cols] = df[text_cols].replace(['', 'NULL'], None)

# NPI uses '0000000000' as its "no NPI on file" sentinel
df['npi'] = df['npi'].replace('0000000000', None)

# Date columns: YYYYMMDD strings, with '00000000' meaning "not applicable"
# Convert to datetime for validation, then back to text (column is VARCHAR now)
for col in ['dob', 'excl_date', 'rein_date', 'waiver_date']:
    df[col] = pd.to_datetime(df[col], format='%Y%m%d', errors='coerce')
    df[col] = df[col].dt.strftime('%Y-%m-%d')

# Federal list, not state-specific -- see schema note
df['source'] = 'LEIE'

# Fill any remaining missing values with empty string (required for NOT NULL columns)
# Must come AFTER date conversion, since date conversion can create new nulls
df = df.fillna('')

# Check results
print("=== MISSING DATA ===")
print(df.isnull().sum())
print("\nTotal rows:", len(df))
print("\nSample:")
print(df.head(10))

# Load into Postgres. chunksize keeps memory/parameter counts sane for ~83K rows.
engine = create_engine('postgresql://postgres@localhost/exclusion_list_db')
df.to_sql('leie_exclusions', engine, if_exists='append', index=False, chunksize=5000)

print("\nDone! LEIE data loaded successfully.")