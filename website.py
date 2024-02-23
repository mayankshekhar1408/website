import streamlit as st
import pandas
st.set_page_config(layout="wide")
col1,col2=st.columns(2)

with col1:
    st.image("images/myphoto.jpg",width=300)
with col2:
    st.title("Mayank Shekhar")
    content="""
Hi, This is Mayank Shekhar.
I am having more than 10 years of experience in Telecom Industry handling different aspects of the domain.

I have worked in Nokia from 2011 to 2015 handling SDM Nodes( One-HLR, One-EIR & One-NDS) for the Tata Tele Services for PAN India.
Configuration and Fault Management.
Took care and owned the Change-Management of subscriber common profile.
Handled customer related, network stack related issues.
In depth MAP & SIGTRAN stack level knowledge on the ITU and 3GPP standards.
IP, SCTP, MTP, SCCP, TCAP, MAP

In 2015, I joined TOMIA as Sr. System Expert in the Cloud SI Team.
Major responsibilities were the project deliveries(Installation, Integration, Business Logic Implementation, iATP, CATP, Dry Run, Launch) 
in Cloud which was actually our datacenter with Physical and VMware virtual environment.
Customer Interaction for the integration of the product with operator's core network devices like HLR, HSS, STPs, DRAs, IN, CSCFs.
L3 support for the TOMIA Signaling Nodes( CCS, Probe, DA, SA)

"""
    st.info(content)

content2="""Hello There.ustomer Interaction for the integration of the product with operator's 
         core network devices like HLR, HSS, STPs, DRAs, IN,the product with operator's core
         ponsibilities were the project deliveries(Installation, Integration,  network devices li

"""

st.write(content2)
col3,empty_col,col4=st.columns([1.5,0.5,1.5])

df=pandas.read_csv("data.csv",sep=";")
with col3:
    for index,row in df[0::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        

with col4:
    for index,row in df[1::2].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])


