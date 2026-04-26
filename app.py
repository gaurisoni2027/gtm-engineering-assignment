import streamlit as st
import pandas as pd

st.set_page_config(page_title="GTM Dashboard", layout="wide")

st.title("GTM Outreach Dashboard")
st.write("CAMX 2025 Exhibitor Outreach Tool")

df = pd.read_csv("final_output.csv")

col1, col2, col3 = st.columns(3)

col1.metric("Total Companies", len(df))
col2.metric("Ready for Outreach", len(df[df["Status"] == "Ready for Outreach"]))
col3.metric("Personalized Lines", len(df))

st.subheader("Company Data")
st.dataframe(df, use_container_width=True)

company = st.selectbox("Select Company", df["Company Name"])

row = df[df["Company Name"] == company].iloc[0]

st.subheader("Selected Company Details")
st.write("Website:", row["Website"])
st.write("Industry:", row["Industry"])
st.write("First Line:")
st.info(row["Personalized First Line"])

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Download CSV",
    csv,
    "final_output.csv",
    "text/csv"
)