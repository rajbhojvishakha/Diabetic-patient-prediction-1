import streamlit as st
import pandas as pd
import pickle

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("model.pkl", "rb"))
sc = pickle.load(open("sc.pkl", "rb"))

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.stApp{
    background-color:#F8FAFC;
}

.main-title{
    text-align:center;
    color:#2563EB;
    font-size:42px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:#64748B;
    font-size:18px;
    margin-bottom:30px;
}

div[data-testid="stForm"]{
    background:white;
}

div[data-testid="stVerticalBlock"]{
    border-radius:15px;
}

[data-testid="stSidebar"]{
    background:#2563EB;
}

.stButton>button{
    width:100%;
    background:#2563EB;
    color:white;
    font-size:18px;
    border:none;
    border-radius:10px;
    padding:12px;
    font-weight:bold;
}

.stButton>button:hover{
    background:#1D4ED8;
    color:white;
}

div[data-baseweb="input"]{
    border-radius:10px;
}

.stSlider{
    padding-top:10px;
}

.result{
    padding:20px;
    border-radius:12px;
    text-align:center;
    font-size:24px;
    font-weight:bold;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 class='main-title'>🩺 Diabetes Prediction System</h1>",
    unsafe_allow_html=True,
)

st.markdown(
    "<p class='sub-title'>Machine Learning Based Diabetes Prediction</p>",
    unsafe_allow_html=True,
)

# ---------------- INPUT SECTION ----------------
st.markdown("### 📋 Patient Information")

col1, col2 = st.columns(2)

with col1:

    Pregnancies = st.slider("Pregnancies",0,17,1)

    BloodPressure = st.slider(
        "Blood Pressure (mmHg)",
        40,140,72
    )

    Insulin = st.slider(
        "Insulin",
        15,300,80
    )

    DiabetesPedigreeFunction = st.number_input(
        "Diabetes Pedigree Function",
        min_value=0.05,
        max_value=3.0,
        value=0.47,
        step=0.001,
        format="%.3f"
    )

with col2:

    Glucose = st.slider(
        "Glucose Level",
        50,200,120
    )

    SkinThickness = st.slider(
        "Skin Thickness",
        7,99,20
    )

    BMI = st.slider(
        "BMI",
        18.0,
        50.0,
        32.0,
        step=0.1
    )

    Age = st.slider(
        "Age",
        21,
        81,
        33
    )

st.write("")
st.write("")

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict Diabetes"):

    columns = [
        'Pregnancies',
        'Glucose',
        'BloodPressure',
        'SkinThickness',
        'Insulin',
        'BMI',
        'DiabetesPedigreeFunction',
        'Age'
    ]

    myinput = [[
        Pregnancies,
        Glucose,
        BloodPressure,
        SkinThickness,
        Insulin,
        BMI,
        DiabetesPedigreeFunction,
        Age
    ]]

    myinput = pd.DataFrame(myinput, columns=columns)
    myinput = pd.DataFrame(sc.transform(myinput), columns=columns)

    prediction = model.predict(myinput)

    st.divider()

    st.subheader("Prediction Result")

    if prediction[0] == 1:

        st.success("✅ The patient is **NOT Diabetic**")

    else:

        st.error("⚠️ The patient is **Diabetic**")

