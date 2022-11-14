import streamlit as st
import joblib
model = joblib.load('spam_ham')
st.title('SPAM-HAM CLASSIFIER') 
ip = st.text_input('enter the msg')
op = model.predict([ip])
if st.button('predict'):
 st.title(op[0])
