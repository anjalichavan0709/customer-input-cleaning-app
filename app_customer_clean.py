import streamlit as st
import pandas as pd
import numpy as np
import re
from io import BytesIO

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

# --------------------------------------------------
# Safe File Reading (FINAL)
# --------------------------------------------------
df_raw = None
file_name = uploaded_file.name.lower()

try:
    if file_name.endswith(".csv"):
        df_raw = pd.read_csv(uploaded_file)

    elif file_name.endswith(".xlsx"):
        try:
            df_raw = pd.read_excel(
                BytesIO(uploaded_file.getvalue()),
                engine="openpyxl"
            )
        except ImportError:
            st.error(
                "❌ Excel support requires **openpyxl**, which is not available "
                "in this Streamlit environment.\n\n"
                "✅ **Solution:** Upload a CSV file instead."
            )
            st.stop()

    else:
        st.error("❌ Unsupported file type.")
        st.stop()

except Exception as e:
    st.error("❌ Failed to read file. Please upload a valid CSV or Excel file.")
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
# Data Profiling
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

with col1:
    remove_duplicates = st.checkbox("Remove duplicate rows", value=True)

with col2:
    clean_text = st.checkbox("Clean text columns", value=True)

with col3:
    handle_missing = st.checkbox("Handle missing values", value=True)

# --------------------------------------------------
# Run Cleaning
# --------------------------------------------------
if st.button("✨ Run Cleaning Pipeline"):
    df_cleaned = df_raw.copy()

    # Standardize column names
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

    # Before vs After
    st.subheader("🔄 Before vs After")

    b1, b2 = st.columns(2)

    with b1:
        st.write("❌ Before Cleaning")
        st.dataframe(df_raw.head())

    with b2:
        st.write("✅ After Cleaning")
        st.dataframe(df_cleaned.head())

    # Summary
    st.subheader("📈 Cleaning Summary")

    s1, s2, s3 = st.columns(3)
    s1.metric("Rows Before", df_raw.shape[0])
    s2.metric("Rows After", df_cleaned.shape[0])
    s3.metric("Rows Removed", df_raw.shape[0] - df_cleaned.shape[0])

    st.divider()

    st.download_button(
        label="⬇️ Download Cleaned Data (CSV)",
        data=df_cleaned.to_csv(index=False),
        file_name="cleaned_customer_data.csv",
        mime="text/csv"
    )
