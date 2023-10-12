
import pickle
import pandas as pd
import streamlit as st
import sklearn

# Load the trained model
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# Load trained feature names from the pickle file
with open('trained_feature_names.pkl', 'rb') as feature_names_file:
    loaded_feature_names = pickle.load(feature_names_file)



st.title('Salary Prediction Web App')

# Provide instructions and example job titles to the user
st.write("Enter your details below and click 'Predict Salary' to get your predicted salary.")


# Collect input data from the user
input_age = st.number_input('Age', min_value=22, max_value=60)
input_gender = st.radio('Gender', ['Male', 'Female'])
input_education_level = st.selectbox('Education Level', ["Bachelor's", "Master's", 'PhD'])
#input_job_title = st.text_input('Job Title')
#input_job_title = st.selectbox('Select Job Title', loaded_feature_names[7:-1])
job_titles = [title.replace('Job Title_', '') for title in loaded_feature_names[7:-1]]
input_job_title = st.selectbox('Select Job Title', job_titles)
input_years_of_experience = st.number_input('Years of Experience', min_value=0, max_value=10, value=0)



if st.button('Predict Salary'):
    # Preprocess the input data
    input_dict = pd.DataFrame({
    'Age': [input_age],
    'Gender_Male': [1 if input_gender == 'Male' else 0],
    'Gender_Female': [1 if input_gender == 'Female' else 0],
    'Education Level_Bachelor\'s': [1 if input_education_level == "Bachelor's" else 0],
    'Education Level_Master\'s': [1 if input_education_level == "Master's" else 0],
    'Education Level_PhD': [1 if input_education_level == "PhD" else 0],
    # for Job titles
    'Job Title_Software Engineer': [1 if input_job_title == 'Software Engineer' else 0],
    'Job Title_Accountant': [1 if input_job_title == 'Accountant' else 0],
    'Job Title_Administrative Assistant': [1 if input_job_title == 'Administrative Assistant' else 0],
    'Job Title_Business Analyst': [1 if input_job_title == 'Business Analyst' else 0],
    'Job Title_Business Development Manager': [1 if input_job_title == 'Business Development Manager' else 0],
    'Job Title_Business Intelligence Analyst': [1 if input_job_title == 'Business Intelligence Analyst' else 0],
    'Job Title_CEO': [1 if input_job_title == 'CEO' else 0],
    'Job Title_Chief Data Officer': [1 if input_job_title == 'Chief Data Officer' else 0],
    'Job Title_Chief Technology Officer': [1 if input_job_title == 'Chief Technology Officer' else 0],
    'Job Title_Content Marketing Manager': [1 if input_job_title == 'Content Marketing Manager' else 0],
    'Job Title_Copywriter': [1 if input_job_title == 'Copywriter' else 0],
    'Job Title_Creative Director': [1 if input_job_title == 'Creative Director' else 0],
    'Job Title_Customer Service Manager': [1 if input_job_title == 'Customer Service Manager' else 0],
    'Job Title_Customer Service Rep': [1 if input_job_title == 'Customer Service Rep' else 0],
    'Job Title_Customer Service Representative': [1 if input_job_title == 'Customer Service Representative' else 0],
    'Job Title_Customer Success Manager': [1 if input_job_title == 'Customer Success Manager' else 0],
    'Job Title_Customer Success Rep': [1 if input_job_title == 'Customer Success Rep' else 0],
    'Job Title_Data Analyst': [1 if input_job_title == 'Data Analyst' else 0],
    'Job Title_Data Entry Clerk': [1 if input_job_title == 'Data Entry Clerk' else 0],
    'Job Title_Data Scientist': [1 if input_job_title == 'Data Scientist' else 0],
    'Job Title_Digital Content Producer': [1 if input_job_title == 'Digital Content Producer' else 0],
    'Job Title_Digital Marketing Manager': [1 if input_job_title == 'Digital Marketing Manager' else 0],
    'Job Title_Director': [1 if input_job_title == 'Director' else 0],
    'Job Title_Director of Business Development': [1 if input_job_title == 'Director of Business Development' else 0],
    'Job Title_Director of Engineering': [1 if input_job_title == 'Director of Engineering' else 0],
    'Job Title_Director of Finance': [1 if input_job_title == 'Director of Finance' else 0],
    'Job Title_Director of HR': [1 if input_job_title == 'Director of HR' else 0],
    'Job Title_Director of Human Capital': [1 if input_job_title == 'Director of Human Capital' else 0],
    'Job Title_Director of Human Resources': [1 if input_job_title == 'Director of Human Resources' else 0],
    'Job Title_Director of Marketing': [1 if input_job_title == 'Director of Marketing' else 0],
    'Job Title_Director of Operations': [1 if input_job_title == 'Director of Operations' else 0],
    'Job Title_Director of Product Management': [1 if input_job_title == 'Director of Product Management' else 0],
    'Job Title_Director of Sales': [1 if input_job_title == 'Director of Sales' else 0],
    'Job Title_Director of Sales and Marketing': [1 if input_job_title == 'Director of Sales and Marketing' else 0],
    'Job Title_Event Coordinator': [1 if input_job_title == 'Event Coordinator' else 0],
    'Job Title_Financial Advisor': [1 if input_job_title == 'Financial Advisor' else 0],
    'Job Title_Financial Analyst': [1 if input_job_title == 'Financial Analyst' else 0],
    'Job Title_Financial Manager': [1 if input_job_title == 'Financial Manager' else 0],
    'Job Title_Graphic Designer': [1 if input_job_title == 'Graphic Designer' else 0],
    'Job Title_HR Generalist': [1 if input_job_title == 'HR Generalist' else 0],
    'Job Title_HR Manager': [1 if input_job_title == 'HR Manager' else 0],
    'Job Title_Help Desk Analyst': [1 if input_job_title == 'Help Desk Analyst' else 0],
    'Job Title_Human Resources Director': [1 if input_job_title == 'Human Resources Director' else 0],
    'Job Title_IT Manager': [1 if input_job_title == 'IT Manager' else 0],
    'Job Title_IT Support': [1 if input_job_title == 'IT Support' else 0],
    'Job Title_IT Support Specialist': [1 if input_job_title == 'IT Support Specialist' else 0],
    'Job Title_Junior Account Manager': [1 if input_job_title == 'Junior Account Manager' else 0],
    'Job Title_Junior Accountant': [1 if input_job_title == 'Junior Accountant' else 0],
    'Job Title_Junior Advertising Coordinator': [1 if input_job_title == 'Junior Advertising Coordinator' else 0],
    'Job Title_Junior Business Analyst': [1 if input_job_title == 'Junior Business Analyst' else 0],
    'Job Title_Junior Business Development Associate': [1 if input_job_title == 'Junior Business Development Associate' else 0],
    'Job Title_Junior Business Operations Analyst': [1 if input_job_title == 'Junior Business Operations Analyst' else 0],
    'Job Title_Junior Copywriter': [1 if input_job_title == 'Junior Copywriter' else 0],
    'Job Title_Junior Customer Support Specialist': [1 if input_job_title == 'Junior Customer Support Specialist' else 0],
    'Job Title_Junior Data Analyst': [1 if input_job_title == 'Junior Data Analyst' else 0],
    'Job Title_Junior Data Scientist': [1 if input_job_title == 'Junior Data Scientist' else 0],
    'Job Title_Junior Designer': [1 if input_job_title == 'Junior Designer' else 0],
    'Job Title_Junior Developer': [1 if input_job_title == 'Junior Developer' else 0],
    'Job Title_Junior Financial Advisor': [1 if input_job_title == 'Junior Financial Advisor' else 0],
    'Job Title_Junior Financial Analyst': [1 if input_job_title == 'Junior Financial Analyst' else 0],
    'Job Title_Junior HR Coordinator': [1 if input_job_title == 'Junior HR Coordinator' else 0],
    'Job Title_Junior HR Generalist': [1 if input_job_title == 'Junior HR Generalist' else 0],
    'Job Title_Junior Marketing Analyst': [1 if input_job_title == 'Junior Marketing Analyst' else 0],
    'Job Title_Junior Marketing Coordinator': [1 if input_job_title == 'Junior Marketing Coordinator' else 0],
    'Job Title_Junior Marketing Manager': [1 if input_job_title == 'Junior Marketing Manager' else 0],
    'Job Title_Junior Marketing Specialist': [1 if input_job_title == 'Junior Marketing Specialist' else 0],
    'Job Title_Junior Operations Analyst': [1 if input_job_title == 'Junior Operations Analyst' else 0],
    'Job Title_Junior Operations Coordinator': [1 if input_job_title == 'Junior Operations Coordinator' else 0],
    'Job Title_Junior Operations Manager': [1 if input_job_title == 'Junior Operations Manager' else 0],
    'Job Title_Junior Product Manager': [1 if input_job_title == 'Junior Product Manager' else 0],
    'Job Title_Junior Project Manager': [1 if input_job_title == 'Junior Project Manager' else 0],
    'Job Title_Junior Recruiter': [1 if input_job_title == 'Junior Recruiter' else 0],
    'Job Title_Junior Research Scientist': [1 if input_job_title == 'Junior Research Scientist' else 0],
    'Job Title_Junior Sales Representative': [1 if input_job_title == 'Junior Sales Representative' else 0],
    'Job Title_Junior Social Media Manager': [1 if input_job_title == 'Junior Social Media Manager' else 0],
    'Job Title_Junior Social Media Specialist': [1 if input_job_title == 'Junior Social Media Specialist' else 0],
    'Job Title_Junior Software Developer': [1 if input_job_title == 'Junior Software Developer' else 0],
    'Job Title_Junior Software Engineer': [1 if input_job_title == 'Junior Software Engineer' else 0],
    'Job Title_Junior UX Designer': [1 if input_job_title == 'Junior UX Designer' else 0],
    'Job Title_Junior Web Designer': [1 if input_job_title == 'Junior Web Designer' else 0],
    'Job Title_Junior Web Developer': [1 if input_job_title == 'Junior Web Developer' else 0],
    'Job Title_Marketing Analyst': [1 if input_job_title == 'Marketing Analyst' else 0],
    'Job Title_Marketing Coordinator': [1 if input_job_title == 'Marketing Coordinator' else 0],
    'Job Title_Marketing Manager': [1 if input_job_title == 'Marketing Manager' else 0],
    'Job Title_Marketing Specialist': [1 if input_job_title == 'Marketing Specialist' else 0],
    'Job Title_Network Engineer': [1 if input_job_title == 'Network Engineer' else 0],
    'Job Title_Office Manager': [1 if input_job_title == 'Office Manager' else 0],
    'Job Title_Operations Analyst': [1 if input_job_title == 'Operations Analyst' else 0],
    'Job Title_Operations Director': [1 if input_job_title == 'Operations Director' else 0],
    'Job Title_Operations Manager': [1 if input_job_title == 'Operations Manager' else 0],
    'Job Title_Principal Engineer': [1 if input_job_title == 'Principal Engineer' else 0],
    'Job Title_Principal Scientist': [1 if input_job_title == 'Principal Scientist' else 0],
    'Job Title_Product Designer': [1 if input_job_title == 'Product Designer' else 0],
    'Job Title_Product Manager': [1 if input_job_title == 'Product Manager' else 0],
    'Job Title_Product Marketing Manager': [1 if input_job_title == 'Product Marketing Manager' else 0],
    'Job Title_Project Engineer': [1 if input_job_title == 'Project Engineer' else 0],
    'Job Title_Project Manager': [1 if input_job_title == 'Project Manager' else 0],
    'Job Title_Public Relations Manager': [1 if input_job_title == 'Public Relations Manager' else 0],
    'Job Title_Recruiter': [1 if input_job_title == 'Recruiter' else 0],
    'Job Title_Research Director': [1 if input_job_title == 'Research Director' else 0],
    'Job Title_Research Scientist': [1 if input_job_title == 'Research Scientist' else 0],
    'Job Title_Sales Associate': [1 if input_job_title == 'Sales Associate' else 0],
    'Job Title_Sales Director': [1 if input_job_title == 'Sales Director' else 0],
    'Job Title_Sales Executive': [1 if input_job_title == 'Sales Executive' else 0],
    'Job Title_Sales Manager': [1 if input_job_title == 'Sales Manager' else 0],
    'Job Title_Sales Operations Manager': [1 if input_job_title == 'Sales Operations Manager' else 0],
    'Job Title_Sales Representative': [1 if input_job_title == 'Sales Representative' else 0],
    'Job Title_Senior Account Executive': [1 if input_job_title == 'Senior Account Executive' else 0],
    'Job Title_Senior Account Manager': [1 if input_job_title == 'Senior Account Manager' else 0],
    'Job Title_Senior Accountant': [1 if input_job_title == 'Senior Accountant' else 0],
    'Job Title_Senior Business Analyst': [1 if input_job_title == 'Senior Business Analyst' else 0],
    'Job Title_Senior Business Development Manager': [1 if input_job_title == 'Senior Business Development Manager' else 0],
    'Job Title_Senior Consultant': [1 if input_job_title == 'Senior Consultant' else 0],
    'Job Title_Senior Data Analyst': [1 if input_job_title == 'Senior Data Analyst' else 0],
    'Job Title_Senior Data Engineer': [1 if input_job_title == 'Senior Data Engineer' else 0],
    'Job Title_Senior Data Scientist': [1 if input_job_title == 'Senior Data Scientist' else 0],
    'Job Title_Senior Engineer': [1 if input_job_title == 'Senior Engineer' else 0],
    'Job Title_Senior Financial Advisor': [1 if input_job_title == 'Senior Financial Advisor' else 0],
    'Job Title_Senior Financial Analyst': [1 if input_job_title == 'Senior Financial Analyst' else 0],
    'Job Title_Senior Financial Manager': [1 if input_job_title == 'Senior Financial Manager' else 0],
    'Job Title_Senior Graphic Designer': [1 if input_job_title == 'Senior Graphic Designer' else 0],
    'Job Title_Senior HR Generalist': [1 if input_job_title == 'Senior HR Generalist' else 0],
    'Job Title_Senior HR Manager': [1 if input_job_title == 'Senior HR Manager' else 0],
    'Job Title_Senior HR Specialist': [1 if input_job_title == 'Senior HR Specialist' else 0],
    'Job Title_Senior Human Resources Coordinator': [1 if input_job_title == 'Senior Human Resources Coordinator' else 0],
    'Job Title_Senior Human Resources Manager': [1 if input_job_title == 'Senior Human Resources Manager' else 0],
    'Job Title_Senior Human Resources Specialist': [1 if input_job_title == 'Senior Human Resources Specialist' else 0],
    'Job Title_Senior IT Consultant': [1 if input_job_title == 'Senior IT Consultant' else 0],
    'Job Title_Senior IT Project Manager': [1 if input_job_title == 'Senior IT Project Manager' else 0],
    'Job Title_Senior IT Support Specialist': [1 if input_job_title == 'Senior IT Support Specialist' else 0],
    'Job Title_Senior Marketing Analyst': [1 if input_job_title == 'Senior Marketing Analyst' else 0],
    'Job Title_Senior Manager': [1 if input_job_title == 'Senior Manager' else 0],
    'Job Title_Senior Marketing Coordinator': [1 if input_job_title == 'Senior Marketing Coordinator' else 0],
    'Job Title_Senior Marketing Director': [1 if input_job_title == 'Senior Marketing Director' else 0],
    'Job Title_Senior Marketing Manager': [1 if input_job_title == 'Senior Marketing Manager' else 0],
    'Job Title_Senior Marketing Specialist': [1 if input_job_title == 'Senior Marketing Specialist' else 0],
    'Job Title_Senior Operations Analyst': [1 if input_job_title == 'Senior Operations Analyst' else 0],
    'Job Title_Senior Operations Coordinator': [1 if input_job_title == 'Senior Operations Coordinator' else 0],
    'Job Title_Senior Operations Manager': [1 if input_job_title == 'Senior Operations Manager' else 0],
    'Job Title_Senior Product Designer': [1 if input_job_title == 'Senior Product Designer' else 0],
    'Job Title_Senior Product Development Manager': [1 if input_job_title == 'Senior Product Development Manager' else 0],
    'Job Title_Senior Product Manager': [1 if input_job_title == 'Senior Product Manager' else 0],
    'Job Title_Senior Product Marketing Manager': [1 if input_job_title == 'Senior Product Marketing Manager' else 0],
    'Job Title_Senior Project Coordinator': [1 if input_job_title == 'Senior Project Coordinator' else 0],
    'Job Title_Senior Project Manager': [1 if input_job_title == 'Senior Project Manager' else 0],
    'Job Title_Senior Quality Assurance Analyst': [1 if input_job_title == 'Senior Quality Assurance Analyst' else 0],
    'Job Title_Senior Research Scientist': [1 if input_job_title == 'Senior Research Scientist' else 0],
    'Job Title_Senior Researcher': [1 if input_job_title == 'Senior Researcher' else 0],
    'Job Title_Senior Sales Manager': [1 if input_job_title == 'Senior Sales Manager' else 0],
    'Job Title_Senior Sales Representative': [1 if input_job_title == 'Senior Sales Representative' else 0],
    'Job Title_Senior Scientist': [1 if input_job_title == 'Senior Scientist' else 0],
    'Job Title_Senior Software Architect': [1 if input_job_title == 'Senior Software Architect' else 0],
    'Job Title_Senior Software Developer': [1 if input_job_title == 'Senior Software Developer' else 0],
    'Job Title_Senior Software Engineer': [1 if input_job_title == 'Senior Software Engineer' else 0],
    'Job Title_Senior Training Specialist': [1 if input_job_title == 'Senior Training Specialist' else 0],
    'Job Title_Senior UX Designer': [1 if input_job_title == 'Senior UX Designer' else 0],
    'Job Title_Social Media Manager': [1 if input_job_title == 'Social Media Manager' else 0],
    'Job Title_Social Media Specialist': [1 if input_job_title == 'Social Media Specialist' else 0],
    'Job Title_Software Developer': [1 if input_job_title == 'Software Developer' else 0],
    'Job Title_Software Manager': [1 if input_job_title == 'Software Manager' else 0],
    'Job Title_Software Project Manager': [1 if input_job_title == 'Software Project Manager' else 0],
    'Job Title_Strategy Consultant': [1 if input_job_title == 'Strategy Consultant' else 0],
    'Job Title_Supply Chain Analyst': [1 if input_job_title == 'Supply Chain Analyst' else 0],
    'Job Title_Supply Chain Manager': [1 if input_job_title == 'Supply Chain Manager' else 0],
    'Job Title_Technical Recruiter': [1 if input_job_title == 'Technical Recruiter' else 0],
    'Job Title_Technical Support Specialist': [1 if input_job_title == 'Technical Support Specialist' else 0],
    'Job Title_Technical Writer': [1 if input_job_title == 'Technical Writer' else 0],
    'Job Title_Training Specialist': [1 if input_job_title == 'Training Specialist' else 0],
    'Job Title_UX Designer': [1 if input_job_title == 'UX Designer' else 0],
    'Job Title_UX Researcher': [1 if input_job_title == 'UX Researcher' else 0],
    'Job Title_VP of Finance': [1 if input_job_title == 'VP of Finance' else 0],
    'Job Title_VP of Operations': [1 if input_job_title == 'VP of Operations' else 0],
    'Job Title_Web Developer': [1 if input_job_title == 'Web Developer' else 0],
    'Years of Experience': [input_years_of_experience]
})

    for job_title in loaded_feature_names[7:-1]:  # Skip the first 7 columns and the last column (Years of Experience)
        input_dict[job_title] = [1 if job_title == f'Job Title_{input_job_title}' else 0]

    # Create a DataFrame from the input_dict
    input_data = pd.DataFrame.from_dict(input_dict)

    # Ensure all columns in the input data match the columns used during training
    missing_columns = set(loaded_feature_names) - set(input_data.columns)
    for column in missing_columns:
        input_data[column] = 0

    # Reorder columns to match the order used during training
    input_data = input_data[loaded_feature_names]

    # Make predictions for the input data
    predicted_salary = loaded_model.predict(input_data)

    st.write(f'Predicted Salary: {predicted_salary[0]:,.2f}')

# Add a section for model description
st.subheader('About This Model')
st.write("This salary prediction model is trained to estimate salaries based on various factors such as age, gender, education level, job title, and years of experience. It uses a machine learning algorithm to provide predictions.")
