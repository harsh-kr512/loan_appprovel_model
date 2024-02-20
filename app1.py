import streamlit as st

st.title("loan Approval App")
client_name = st.text_input("enter your name:")
income = st.number_input("enter your monthly income:")
credit_score = st.number_input("Enter your cridit score:")
loan_amount = st.number_input("Enter requested loan amount:")

st.button("check loan eligibility")
if income >= 30000 and credit_score >= 500 and loan_amount >= 1500000:
    st.success(f"congratulations! {client_name} is eligible for the loan.")
else:
    st.error(f"sorry ,{client_name} is not eligible for the loan.")