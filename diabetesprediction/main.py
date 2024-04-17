import numpy as np
import pickle
import streamlit as st

# loading the saved model
loaded_model = pickle.load(open('/home/isha/Documents/PythonProject2024/diabetesprediction/diabetes_model.sav', 'rb'))


# creating a function for prediction

def diabetes_prediction(input_data):
    
    # changing the input data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'the person is not diabetic'
    else:
        return 'the person is diabetic'
    
def main():
    st.title('Diabetes Prediction App')
    
    Pregnancies = st.text_input('Number of Pregnancies')
    Glucose = st.text_input('Glucose Level')
    BloodPressure = st.text_input('Blood Pressure')
    SkinThickness = st.text_input('Skin Thickness')
    Insulin = st.text_input('Insulin')
    BMI = st.text_input('BMI')
    DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function')
    Age = st.text_input('Age')
    
    # the code for prediction 
    diagnosis = ''
    
    # creating a button for prediction
    if st.button('Predict'):
        diagnosis = diabetes_prediction([Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age])
        
    st.success(diagnosis)
    
if __name__ == '__main__':
    main()
    
    