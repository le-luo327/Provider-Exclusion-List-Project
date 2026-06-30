DROP TABLE IF EXISTS georgia_exclusions;
DROP TABLE IF EXISTS hawaii_exclusions;
DROP TABLE IF EXISTS idaho_exclusions;
DROP TABLE IF EXISTS illinois_exclusions;
DROP TABLE IF EXISTS indiana_exclusions;
DROP TABLE IF EXISTS iowa_exclusions;
DROP TABLE IF EXISTS kansas_exclusions;
DROP TABLE IF EXISTS kentucky_exclusions;
DROP TABLE IF EXISTS louisiana_exclusions;
DROP TABLE IF EXISTS maine_exclusions;
DROP TABLE IF EXISTS leie_exclusions;

CREATE TABLE georgia_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    middle_name VARCHAR NOT NULL,
    business_name VARCHAR NOT NULL,
    general VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    exclusion_date VARCHAR NOT NULL,
    npi VARCHAR NOT NULL
);

CREATE TABLE hawaii_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    middle_initial VARCHAR NOT NULL,
    medicaid_provider_id VARCHAR NOT NULL,
    provider_type VARCHAR NOT NULL,
    exclusion_date VARCHAR NOT NULL,
    reinstatement_date VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'HI'
);

CREATE TABLE idaho_exclusions (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR NOT NULL,
    start_date VARCHAR NOT NULL,
    eligible_for_reinstatement VARCHAR NOT NULL,
    date_reinstated VARCHAR NOT NULL,
    additional_information VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'ID'
);

CREATE TABLE illinois_exclusions (
    id SERIAL PRIMARY KEY,
    provider_name VARCHAR NOT NULL,
    license_number VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    provider_type VARCHAR NOT NULL,
    action_date VARCHAR NOT NULL,
    action_type VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    zip_code VARCHAR NOT NULL
);

CREATE TABLE indiana_exclusions (
    id SERIAL PRIMARY KEY,
    provider_name VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    service_location VARCHAR NOT NULL,
    termination_date VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'IN'
);

CREATE TABLE iowa_exclusions (
    id SERIAL PRIMARY KEY,
    enrollment_type VARCHAR NOT NULL,
    specialty VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    affiliated_npi VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    business_name VARCHAR NOT NULL,
    sanction_type VARCHAR NOT NULL,
    effective_date VARCHAR NOT NULL,
    sanction_end_date VARCHAR NOT NULL,
    eligible_reapply_date VARCHAR NOT NULL,
    authority VARCHAR NOT NULL,
    license_type VARCHAR NOT NULL,
    license_number VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'IA'
);

CREATE TABLE kansas_exclusions (
    id SERIAL PRIMARY KEY,
    termination_date VARCHAR NOT NULL,
    business_name VARCHAR NOT NULL,
    provider_name VARCHAR NOT NULL,
    provider_type VARCHAR NOT NULL,
    kmap_provider_number VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    comments VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'KS'
);

CREATE TABLE kentucky_exclusions (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    license VARCHAR NOT NULL,
    effective_date VARCHAR NOT NULL,
    reason VARCHAR NOT NULL,
    timeframe VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'KY'
);

CREATE TABLE louisiana_exclusions (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    birthdate VARCHAR NOT NULL,
    affiliated_entity VARCHAR NOT NULL,
    provider_type VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    reason_exclusion VARCHAR NOT NULL,
    period_exclusion VARCHAR NOT NULL,
    reason_termination VARCHAR NOT NULL,
    exclusion_type VARCHAR NOT NULL,
    enrollment_prohibition_period VARCHAR NOT NULL,
    effective_date VARCHAR NOT NULL,
    reinstate_date VARCHAR NOT NULL,
    state_zip VARCHAR NOT NULL,
    program_office VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'LA'
);

CREATE TABLE maine_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    middle_initial VARCHAR NOT NULL,
    alias_last_name_1 VARCHAR NOT NULL,
    alias_first_name_1 VARCHAR NOT NULL,
    alias_last_name_2 VARCHAR NOT NULL,
    alias_first_name_2 VARCHAR NOT NULL,
    alias_last_name_3 VARCHAR NOT NULL,
    alias_first_name_3 VARCHAR NOT NULL,
    alias_last_name_4 VARCHAR NOT NULL,
    alias_first_name_4 VARCHAR NOT NULL,
    provider_type VARCHAR NOT NULL,
    exclusion_start_date VARCHAR NOT NULL,
    state VARCHAR NOT NULL DEFAULT 'ME'
);

CREATE TABLE leie_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    mid_name VARCHAR NOT NULL,
    business_name VARCHAR NOT NULL,
    general VARCHAR NOT NULL,
    specialty VARCHAR NOT NULL,
    upin VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    dob VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    city VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    zip VARCHAR NOT NULL,
    excl_type VARCHAR NOT NULL,
    excl_date VARCHAR NOT NULL,
    rein_date VARCHAR NOT NULL,
    waiver_date VARCHAR NOT NULL,
    waiver_state VARCHAR NOT NULL,
    source VARCHAR NOT NULL DEFAULT 'LEIE'
);
