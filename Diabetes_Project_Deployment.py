import pickle
import streamlit as st
import pandas as pd

data = pickle.load(open('C:\\Users\\sarao\\Downloads\\Diabetes_prediction.sav', 'rb'))

st.title('Diabetes Prediction Web App')
st.info('Easy Application for Diabetes Prediction Disease')

st.sidebar.header('Feature Selection')

# ['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin',
#  'BMI', 'DiabetesPedigreeFunction', 'Age', 'Outcome']

Pregnancies = st.text_input('Pregnancies')
Glucose = st.text_input('Glucose')
BloodPressure = st.text_input('BloodPressure')
SkinThickness = st.text_input('SkinThickness')
Insulin = st.text_input('Insulin')
BMI = st.text_input('BMI')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
Age = st.text_input('Age')

df = pd.DataFrame({
    'Pregnancies': [Pregnancies],
    'Glucose': [Glucose],
    'BloodPressure': [BloodPressure],
    'SkinThickness': [SkinThickness],
    'Insulin': [Insulin],
    'BMI': [BMI],
    'DiabetesPedigreeFunction': [DiabetesPedigreeFunction],
    'Age': [Age]
}, index=[0])

con = st.sidebar.button('Confirm')

if con:
    df = df.apply(pd.to_numeric)
    
    result = data.predict(df)
    #st.sidebar.write(result)
    if result == 0:
        st.sidebar.write('The person is not infected')
        st.sidebar.image('https://regencyhealthcare.in/wp-content/uploads/2019/09/19_09_Sept.jpg',width=150)
    else:
        st.sidebar.write('The person has the disease')
        st.sidebar.image('https://wearemore.life/wp-content/uploads/2016/08/heart-4248636_1920.jpg',width=150)