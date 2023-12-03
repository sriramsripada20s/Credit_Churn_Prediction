import streamlit as st
import pandas as pd
import joblib
#from sklearn.preprocessing import StandardScaler

# Load the model and other necessary preprocessing objects
model = joblib.load('model.joblib')

st.title("Customer Churn Prediction")

# Create input fields for each variable
credit_score = st.text_input('Enter Credit Score (350-750)', 0.0)
gender = st.selectbox('Select Gender (1 for male 0 for female)', [0, 1])
age = st.text_input('Enter Age (18yrs-92yrs)', 0.0)
tenure = st.text_input('Enter Tenure (0 to 10)', 0.0)
balance = st.text_input('Enter Balance (0 to 260000)', 0.0)
num_of_products = st.text_input('Enter Number of Products (1 to 4)', 0.0)
has_cr_card = st.text_input('Has Credit Card? (1 for Yes, 0 for No)', 0.0)
is_active_member = st.text_input('Is Active Member? (1 for Yes, 0 for No)', 0.0)
estimated_salary = st.text_input('Enter Estimated Salary (11.5 to 199992)' , 0.0)
geography_germany = st.selectbox('Is from Germany? (1 for Yes, 0 for No)', [0, 1])
geography_spain = st.selectbox('Is from Spain? (1 for Yes, 0 for No)', [0, 1])

# Create a dictionary to hold the user input
user_data = {
    'CreditScore': float(credit_score),
    'Gender': int(gender),
    'Age': float(age),
    'Tenure': float(tenure),
    'Balance': float(balance),
    'NumOfProducts': float(num_of_products),
    'HasCrCard': float(has_cr_card),
    'IsActiveMember': float(is_active_member),
    'EstimatedSalary': float(estimated_salary),
    'Geography_Germany': int(geography_germany),
    'Geography_Spain': int(geography_spain)
}

# Convert the user input to a DataFrame
input_df = pd.DataFrame([user_data])

# Apply any necessary transformations
# For example, scaling the input data
#scaler = StandardScaler()
#input_df_scaled = scaler.fit_transform(input_df)

# Make predictions
prediction = model.predict(input_df)

if st.button("Predict Churn"):
    if prediction[0] == 0:
        st.header("Customer will not churn")
    else:
        st.header("Customer will churn")
