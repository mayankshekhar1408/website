import streamlit as st
import pandas

st.set_page_config(layout="wide")
col1,col2,col3=st.columns(3)
comanyname="The Best Company"
with col1:
    st.title(comanyname)

st.info("""The Best Company is the most advanced company in the AI business.It is delivering worldwide applications.
        """)
st.subheader("Our Team")

col4,empty_col1,col5,empty_col2,col6=st.columns([1.5,0.5,1.5,0.5,1.5])

df=pandas.read_csv("websitecompany/data.csv")
with col4:
    for index,row in df[0::3].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("websitecompany/images/"+row["image"])

with col5:
    for index,row in df[1::3].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("websitecompany/images/"+row["image"])

with col6:
    for index,row in df[2::3].iterrows():
        st.header(f'{row["first name"].title()} {row["last name"].title()}')
        st.write(row["role"])
        st.image("websitecompany/images/"+row["image"])

