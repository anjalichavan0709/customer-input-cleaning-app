# 🧹 Customer Input Data Cleaning App

An interactive **Streamlit web application** designed to clean messy customer text data using a configurable and transparent data-cleaning pipeline.

---

## 📌 App Overview

Customer-generated text data such as social media comments or feedback is often noisy, inconsistent, and unstructured.  
This application provides a simple interface to inspect, clean, and export such data, making it ready for analytics or NLP workflows.

---

## 🚀 Features

- 📤 Upload customer data in **CSV format**
- 📊 Dataset overview:
  - total rows
  - total columns
  - missing values
- 🔍 Data profiling:
  - raw data preview
  - missing value summary
  - duplicate detection
- 🧹 Interactive cleaning options:
  - remove duplicate rows
  - clean text columns (lowercase, remove special characters)
  - handle missing values
- 🔄 Before vs After comparison
- ⬇️ Download cleaned dataset as CSV

---

## 🗂️ App Structure

customer_input_cleaning_app/
│
├── app_customer_clean.py
├── requirements.txt
└── README.md

---

## 📄 Accepted Input Format

### CSV only (intentional design decision)

The application accepts **CSV files** as input.

Although the original dataset was available in Excel (.xlsx) format, CSV was chosen for the Streamlit application to ensure:

- stable deployment on Streamlit Cloud  
- no dependency on optional Excel libraries (`openpyxl`)  
- faster and more reliable file ingestion  
- alignment with industry-standard production pipelines  

The raw Excel file was converted to CSV **without any modification to the data**.

---

## 🧠 Technical Note

The Streamlit application focuses exclusively on **data cleaning and processing**.  
File format conversion (Excel → CSV) was intentionally handled outside the app to avoid deployment instability and maintain data integrity.

This separation reflects real-world best practices between experimentation and production systems.

---

## 📦 Dependencies

The application requires the following libraries:
streamlit
pandas
numpy

---

## ✅ Output

- Cleaned customer dataset
- Downloadable in CSV format
- Ready for analytics or NLP workflows

---

## 🎯 Summary

This application demonstrates:
- practical data-cleaning workflows
- clear separation between raw data handling and processing
- deployment-aware engineering decisions
- clean and modular Streamlit UI design

