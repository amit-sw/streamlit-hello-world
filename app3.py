import streamlit as st

m="Initial text"
st.write('User said initially:', m)
m = st.text_input('Say something', 'Edit here')
st.write('User said finally:', m)
