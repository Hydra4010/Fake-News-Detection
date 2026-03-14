import streamlit as st
import pickle
import re

model = pickle.load(open("fake_news_model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"\W"," ",text)
    text = re.sub(r"\d"," ",text)
    text = re.sub(r"\s+"," ",text)
    return text

st.title("Fake News Detection System")

news = st.text_area("Enter News Text")

if st.button("Check News"):

    news = clean_text(news)
    
    vector = vectorizer.transform([news])
    
    prediction = model.predict(vector)
    
    if prediction[0] == 1:
        st.success("This is Real News")
    else:
        st.error("This is Fake News")