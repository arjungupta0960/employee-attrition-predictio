import streamlit as st
import pandas as pd
import pickle


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Employee Attrition Predictor",
    page_icon="👨‍💼",
    layout="wide"
)


# =========================================================
# LOAD MODEL FILES
# =========================================================

@st.cache_resource
def load_files():

    with open("model.pkl", "rb") as file:
        model = pickle.load(file)

    with open("encoders.pkl", "rb") as file:
        encoders = pickle.load(file)

    with open("scaler.pkl", "rb") as file:
        scaler = pickle.load(file)

    with open("feature_order.pkl", "rb") as file:
        feature_order = pickle.load(file)

    return model, encoders, scaler, feature_order


model, encoders, scaler, feature_order = load_files()


# =========================================================
# HEADER
# =========================================================

st.title("👨‍💼 Employee Attrition Prediction")

st.write(
    "Enter employee information to predict the likelihood "
    "of employee attrition."
)

st.divider()


# =========================================================
# EMPLOYEE INFORMATION
# =========================================================

st.header("👤 Employee Information")

col1, col2, col3 = st.columns(3)

with col1:
    age = st.number_input(
        "Age",
        min_value=18,
        max_value=60,
        value=30
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

with col3:
    marital_status = st.selectbox(
        "Marital Status",
        encoders["MaritalStatus"].classes_.tolist()
    )


# =========================================================
# JOB INFORMATION
# =========================================================

st.header("💼 Job Information")

col1, col2, col3 = st.columns(3)

with col1:
    department = st.selectbox(
        "Department",
        encoders["Department"].classes_.tolist()
    )

with col2:
    job_role = st.selectbox(
        "Job Role",
        encoders["JobRole"].classes_.tolist()
    )

with col3:
    business_travel = st.selectbox(
        "Business Travel",
        encoders["BusinessTravel"].classes_.tolist()
    )


col1, col2, col3 = st.columns(3)

with col1:
    job_level = st.slider(
        "Job Level",
        1,
        5,
        2
    )

with col2:
    job_involvement = st.slider(
        "Job Involvement",
        1,
        4,
        3
    )

with col3:
    job_satisfaction = st.slider(
        "Job Satisfaction",
        1,
        4,
        3
    )


# =========================================================
# EXPERIENCE
# =========================================================

st.header("📈 Experience & Career")

col1, col2, col3 = st.columns(3)

with col1:
    total_working_years = st.number_input(
        "Total Working Years",
        min_value=0,
        max_value=40,
        value=8
    )

with col2:
    years_at_company = st.number_input(
        "Years at Company",
        min_value=0,
        max_value=40,
        value=5
    )

with col3:
    years_current_role = st.number_input(
        "Years in Current Role",
        min_value=0,
        max_value=20,
        value=3
    )


col1, col2, col3 = st.columns(3)

with col1:
    years_since_promotion = st.number_input(
        "Years Since Last Promotion",
        min_value=0,
        max_value=20,
        value=2
    )

with col2:
    years_manager = st.number_input(
        "Years With Current Manager",
        min_value=0,
        max_value=20,
        value=3
    )

with col3:
    num_companies = st.number_input(
        "Number of Companies Worked",
        min_value=0,
        max_value=20,
        value=2
    )


# =========================================================
# SALARY & WORK
# =========================================================

st.header("💰 Salary & Work Information")

col1, col2, col3 = st.columns(3)

with col1:
    monthly_income = st.number_input(
        "Monthly Income",
        min_value=1000,
        max_value=20000,
        value=5000
    )

with col2:
    monthly_rate = st.number_input(
        "Monthly Rate",
        min_value=2000,
        max_value=30000,
        value=15000
    )

with col3:
    daily_rate = st.number_input(
        "Daily Rate",
        min_value=100,
        max_value=1500,
        value=700
    )


col1, col2, col3 = st.columns(3)

with col1:
    hourly_rate = st.number_input(
        "Hourly Rate",
        min_value=20,
        max_value=100,
        value=60
    )

with col2:
    salary_hike = st.slider(
        "Percent Salary Hike",
        10,
        25,
        15
    )

with col3:
    performance_rating = st.slider(
        "Performance Rating",
        1,
        4,
        3
    )


# =========================================================
# SATISFACTION
# =========================================================

st.header("😊 Satisfaction & Work Environment")

col1, col2, col3 = st.columns(3)

with col1:
    environment_satisfaction = st.slider(
        "Environment Satisfaction",
        1,
        4,
        3
    )

with col2:
    relationship_satisfaction = st.slider(
        "Relationship Satisfaction",
        1,
        4,
        3
    )

with col3:
    work_life_balance = st.slider(
        "Work Life Balance",
        1,
        4,
        3
    )


col1, col2, col3 = st.columns(3)

with col1:
    overtime = st.selectbox(
        "OverTime",
        ["No", "Yes"]
    )

with col2:
    stock_option = st.slider(
        "Stock Option Level",
        0,
        3,
        1
    )

with col3:
    training = st.slider(
        "Training Times Last Year",
        0,
        6,
        3
    )


# =========================================================
# EDUCATION
# =========================================================

st.header("🎓 Education")

col1, col2 = st.columns(2)

with col1:
    education = st.slider(
        "Education Level",
        1,
        5,
        3
    )

with col2:
    education_field = st.selectbox(
        "Education Field",
        encoders["EducationField"].classes_.tolist()
    )


# =========================================================
# OTHER INFORMATION
# =========================================================
# =========================================================
# OTHER INFORMATION
# =========================================================

st.header("⚙️ Other Information")

col1, col2 = st.columns(2)

with col1:
    distance_home = st.number_input(
        "Distance From Home",
        min_value=1,
        max_value=30,
        value=5
    )

with col2:
    employee_number = st.number_input(
        "Employee Number",
        min_value=1,
        max_value=2000,
        value=100
    )


# =========================================================
# PREDICTION BUTTON
# =========================================================

st.divider()

predict_button = st.button(
    "🔮 Predict Attrition",
    use_container_width=True
)


# =========================================================
# PREDICTION
# =========================================================

if predict_button:

    try:

        # -------------------------------------------------
        # Encode categorical columns
        # -------------------------------------------------

        business_travel_encoded = encoders[
            "BusinessTravel"
        ].transform([business_travel])[0]

        department_encoded = encoders[
            "Department"
        ].transform([department])[0]

        education_field_encoded = encoders[
            "EducationField"
        ].transform([education_field])[0]

        job_role_encoded = encoders[
            "JobRole"
        ].transform([job_role])[0]

        marital_status_encoded = encoders[
            "MaritalStatus"
        ].transform([marital_status])[0]


        # -------------------------------------------------
        # Binary encoding
        # -------------------------------------------------

        gender_encoded = (
            0 if gender == "Male" else 1
        )

        overtime_encoded = (
            0 if overtime == "No" else 1
        )


        # -------------------------------------------------
        # Create input
        # -------------------------------------------------

        input_data = pd.DataFrame({

    "Age": [age],

    "BusinessTravel": [
        business_travel_encoded
    ],

    "DailyRate": [
        daily_rate
    ],

    "Department": [
        department_encoded
    ],

    "DistanceFromHome": [
        distance_home
    ],

    "Education": [
        education
    ],

    "EducationField": [
        education_field_encoded
    ],

    "EmployeeCount": [
        1
    ],

    "EmployeeNumber": [
        employee_number
    ],

    "EnvironmentSatisfaction": [
        environment_satisfaction
    ],

    "Gender": [
        gender_encoded
    ],

    "HourlyRate": [
        hourly_rate
    ],

    "JobInvolvement": [
        job_involvement
    ],

    "JobLevel": [
        job_level
    ],

    "JobRole": [
        job_role_encoded
    ],

    "JobSatisfaction": [
        job_satisfaction
    ],

    "MaritalStatus": [
        marital_status_encoded
    ],

    "MonthlyIncome": [
        monthly_income
    ],

    "MonthlyRate": [
        monthly_rate
    ],

    "NumCompaniesWorked": [
        num_companies
    ],

    "OverTime": [
        overtime_encoded
    ],

    "PercentSalaryHike": [
        salary_hike
    ],

    "PerformanceRating": [
        performance_rating
    ],

    "RelationshipSatisfaction": [
        relationship_satisfaction
    ],

    "StandardHours": [
        80
    ],

    "StockOptionLevel": [
        stock_option
    ],

    "TotalWorkingYears": [
        total_working_years
    ],

    "TrainingTimesLastYear": [
        training
    ],

    "WorkLifeBalance": [
        work_life_balance
    ],

    "YearsAtCompany": [
        years_at_company
    ],

    "YearsInCurrentRole": [
        years_current_role
    ],

    "YearsSinceLastPromotion": [
        years_since_promotion
    ],

    "YearsWithCurrManager": [
        years_manager
    ],

    "count": [
        1
    ]
})


        # -------------------------------------------------
        # Arrange features in exact training order
        # -------------------------------------------------

        input_data = input_data[
            feature_order
        ]


        # -------------------------------------------------
        # Scale input
        # -------------------------------------------------

        input_scaled = scaler.transform(
            input_data
        )


        # -------------------------------------------------
        # Prediction
        # -------------------------------------------------

        prediction = model.predict(
            input_scaled
        )[0]

        probability = model.predict_proba(
            input_scaled
        )[0][1]


        # -------------------------------------------------
        # RESULT
        # -------------------------------------------------

        st.divider()

        st.subheader("📊 Prediction Result")

        probability_percent = probability * 100

        if prediction == 1:

            st.error(
                "⚠️ HIGH ATTRITION RISK"
            )

            st.metric(
                "Attrition Probability",
                f"{probability_percent:.2f}%"
            )

            st.warning(
                "The model predicts that this employee "
                "has a higher likelihood of leaving."
            )

        else:

            st.success(
                "✅ LOW ATTRITION RISK"
            )

            st.metric(
                "Attrition Probability",
                f"{probability_percent:.2f}%"
            )

            st.info(
                "The model predicts that this employee "
                "has a lower likelihood of leaving."
            )


    except Exception as e:

        st.error(
            "An error occurred while making the prediction."
        )

        st.exception(e)