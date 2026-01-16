# NER-Model

## Automated Resume Parser with UI, Multi-File Processing & Database Integration

---

## 1. Project Overview

This project implements an end-to-end **Named Entity Recognition (NER)–based Resume Parsing System** that automatically extracts structured candidate information from resumes in **PDF, DOCX, and image formats**.

The system eliminates manual resume screening by using **NLP, Regex rules, OCR, and database integration**, all wrapped inside a **user-friendly UI**.

---

## 2. What is Named Entity Recognition (NER)?

**Named Entity Recognition (NER)** is a Natural Language Processing (NLP) technique used to identify and classify important information (entities) from unstructured text.

### Entities extracted in this project:

* Candidate Name
* Email ID
* Phone Number
* Technical Skills (section-based)
* Projects
* Experience Highlights (optional)

---

## 3. Complete Pipeline & Technologies Used

The system supports **bulk resume uploads** and processes them end-to-end using the following technologies:

### 3.1 spaCy

* Loads pretrained NLP model (`en_core_web_sm`)
* Performs tokenization and sentence segmentation
* Extracts base entities such as PERSON and ORG

### 3.2 pdfplumber

* Extracts text from text-based PDF resumes

### 3.3 python-docx

* Reads and parses DOCX resumes

### 3.4 pytesseract (OCR)

* Extracts text from scanned PDFs and image-based resumes

### 3.5 Regex (re module)

Used for rule-based extraction of:

* Email IDs
* Phone numbers
* Section headers
* Project titles

### 3.6 phonenumbers

* Validates phone numbers
* Formats numbers correctly
* Removes invalid or incomplete contacts

### 3.7 pandas

* Creates and cleans DataFrames
* Merges multiple CSV outputs
* Prepares structured data for storage

### 3.8 MySQL Connector

* Connects Python with MySQL
* Inserts cleaned candidate data into database tables

---

## 4. Improved Skill Extraction System

Earlier versions detected random words as skills. This system was optimized for accuracy.

### 4.1 Section-Based Skill Extraction

Skills are extracted only from the following sections:

* Skills
* Technical Skills
* Technologies
* Tools
* Key Skills
* Tech Stack

**Process:**

1. Identify skill section
2. Extract text until the next heading
3. Clean extracted text
4. Filter technical terms only

### 4.2 Duplicate Skill Removal

* Skills are converted into a set
* Ensures all skills are unique

### 4.3 Clean Technical Skills Only

The system removes:

* Stopwords
* Soft skills (communication, leadership)
* Non-technical keywords

---

## 5. Project Extraction Logic

Project titles are detected using:

* Keywords such as project, developed, implemented, built, created
* Bullet-point patterns
* Title-case detection

---

## 6. Output Generated

Each resume generates structured CSV outputs:

### 6.1 names.csv

* Clean candidate names

### 6.2 emails.csv

* Verified email IDs

### 6.3 phones.csv

* Valid phone numbers
* Duplicate-free
* Country-aware formatting

### 6.4 skills.csv

* Technical skills only
* Section-based extraction
* No duplicates

### 6.5 projects.csv

* Clean project titles

Each CSV contains a `file` column to enable merging.

---

## 7. User Interface (UI)

A fully functional UI was developed for ease of use.

### UI Features:

* Upload multiple resumes at once
* One-click pipeline execution
* Live processing logs
* File-wise status tracking
* Automatic result updates
* No manual folder path required
* Accessible via local IP

**Example Access URL:**

```
http://192.168.1.5:5000
```

---

## 8. Database Integration (MySQL)

### 8.1 Process Followed

1. Read all generated CSV files
2. Merge into a single DataFrame
3. Remove duplicate records
4. Insert cleaned data into MySQL

### 8.2 Final Database Schema

* file
* name
* email
* phone
* skills
* projects

This enables dashboards, analytics, and candidate search.

---

## 9. System Workflow (End-to-End)

```
Upload → Extract → NER → Clean → CSV → MySQL → Snowflake → Power BI → UI
```

---

## 10. Final Result / Current Status

The project is fully implemented and functional with:

* End-to-end automated resume parsing
* Multi-file upload support
* OCR for image-based resumes
* Accurate section-based skill extraction
* De-duplicated skills and contacts
* Clean CSV outputs
* Automatic MySQL insertion
* Fully working UI via local IP
* Real-time processing logs

---

## 11. Conclusion

This project demonstrates a production-ready NER pipeline combining NLP, rule-based extraction, OCR, database integration, and UI-based automation, significantly reducing manual effort and improving resume screening accuracy.

<img src="Screenshot 2025-12-20 234551" alt="NER Project Screenshot" width="800">
