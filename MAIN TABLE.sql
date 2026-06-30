DROP TABLE IF EXISTS main_exclusions;

CREATE TABLE main_exclusions (
    id SERIAL PRIMARY KEY,
    source_table VARCHAR NOT NULL,
    source_type VARCHAR NOT NULL,
    state VARCHAR NOT NULL,
    first_name VARCHAR NOT NULL,
    middle_name VARCHAR NOT NULL,
    last_name VARCHAR NOT NULL,
    business_name VARCHAR NOT NULL,
    provider_type VARCHAR NOT NULL,
    npi VARCHAR NOT NULL,
    license_number VARCHAR NOT NULL,
    exclusion_date VARCHAR NOT NULL,
    reinstatement_date VARCHAR NOT NULL,
    reason VARCHAR NOT NULL
);
-- Georgia
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'georgia_exclusions', 'STATE', state, first_name, middle_name, last_name, business_name, general, npi, '', exclusion_date, '', ''
FROM georgia_exclusions;

-- Hawaii
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'hawaii_exclusions', 'STATE', state, first_name, middle_initial, last_name, '', provider_type, '', medicaid_provider_id, exclusion_date, reinstatement_date, ''
FROM hawaii_exclusions;

-- Idaho
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'idaho_exclusions', 'STATE', state, '', '', full_name, '', '', '', '', start_date, date_reinstated, additional_information
FROM idaho_exclusions;

-- Illinois
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'illinois_exclusions', 'STATE', state, '', '', provider_name, '', provider_type, npi, license_number, action_date, '', action_type
FROM illinois_exclusions;

-- Indiana
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'indiana_exclusions', 'STATE', state, '', '', provider_name, '', '', npi, '', termination_date, '', service_location
FROM indiana_exclusions;

-- Iowa
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'iowa_exclusions', 'STATE', state, first_name, '', last_name, business_name, specialty, npi, license_number, effective_date, sanction_end_date, sanction_type
FROM iowa_exclusions;

-- Kansas
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'kansas_exclusions', 'STATE', state, '', '', provider_name, business_name, provider_type, npi, kmap_provider_number, termination_date, '', comments
FROM kansas_exclusions;

-- Kentucky
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'kentucky_exclusions', 'STATE', state, first_name, '', last_name, '', '', npi, license, effective_date, '', reason || ' ' || timeframe
FROM kentucky_exclusions;

-- Louisiana
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'louisiana_exclusions', 'STATE', state, first_name, '', last_name, affiliated_entity, provider_type, npi, '', effective_date, reinstate_date, reason_exclusion || ' ' || reason_termination
FROM louisiana_exclusions;

-- Maine
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'maine_exclusions', 'STATE', state, first_name, middle_initial, last_name, '', provider_type, '', '', exclusion_start_date, '', ''
FROM maine_exclusions;

-- LEIE (federal)
INSERT INTO main_exclusions (source_table, source_type, state, first_name, middle_name, last_name, business_name, provider_type, npi, license_number, exclusion_date, reinstatement_date, reason)
SELECT 'leie_exclusions', 'FEDERAL', state, first_name, mid_name, last_name, business_name, general, npi, upin, excl_date, rein_date, excl_type
FROM leie_exclusions;