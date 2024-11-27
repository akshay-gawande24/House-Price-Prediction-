import streamlit as st
import numpy as np
import pickle

model = pickle.load(open('akshay24.pkl','rb'))


# let's create web app
st.title("House Price Prediction ")
Bedrooms = st.text_input('Enter Bedrooms')
Bathrooms = st.text_input("Enter Bathrooms")
Sqft_living = st.text_input("Enter sqft_living")
Sqft_lot = st.text_input("Enter sqft_lot")
Floors = st.text_input("Enter floors")
Price_per_sqfeet = st.text_input("Enter price_per_sqfeet")


if st.button("predict"):
    Bedrooms = float(Bedrooms)
    Bathrooms = float(Bathrooms) if Bathrooms else 0.0
    Sqft_living = float(Sqft_living) if Sqft_living else 0.0
    Sqft_lot = float(Sqft_lot) if Sqft_lot else 0.0
    Floors = float(Floors) if Floors else 0.0
    Price_per_sqfeet = float(Price_per_sqfeet) if Price_per_sqfeet else 0.0
    features = np.array([[Bedrooms,Bathrooms,Sqft_living,Floors,Price_per_sqfeet,Sqft_lot]])
    results = model.predict(features).reshape(1,-1)
    st.write("Predicted Price::::",results[0])