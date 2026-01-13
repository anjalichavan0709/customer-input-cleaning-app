# 🧹 Customer Input Data Cleaning Pipeline

An interactive Streamlit application designed to clean messy customer datasets efficiently using a configurable and transparent data cleaning pipeline.

---

## 🚀 Features

- Upload customer data in **CSV or Excel** format  
- Dataset overview including rows, columns, and missing values  
- Missing value analysis by column  
- Duplicate record detection  
- Interactive cleaning options:
  - Remove duplicate rows  
  - Clean text columns  
  - Handle missing values  
- Before and after data comparison  
- Download cleaned dataset as a CSV file  

---

## 🔄 Data Cleaning Pipeline Explanation

The application follows a structured data cleaning pipeline:

1. The user uploads a CSV or Excel file containing customer data  
2. The application displays basic dataset statistics and profiling information  
3. Missing values and duplicate records are identified and shown  
4. The user selects the required cleaning operations through the interface  
5. The selected cleaning steps are applied sequentially to the dataset  
6. A cleaned dataset is generated and made available for download  

This approach ensures clarity, user control, and transparency throughout the data cleaning process.

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Pandas  
- NumPy  

---

## 📂 Project Structure

customer_input_cleaning_app/
│
├── app_customer_clean.py
├── requirements.txt
└── README.md

---

## ▶️ How to Run the Application Locally

1. Navigate to the project folder  
2. Install the required dependencies:
pip install -r requirements.txt

3. Run the Streamlit application:
streamlit run app_customer_clean.py


---

## 📌 Use Case

This application is useful for data analysts, data science students, and beginners who need to clean raw customer input data before analysis or machine learning tasks.

