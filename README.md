# Employee Attrition Prediction
A Machine Learning project that predicts the likelihood of an employee leaving an organization based on employee, job, salary, experience, and satisfaction-related information.

## i have uploaded the url for reference

👉 **[Open Employee Attrition Predictor](https://employeeattritionpredict.streamlit.app/)**

## 📌 Project Overview
Employee attrition is an important challenge for organizations because losing employees can increase recruitment and training costs.
This project uses Machine Learning to predict whether an employee is likely to leave the organization. The application provides an interactive Streamlit interface where users can enter employee details and receive an attrition prediction along with the estimated probability.

## 🎯 Objectives
- Predict whether an employee is likely to leave the organization.
- Analyze employee-related factors associated with attrition.
- Apply data preprocessing and Machine Learning techniques.
- Build an interactive prediction application using Streamlit.
- Deploy the application so it can be accessed through a web browser.

## 📊 Dataset
The project uses the IBM HR Analytics Employee Attrition dataset.
The dataset contains employee information related to:
- Age
- Business Travel
- Department
- Education
- Education Field
- Job Role
- Job Satisfaction
- Monthly Income
- Overtime
- Performance Rating
- Relationship Satisfaction
- Work-Life Balance
- Years at Company
- Total Working Years
- And other employee-related attributes

## ⚙️ Machine Learning Workflow

The project follows these steps:

1. Data Collection
2. Data Preprocessing
3. Categorical Encoding
4. Class Balancing using Random Oversampling
5. Feature Scaling using StandardScaler
6. Model Training
7. Model Prediction
8. Streamlit Application Development
9. Deployment

## 🤖 Machine Learning Model

The project uses:

**Logistic Regression**

The model is trained on the preprocessed and balanced dataset and produces:

- Attrition prediction
- Attrition probability

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Imbalanced-learn
- Logistic Regression
- RandomOverSampler
- StandardScaler
- Streamlit
- GitHub
- Streamlit Community Cloud

## 🖥️ Application

The Streamlit application allows users to enter employee information including:

- Personal information
- Job information
- Experience
- Salary information
- Job satisfaction
- Work environment
- Education
- Overtime
- Career-related information

After entering the information, the user can click **Predict Attrition** to receive the prediction.

### Prediction Output

The application provides:

- 🟢 Low Attrition Risk
- 🔴 High Attrition Risk
- 📊 Estimated Attrition Probability

## 📁 Project Structure

```text
employee-attrition-prediction/
│
├── app.py
├── model.pkl
├── encoders.pkl
├── scaler.pkl
├── feature_order.pkl
├── requirements.txt
└── README.md
