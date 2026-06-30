SELECT * FROM georgia_exclusions LIMIT 10;
SELECT COUNT(*) FROM georgia_exclusions;

SELECT * FROM illinois_exclusions LIMIT 10;
SELECT COUNT(*) FROM illinois_exclusions;

SELECT * FROM indiana_exclusions LIMIT 10;
SELECT COUNT(*) FROM indiana_exclusions;

SELECT * FROM iowa_exclusions LIMIT 10;
SELECT COUNT(*) FROM iowa_exclusions;

SELECT source_type,`	` source_table, COUNT(*) 
FROM main_exclusions 
GROUP BY source_type, source_table
ORDER BY source_type, source_table;

SELECT source_table, first_name, middle_name, last_name, business_name
FROM main_exclusions
WHERE source_table IN ('idaho_exclusions', 'illinois_exclusions', 'indiana_exclusions', 'kansas_exclusions')
ORDER BY RANDOM()
LIMIT 20;

SELECT source_table, first_name, middle_name, last_name, business_name
FROM main_exclusions
WHERE source_table NOT IN ('idaho_exclusions', 'illinois_exclusions', 'indiana_exclusions', 'kansas_exclusions')
ORDER BY RANDOM()
LIMIT 20;


SELECT column_name, data_type, character_maximum_length 
FROM information_schema.columns 
WHERE table_name = 'kansas_exclusions';

SELECT * FROM kansas_exclusions LIMIT 10;
SELECT COUNT(*) FROM kansas_exclusions;

SELECT * FROM kentucky_exclusions LIMIT 10;
SELECT COUNT(*) FROM kentucky_exclusions;

SELECT * FROM louisiana_exclusions LIMIT 10;
SELECT COUNT(*) FROM louisiana_exclusions;

SELECT * FROM hawaii_exclusions LIMIT 10;
SELECT COUNT(*) FROM hawaii_exclusions;

SELECT * FROM idaho_exclusions LIMIT 10;
SELECT COUNT(*) FROM idaho_exclusions;

SELECT * FROM maine_exclusions LIMIT 10;
SELECT COUNT(*) FROM maine_exclusions;

SELECT * FROM leie_exclusions LIMIT 10;
SELECT COUNT(*) FROM leie_exclusions;

SELECT source_type, source_table, COUNT(*) 
FROM main_exclusions 
GROUP BY source_type, source_table
ORDER BY source_type, source_table;

SELECT state, first_name, last_name, business_name, provider_type, exclusion_date, source_type
FROM main_exclusions
WHERE source_type = 'STATE'
ORDER BY RANDOM()
LIMIT 10;

SELECT source_table, first_name, middle_name, last_name
FROM main_exclusions
WHERE source_table IN ('idaho_exclusions', 'illinois_exclusions', 'indiana_exclusions', 'kansas_exclusions')
AND first_name = ''
AND middle_name = ''
LIMIT 20;

SELECT COUNT(*) FROM main_exclusions;

SELECT source_table, last_name, first_name, business_name 
FROM main_exclusions 
WHERE last_name ILIKE '%Global Medical Direct%';

SELECT source_table, first_name, last_name, business_name 
FROM main_exclusions 
WHERE last_name ILIKE '%(Owner%' 
   OR last_name ILIKE '%Owners:%';

SELECT source_table, business_name, reason, last_name, first_name
FROM main_exclusions 
WHERE business_name ILIKE '%Global Medical Direct%';

-- Check for other parenthetical patterns in names
SELECT source_table, last_name, first_name, business_name
FROM main_exclusions
WHERE last_name LIKE '%(%' OR first_name LIKE '%(%'
LIMIT 30;
