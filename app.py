
import streamlit as st

st.set_page_config(page_title="AISE Deployment Demo")

st.title("AI-Enabled Software Engineering")
st.header("Cloud Deployment Demonstration")

st.write("This application is running as a cloud deployment demo.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name.strip():
        st.success(f"Hello, {name}! Your application is working.")
    else:
        st.warning("Please enter your name.")

st.divider()
st.subheader("Deployment Check")
st.write("If you can see this page and use the button, the application is running.")
