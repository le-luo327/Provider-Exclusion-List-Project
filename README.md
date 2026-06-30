 # Provider Exclusion List Project

A comprehensive database and search tool for Medicaid/Medicare provider exclusion lists across 10 states and the federal LEIE database.

---

## 📋 Project Overview

This project collects, cleans, and consolidates provider exclusion data from multiple sources into a unified PostgreSQL database, with a Django web application for searching excluded providers.

**Data Sources:**
- 10 state Medicaid exclusion lists
- Federal HHS OIG LEIE (List of Excluded Individuals/Entities) database

**Total Records:** ~97,400+ providers across all sources

---

## 🗺️ States Covered

| State | Format | Records |
|-------|--------|---------|
| Georgia | XLSX | 1,370 |
| Hawaii | PDF | 213 |
| Idaho | PDF | 171 |
| Illinois | XLSX | 3,229 |
| Indiana | XLSX | 151 |
| Iowa | XLSX | 1,272 |
| Kansas | XLSX | 199 |
| Kentucky | XLSX | 397 |
| Louisiana | XLSX | 5,880 |
| Maine | PDF | 1,108 |
| LEIE (Federal) | CSV | 83,464 |

---

## 🗂️ Project Structure
```
Provider-Exclusion-List-Project/
├── Exclusion_Project_Database/
│   ├── Original_Data/        ← Raw source files (XLSX, CSV, PDF)
│   ├── Cleaned_Data/         ← Python data cleaning scripts
│   └── SQL/                  ← Database schema and query files
├── Exclusion_Project_Search/  ← Django web search application
├── Weekly Reports/            ← Weekly progress reports
└── .gitignore
```

---

## ⚙️ Tech Stack

- **Python** — pandas, pdfplumber, sqlalchemy, python-calamine
- **PostgreSQL** — database storage and querying
- **PgAdmin 4** — database management
- **Django** — web search application

---

## 🔧 Setup

### 1. Install Dependencies

```bash
pip3 install pandas openpyxl psycopg2-binary sqlalchemy django pdfplumber python-calamine
```

### 2. Set Up PostgreSQL Database
Create a database called exclusion_list_db in PostgreSQL, then run the SQL schema files in this order:
1. SQL/revised-not null:varchar.sql — Creates all staging tables
2. SQL/MAIN TABLE.sql — Creates the unified main table

### 3. Run Data Cleaning Scripts

Run each cleaning script from the `Cleaned_Data/` folder:

```bash
python3 "Clean Georgia.py"
python3 "Clean Hawaii.py"
python3 "Clean Idaho.py"
python3 "Clean Illinois.py"
python3 "Clean Indiana.py"
python3 "Clean Iowa.py"
python3 "Clean Kansas.py"
python3 "Clean Kentucky.py"
python3 "Clean Kentucky.py"
python3 "Clean Louisiana.py"
python3 "Clean Maine.py"
python3 "Clean LEIE.py"
```

### 4. Run the Name Split Script

```bash
python3 split_names.py
```

This separates combined name fields (Idaho, Illinois, Indiana, Kansas) into first/middle/last name columns.

### 5. Start the Django Search App

```bash
cd Exclusion_Project_Search
python3 manage.py runserver
```

Visit `http://127.0.0.1:8000/` to search the exclusion database.

---

## 🔍 Search Features

- Search by **name** (first, last, or business name)
- Search by **NPI** (National Provider Identifier)
- Results show: Last Name, First Name, Business Name, State, Source, Exclusion Date, NPI
- **Relevance-based sorting**: exact matches → starts-with → contains
- **Pagination**: 100 results per page
- Color-coded badges: **MEDICARE** (federal) vs **MEDICAID** (state)

---

## 🗄️ Database Structure

### Staging Tables (11 total)
One table per source, preserving the original structure of each state's data.

### Main Table (`main_exclusions`)
Unified table combining all sources with standardized columns:

| Column | Description |
|--------|-------------|
| `source_table` | Original staging table name |
| `source_type` | `FEDERAL` or `STATE` |
| `state` | 2-letter state code |
| `first_name` | Provider first name |
| `middle_name` | Provider middle name |
| `last_name` | Provider last name |
| `business_name` | Entity/business name |
| `provider_type` | Provider role/specialty |
| `npi` | National Provider Identifier |
| `license_number` | License or ID number |
| `exclusion_date` | Date of exclusion |
| `reinstatement_date` | Date of reinstatement (if applicable) |
| `reason` | Reason for exclusion |

---

## 📊 Data Challenges Solved

- **PDF extraction** — Used `pdfplumber` for Hawaii, Idaho, and Maine lists
- **Excel date serial numbers** — Converted numeric dates (e.g., `45826`) to readable format
- **Combined name fields** — Split full names into first/middle/last for Idaho, Illinois, Indiana, Kansas
- **Inconsistent column names** — Standardized across all 11 sources
- **Mixed date formats** — Normalized all dates to `YYYY-MM-DD`
- **Business names embedded in name fields** — Cleaned and moved to `business_name` column

---

## 📅 Development Timeline

- **Week 1-2**: Data collection and research across 10 states
- **Week 3-4**: PostgreSQL setup, staging table design, data cleaning scripts
- **Week 5-6**: Main table creation, name splitting, data quality fixes
- **Week 7**: Django web application development and UI refinement
- **Week 8**: GitHub upload and project documentation

---

## 👤 Developer

- **Developer**: Le Luo
- **Repository**: https://github.com/le-luo327/Provider-Exclusion-List-Project
- **Internship**: EMRTS Intern 2026

---

*Last Updated: June 2026*