import streamlit as st
page = st.sidebar.selectbox("Select a page", ["Dashboard", "Page 1", "Page 2"])

if page == "page1":
    st.title("page 1")
    st.write("test test 123")