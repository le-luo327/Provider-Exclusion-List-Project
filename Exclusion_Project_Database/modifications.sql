ALTER TABLE georgia_exclusions 
ALTER COLUMN middle_name TYPE VARCHAR(200);

ALTER TABLE georgia_exclusions 
ALTER COLUMN general TYPE VARCHAR(200);

ALTER TABLE georgia_exclusions 
ALTER COLUMN business_name TYPE VARCHAR(500);

ALTER TABLE georgia_exclusions 
ALTER COLUMN state TYPE VARCHAR(50);

ALTER TABLE indiana_exclusions 
ALTER COLUMN npi TYPE VARCHAR(100);

ALTER TABLE indiana_exclusions 
ALTER COLUMN service_location TYPE VARCHAR(500);

DROP TABLE iowa_exclusions;

CREATE TABLE iowa_exclusions (
    id SERIAL PRIMARY KEY,
    enrollment_type VARCHAR(50),
    specialty VARCHAR(100),
    npi VARCHAR(20),
    affiliated_npi VARCHAR(20),
    last_name VARCHAR(100),
    first_name VARCHAR(100),
    business_name VARCHAR(200),
    sanction_type VARCHAR(200),
    effective_date DATE,
    sanction_end_date DATE,
    eligible_reapply_date DATE,
    authority VARCHAR(200),
    license_type VARCHAR(50),
    license_number VARCHAR(50),
    state VARCHAR(5) DEFAULT 'IA'
);

DROP TABLE kansas_exclusions;

CREATE TABLE kansas_exclusions (
    id SERIAL PRIMARY KEY,
    termination_date DATE,
    business_name VARCHAR(300),
    provider_name VARCHAR(300),
    provider_type VARCHAR(100),
    kmap_provider_number VARCHAR(50),
    npi VARCHAR(50),
    comments TEXT,
    state VARCHAR(5) DEFAULT 'KS'
);

ALTER TABLE kansas_exclusions ALTER COLUMN kmap_provider_number TYPE VARCHAR(200);
ALTER TABLE kansas_exclusions ALTER COLUMN npi TYPE VARCHAR(200);
ALTER TABLE kansas_exclusions ALTER COLUMN provider_type TYPE VARCHAR(200);

DROP TABLE kentucky_exclusions;

CREATE TABLE kentucky_exclusions (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(200),
    npi VARCHAR(50),
    license VARCHAR(50),
    effective_date DATE,
    reason VARCHAR(300),
    timeframe VARCHAR(200),
    state VARCHAR(5) DEFAULT 'KY'
);

DROP TABLE louisiana_exclusions;

CREATE TABLE louisiana_exclusions (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(200),
    birthdate DATE,
    affiliated_entity VARCHAR(300),
    provider_type VARCHAR(200),
    npi VARCHAR(50),
    reason_exclusion VARCHAR(300),
    period_exclusion VARCHAR(200),
    reason_termination VARCHAR(300),
    exclusion_type VARCHAR(200),
    enrollment_prohibition_period VARCHAR(200),
    effective_date DATE,
    reinstate_date DATE,
    state_zip VARCHAR(100),
    program_office VARCHAR(100),
    state VARCHAR(5) DEFAULT 'LA'
);

DROP TABLE hawaii_exclusions;

CREATE TABLE hawaii_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(150),
    first_name VARCHAR(150),
    middle_initial VARCHAR(20),
    medicaid_provider_id VARCHAR(50),
    provider_type VARCHAR(300),
    exclusion_date DATE,
    reinstatement_date VARCHAR(50),
    state VARCHAR(5) DEFAULT 'HI'
);

ALTER TABLE hawaii_exclusions ALTER COLUMN middle_initial TYPE VARCHAR(500);
ALTER TABLE hawaii_exclusions ALTER COLUMN last_name TYPE VARCHAR(500);
ALTER TABLE hawaii_exclusions ALTER COLUMN first_name TYPE VARCHAR(500);
ALTER TABLE hawaii_exclusions ALTER COLUMN provider_type TYPE VARCHAR(500);
ALTER TABLE hawaii_exclusions ALTER COLUMN reinstatement_date TYPE VARCHAR(50);

DROP TABLE idaho_exclusions;

CREATE TABLE idaho_exclusions (
    id SERIAL PRIMARY KEY,
    full_name VARCHAR(300),
    start_date DATE,
    eligible_for_reinstatement DATE,
    date_reinstated DATE,
    additional_information TEXT,
    state VARCHAR(5) DEFAULT 'ID'
);

DROP TABLE maine_exclusions;
 
CREATE TABLE maine_exclusions (
    id SERIAL PRIMARY KEY,
    last_name VARCHAR(200),
    first_name VARCHAR(100),
    middle_initial VARCHAR(10),
    alias_last_name_1 VARCHAR(200),
    alias_first_name_1 VARCHAR(100),
    alias_last_name_2 VARCHAR(200),
    alias_first_name_2 VARCHAR(100),
    alias_last_name_3 VARCHAR(200),
    alias_first_name_3 VARCHAR(100),
    alias_last_name_4 VARCHAR(200),
    alias_first_name_4 VARCHAR(100),
    provider_type VARCHAR(200),
    exclusion_start_date DATE,
    state VARCHAR(5) DEFAULT 'ME'
);

UPDATE main_exclusions
SET 
    business_name = TRIM(SPLIT_PART(last_name, '(', 1)),
    reason = CASE 
        WHEN reason = '' THEN TRIM(SPLIT_PART(last_name, '(', 2))
        ELSE reason || ' | ' || TRIM(SPLIT_PART(last_name, '(', 2))
    END,
    first_name = '',
    last_name = ''
WHERE last_name ILIKE '%(Owner%' 
   OR last_name ILIKE '%Owners:%';