import streamlit as st 
import pandas as pd
import pickle

st.title("Diamond Price Prediction")

carat=st.number_input("Enter the carat")
cut=st.radio("Pick Your cut",['Premium', 'Very Good', 'Ideal', 'Good', 'Fair'])
clarity=st.radio("Select the clarity",['VS2', 'SI2', 'VS1', 'SI1', 'IF', 'VVS2', 'VVS1', 'I1'])
color=st.radio('Select the color',['F', 'J', 'G', 'E', 'D', 'H', 'I'])
depth=st.number_input("Enter the Depth")
table=st.number_input("Enter the table")
x=st.number_input("Enter the x")
y=st.number_input("Enter y")
z=st.number_input("Enter z")
submit=st.button("Submit")

with open('model.pkl', 'rb') as file:  
    model = pickle.load(file)

if submit==True:
    if cut=='Premium':
        cut=4
    if cut=='Very Good':
        cut=3
    if cut=='Good':
        cut=2
    if cut=='Ideal':
        cut=5
    if cut=='Fair':
        cut=1
    
    if clarity=='I1':
        clarity=1
    if clarity=='SI2':
        clarity=2
    if clarity=='SI1':
        clarity=3
    if clarity=='VS1':
        clarity=4
    if clarity=='VS2':
        clarity=5
    if clarity=='VVS1':
        clarity=6
    if clarity=='VVS2':
        clarity=7
    if clarity=='IF':
        clarity=8
    
    if color=='D':
        color=1
    if color=='E':
        color=2
    if color=='F':
        color=3
    if color=='G':
        color=4
    if color=='H':
        color=5
    if color=='I':
        color=6
    if color=='J':
        color=7
    
    prediction_data=pd.DataFrame({
        'carat':[carat],
        'cut':[cut],
        'color':[color],
        'clarity':[clarity],
        'depth':[depth],
        'table':[table],
        'x':[x],
        'y':[y],
        'z':[z]
    })
    
    prediction=model.predict(prediction_data)

    st.text_area('Result',prediction)
