import pickle 
import streamlit as st

# membaca model
depression_model = pickle.load(open('depression_model.sav', 'rb'))

# Judul Web
st.title('Prediksi Depresi')

Gender = st.text_input('Gender (male = 1 and female = 2)')

Age = st.text_input('Age')

AcademicPressure = st.text_input('Academic Pressure (1(low) to 5(high))')

StudySatisfaction = st.text_input('Study Satification (1(low) to 5(high))')

SleepDuration = st.text_input('Sleep Duration')

DietaryHabits = st.text_input('Dietary Habits (unhealthy = 2, moderate = 1, and healthy = 0)')

SuicidalThoughts = st.text_input('Have you ever had suicidal thoughts? (yes = 1 and no = 0)')

StudyHours = st.text_input('Study Hours')

FinancialStress = st.text_input('Financial Stress (1(low) to 5(high))')

FamilyHistoryofMentalIllness = st.text_input('Is there family history of depression? (yes = 1 and no = 0)')

# code untuk prediksi 
depression_diagnosis = ''

# membuat tombol untuk prediksi
if st.button('Test Prediksi Depresi'):
    depression_prediction = depression_model.predict([[Gender, Age, AcademicPressure, StudySatisfaction, SleepDuration, DietaryHabits, SuicidalThoughts, StudyHours, FinancialStress, FamilyHistoryofMentalIllness]])

    if (depression_prediction[0] == 1):
        depression_diagnosis = 'Pasien mengalami depresi'
    else :
        depression_diagnosis = 'Pasien tidak mengalami depresi'
    st.success(depression_diagnosis)
