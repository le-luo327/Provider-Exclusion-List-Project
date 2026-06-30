CREATE TABLE georgia_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    license_number VARCHAR(50),
    exclusion_type VARCHAR(100),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'GA'
);

CREATE TABLE hawaii_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_initial VARCHAR(5),
    medicaid_provider_id VARCHAR(20),
    provider_type VARCHAR(100),
    exclusion_date DATE,
    reinstatement_date VARCHAR(50),
    state VARCHAR(5) DEFAULT 'HI'
);

CREATE TABLE idaho_exclusions (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(200),
    start_date DATE,
    eligible_for_reinstatement DATE,
    date_reinstated DATE,
    additional_information TEXT,
    state VARCHAR(5) DEFAULT 'ID'
);

CREATE TABLE illinois_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    license_number VARCHAR(50),
    exclusion_type VARCHAR(100),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'IL'
);

CREATE TABLE indiana_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'IN'
);

CREATE TABLE iowa_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'IA'
);

CREATE TABLE kansas_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'KS'
);

CREATE TABLE kentucky_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'KY'
);

CREATE TABLE louisiana_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'LA'
);

CREATE TABLE maine_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    middle_name VARCHAR(50),
    business_name VARCHAR(200),
    npi VARCHAR(20),
    exclusion_date DATE,
    reinstatement_date DATE,
    state VARCHAR(5) DEFAULT 'ME'
);