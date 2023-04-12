# General Libraries
import pickle
import pandas as pd

# Model deployment
import streamlit as st

# Load the trained model
model = pickle.load(open('ETC_NM.pkl', 'rb'))

# Add an empty space for centering the button
st.image('Title.png')

# Set up input fields for user to enter features
high_bp_mapping = {'Yes': 1, 'No': 0}
high_bp = st.selectbox("High Blood Pressure", ['Yes', 'No'])
high_bp_num = high_bp_mapping[high_bp]
high_chol_mapping = {'Yes': 1, 'No': 0}
high_chol = st.selectbox("High Cholesterol", ['Yes', 'No'])
high_chol_num = high_chol_mapping[high_chol]
chol_check_mapping = {'Yes': 1, 'No': 0}
chol_check = st.selectbox("Cholesterol Checked", ['Yes', 'No'])
chol_check_num = chol_check_mapping[chol_check]
smoker_mapping = {'Yes': 1, 'No': 0}
smoker = st.selectbox("Smoker", ['Yes', 'No'])
smoker_num = smoker_mapping[smoker]
stroke_mapping = {'Yes': 1, 'No': 0}
stroke = st.selectbox("History of Stroke", ['Yes', 'No'])
stroke_num = stroke_mapping[stroke]
heart_disease_mapping = {'Yes': 1, 'No': 0}
heart_disease = st.selectbox("History of Heart Disease or Heart Attack", ['Yes', 'No'])
heart_disease_num = heart_disease_mapping[heart_disease]
phys_activity_mapping = {'Yes': 1, 'No': 0}
phys_activity = st.selectbox("Physically Active", ['Yes', 'No'])
phys_activity_num = phys_activity_mapping[phys_activity]
gen_hlth_mapping = {'Excellent': 1, 'Very Good': 2, 'Good': 3, 'Fair': 4, 'Poor': 5}
gen_hlth = st.selectbox("General Health", ['Excellent', 'Very Good', 'Good', 'Fair', 'Poor'])
gen_hlth_num = gen_hlth_mapping[gen_hlth]
diff_walk_mapping = {'None': 0, 'Yes': 1}
diff_walk = st.selectbox("Difficulty in Walking", ['None', 'Yes'])
diff_walk_num = diff_walk_mapping[diff_walk]
age_mapping = {'18-24': 1, '25-29': 2, '30-34': 3, '35-39': 4, '40-44': 5, '45-49': 6, '50-54': 7, '55-59': 8, '60-64': 9, '65-69': 10, '70-74': 11, '75-79': 12, '80 and older': 13}
age = st.selectbox("Age (years)", ['18-24', '25-29', '30-34', '35-39', '40-44', '45-49', '50-54', '55-59', '60-64', '65-69', '70-74', '75-79', '80 and older'])
age_num = age_mapping[age]
educ_mapping = {'Never Attended': 1, 'Elementary': 2, 'High School Undergrad': 3, 'High School Graduate': 4, 'College Undergrad': 5, 'College Graduate': 6 }
education = st.selectbox("Education", ['Never Attended', 'Elementary', 'High School Undergrad', 'High School Graduate', 'College Undergrad', 'College Graduate'])
educ_num = educ_mapping[education]
income_mapping = {'<10000 USD': 1, '10000 to 15000 USD': 2, '15000 to 20000 USD': 3, '20000 to 25000 USD': 4, '25000 to 35000 USD': 5, '35000 to 50000 USD': 6, '50000 to 75000 USD': 7, '>75000 USD': 8}
income = st.selectbox("Income", ['<10000 USD', '10000 to 15000 USD', '15000 to 20000 USD', '20000 to 25000 USD', '25000 to 35000 USD', '35000 to 50000 USD', '50000 to 75000 USD', '>75000 USD'])
income_num = income_mapping[income]

bmi_mapping = {'Underweight': 1, 'Normal Weight': 2, 'Overweight': 3, 'Obese': 4}
bmi_bins = st.selectbox("BMI", ['Underweight', 'Normal Weight', 'Overweight', 'Obese'])
bmi_bins_num = bmi_mapping[bmi_bins]

# Create a dataframe with user input features
# Create a DataFrame with input fields as columns
df = pd.DataFrame({
    'HighBP_0.0': [1 if high_bp_mapping[high_bp] == 0 else 0],
    'HighBP_1.0': [1 if high_bp_mapping[high_bp] == 1 else 0],
    'HighChol_0.0': [1 if high_chol_mapping[high_chol] == 0 else 0],
    'HighChol_1.0': [1 if high_chol_mapping[high_chol] == 1 else 0],
    'CholCheck_0.0': [1 if chol_check_mapping[chol_check] == 0 else 0],
    'CholCheck_1.0': [1 if chol_check_mapping[chol_check] == 1 else 0],
    'Smoker_0.0': [1 if smoker_mapping[smoker] == 0 else 0],
    'Smoker_1.0': [1 if smoker_mapping[smoker] == 1 else 0],
    'Stroke_0.0': [1 if stroke_mapping[stroke] == 0 else 0],
    'Stroke_1.0': [1 if stroke_mapping[stroke] == 1 else 0],
    'HeartDisease_0.0': [1 if heart_disease_mapping[heart_disease] == 0 else 0],
    'HeartDisease_1.0': [1 if heart_disease_mapping[heart_disease] == 1 else 0],
    'PhysActivity_0.0': [1 if phys_activity_mapping[phys_activity] == 0 else 0],
    'PhysActivity_1.0': [1 if phys_activity_mapping[phys_activity] == 1 else 0],
    'GenHlth_1.0': [1 if gen_hlth_mapping[gen_hlth] == 1 else 0],
    'GenHlth_2.0': [1 if gen_hlth_mapping[gen_hlth] == 2 else 0],
    'GenHlth_3.0': [1 if gen_hlth_mapping[gen_hlth] == 3 else 0],
    'GenHlth_4.0': [1 if gen_hlth_mapping[gen_hlth] == 4 else 0],
    'GenHlth_5.0': [1 if gen_hlth_mapping[gen_hlth] == 5 else 0],
    'DiffWalk_0.0': [1 if diff_walk_mapping[diff_walk] == 0 else 0],
    'DiffWalk_1.0': [1 if diff_walk_mapping[diff_walk] == 1 else 0],
    'Age_1.0': [1 if age_mapping[age] == 1 else 0],
    'Age_2.0': [1 if age_mapping[age] == 2 else 0],
    'Age_3.0': [1 if age_mapping[age] == 3 else 0],
    'Age_4.0': [1 if age_mapping[age] == 4 else 0],
    'Age_5.0': [1 if age_mapping[age] == 5 else 0],
    'Age_6.0': [1 if age_mapping[age] == 6 else 0],
    'Age_7.0': [1 if age_mapping[age] == 7 else 0],
    'Age_8.0': [1 if age_mapping[age] == 8 else 0],
    'Age_9.0': [1 if age_mapping[age] == 9 else 0],
    'Age_10.0': [1 if age_mapping[age] == 10 else 0],
    'Age_11.0': [1 if age_mapping[age] == 11 else 0],
    'Age_12.0': [1 if age_mapping[age] == 12 else 0],
    'Age_13.0': [1 if age_mapping[age] == 13 else 0],
    'Education_1.0': [1 if educ_mapping[education] == 1 else 0],
    'Education_2.0': [1 if educ_mapping[education] == 2 else 0],
    'Education_3.0': [1 if educ_mapping[education] == 3 else 0],
    'Education_4.0': [1 if educ_mapping[education] == 4 else 0],
    'Education_5.0': [1 if educ_mapping[education] == 5 else 0],
    'Education_6.0': [1 if educ_mapping[education] == 6 else 0],
    'Income_1.0': [1 if income_mapping[income] == 1 else 0],
    'Income_2.0': [1 if income_mapping[income] == 2 else 0],
    'Income_3.0': [1 if income_mapping[income] == 3 else 0],
    'Income_4.0': [1 if income_mapping[income] == 4 else 0],
    'Income_5.0': [1 if income_mapping[income] == 5 else 0],
    'Income_6.0': [1 if income_mapping[income] == 6 else 0],
    'Income_7.0': [1 if income_mapping[income] == 7 else 0],
    'Income_8.0': [1 if income_mapping[income] == 8 else 0],
    'BMI_bins_1.0': [1 if bmi_mapping[bmi_bins] == 1 else 0],
    'BMI_bins_2.0': [1 if bmi_mapping[bmi_bins] == 2 else 0],
    'BMI_bins_3.0': [1 if bmi_mapping[bmi_bins] == 3 else 0],
    'BMI_bins_4.0': [1 if bmi_mapping[bmi_bins] == 4 else 0]})



# Center the button using CSS
st.markdown("""
    <style>
    .centered {
        display: flex;
        justify-content: center;
    }
    </style>
""", unsafe_allow_html=True)

# Create a button to run the model
if st.button('Run MODEL'):
    # Make prediction using the trained model
    prediction_num = model.predict(df)[0]
    pred_map = {1: 'Diabetic Risk', 0: 'Non-Diabetic'}
    prediction = pred_map[prediction_num]

    # Display the prediction
    st.subheader(prediction)
    

    # Load and display image based on prediction
    if prediction == 'Diabetic Risk':
        st.image('sugar-blood-level.png', width=200)
        st.write('High Risk: Please consult your healthcare provider for further evaluation and management.')
        st.markdown('<p style="font-size: 12px;">All content and media on the Project Dia-BEAT-this app is created and published online for informational purposes only. It is not intended to be a substitute for professional medical advice and should not be relied on as health or personal advice.</p>', unsafe_allow_html=True)
    elif prediction == 'Non-Diabetic':
        st.image('healthy.png', width=200)
        st.write('Low Risk: No immediate concern, but it is always good to maintain a healthy lifestyle and regular check-ups.')
        st.markdown('<p style="font-size: 12px;">All content and media on the Project Dia-BEAT-this app is created and published online for informational purposes only. It is not intended to be a substitute for professional medical advice and should not be relied on as health or personal advice.</p>', unsafe_allow_html=True)







