import streamlit as st

st.write("This page is online")

box=st.slider("Gaetano please insert a number",1,30)

st.text(box)

box=st.slider("Please insert another number",30,300)

st.text(box)