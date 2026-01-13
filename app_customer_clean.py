import streamlit as st
import pandas as pd
import numpy as np
import re

# --------------------------------------------------
# Page Config
# --------------------------------------------------
st.set_page_config(
    page_title="Customer Input Data Cleaning Pipeline",
    layout="wide"
)

# --------------------------------------------------
# Title
# --------------------------------------------------
st.markdown(
    """
    <h1 style='text-align:center;'>🧹 Customer Input Data Cleaning Pipeline</h1>
    <p style='text-align:center; font-size:18px;'>
    Clean messy customer data instantly with a smart, interactive pipeline
    </p>
    """,
    unsafe_allow_html=True
)

st.divider()

# --------------------------------------------------
# File Upload
# --------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload customer data file (CSV or Excel)",
    type=["csv", "xlsx"]
)

if uploaded_file is None:
    st.info("👆 Upload a CSV or Excel file to begin")
    st.stop()

# 🔴 CRITICAL STREAMLIT FIX
uploaded_file.seek(0)

# --------------------------------------------------
# Safe File Reading (FINAL)
# --------------------------------------------------
try:
    file_name = uploaded_file.name.lower()

    if file_name.endswith(".csv"):
        df_raw = pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        df_raw = pd.read_excel(uploaded_file, engine="openpyxl")

    else:
        st.error("❌ Unsupported file format.")
        st.stop()

except Exception as e:
    st.error("❌ Failed to read file.")
    st.code(str(e))
    st.stop()

# --------------------------------------------------
# Dataset Overview
# --------------------------------------------------
st.subheader("📊 Dataset Overview")

c1, c2, c3 = st.columns(3)
c1.metric("Total Rows", df_raw.shape[0])
c2.metric("Total Columns", df_raw.shape[1])
c3.metric("Missing Values", int(df_raw.isnull().sum().sum()))

st.divider()

# --------------------------------------------------
# Profiling
# --------------------------------------------------
tab1, tab2, tab3 = st.tabs(
    ["📄 Raw Data", "🔍 Missing Values", "🧬 Duplicates"]
)

with tab1:
    st.dataframe(df_raw.head(10))

with tab2:
    missing_df = df_raw.isnull().sum().reset_index()
    missing_df.columns = ["Column", "Missing Count"]
    st.dataframe(missing_df)

with tab3:
    dup_count = df_raw.duplicated().sum()
    st.write(f"Total duplicate rows: **{dup_count}**")

st.divider()

# --------------------------------------------------
# Cleaning Options
# --------------------------------------------------
st.subheader("🧹 Cleaning Options")

col1, col2, col3 = st.columns(3)

remove_duplicates = col1.checkbox("Remove duplicate rows", value=True)
clean_text = col2.checkbox("Clean text columns", value=True)
handle_missing = col3.checkbox("Handle missing values", value=True)

# --------------------------------------------------
# Run Cleaning
# --------------------------------------------------
if st.button("✨ Run Cleaning Pipeline"):
    df_cleaned = df_raw.copy()

    df_cleaned.columns = (
        df_cleaned.columns.str.lower()
        .str.strip()
        .str.replace(" ", "_")
    )

    if remove_duplicates:
        df_cleaned = df_cleaned.drop_duplicates()

    if clean_text:
        for col in df_cleaned.select_dtypes(include="object").columns:
            df_cleaned[col] = (
                df_cleaned[col]
                .astype(str)
                .str.lower()
                .str.strip()
                .str.replace(r"[^a-z0-9\s]", "", regex=True)
            )

    if handle_missing:
        df_cleaned = df_cleaned.fillna("unknown")

    st.success("✅ Data cleaned successfully!")

    b1, b2 = st.columns(2)
    with b1:
        st.write("❌ Before Cleaning")
        st.dataframe(df_raw.head())

    with b2:
        st.write("✅ After Cleaning")
        st.dataframe(df_cleaned.head())

    st.divider()

    st.download_button(
        "⬇️ Download Cleaned Data (CSV)",
        data=df_cleaned.to_csv(index=False),
        file_name="cleaned_customer_data.csv",
        mime="text/csv"
    )
