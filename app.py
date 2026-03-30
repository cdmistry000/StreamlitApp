import streamlit as st

st.set_page_config(page_title="My Streamlit App", page_icon="🚀", layout="centered")

st.title("🚀 My First Streamlit App")
st.write("Hello world! This app is deployed on **Streamlit Community Cloud**.")

name = st.text_input("What's your name?")
if name:
    st.success(f"Welcome, {name}! 👋")

st.divider()
st.caption("Built with Streamlit • Deployed on streamlit.io")
