
import pandas as pd
import streamlit as st
from sqlalchemy import create_engine, URL

# Page configuration
st.set_page_config(
    page_title="Loan Analysis Dashboard",
    layout="wide"
)

# Dashboard title
st.title("Credit Risk Analysis Dashboard")
st.write("Loan Previous Application Analysis")

# MySQL connection
connection_url = URL.create(
    "mysql+pymysql",
    username="root",
    password="tamil",
    host="localhost",
    port=3306,
    database="loan_data"
)

engine = create_engine(connection_url)

# Load data
df = pd.read_sql(
    "select * from loan_previous_data",
    engine
)

# Loan application overview
st.subheader("Loan Application Overview")

col1, col2, col3 = st.columns(3)

col1.metric("Total Applications", len(df))

col2.metric(
    "Total Credit Amount",
    f"{df['AMT_CREDIT'].sum():,.2f}"
)

col3.metric(
    "Average Credit Amount",
    f"{df['AMT_CREDIT'].mean():,.2f}"
)

# Display sample data
st.subheader("Loan Application Data")
st.dataframe(df)
