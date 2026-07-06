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
    background-color:#FAFAFA;
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

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    "<h1 class='main-title'>🩺 Diabetes Prediction System</h1>",
    unsafe_allow_html=True,
)





st.image(
    "diabeties1.png",
    width=700
)



st.sidebar.markdown("### 🩺 Diabetes")
st.sidebar.text("High blood sugar due to insulin issues.")
st.sidebar.text("Needs early detection and control.")
st.sidebar.text("Can cause serious health problems.")

st.sidebar.markdown("### 🩺 Prevention of Type 1 Diabetes")
st.sidebar.text("🧬Type 1 diabetes cannot be fully prevented as it is autoimmune.")
st.sidebar.text("🦠Reduce risk of infections by maintaining good hygiene.")
st.sidebar.text("🥗Support immune health with a balanced nutritious diet.")
st.sidebar.text("👨‍⚕️Early screening if there is a family history.")
st.markdown('-----------')
st.sidebar.markdown("### 🩺 Prevention of Type 2 Diabetes")
st.sidebar.text("🏃 Exercise regularly (at least 30 minutes daily.")
st.sidebar.text("⚖️ Maintain a healthy body weight.")
st.sidebar.text("🍎 Eat a balanced diet low in sugar and processed foods.")
st.sidebar.text("🩺 Go for regular blood sugar check-ups.")

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
        st.subheader("📋 Patient Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Age:** {Age}")
            st.write(f"**BMI:** {BMI}")
            st.write(f"**Glucose:** {Glucose}")
        with col2:
            st.write(f"**Blood Pressure:** {BloodPressure}")
            st.write(f"**Insulin:** {Insulin}")
            st.write(f"**Pregnancies:** {Pregnancies}")

    else:

        st.error("⚠️ The patient is **Diabetic**")
        st.markdown("---")
        st.subheader("📋 Patient Summary")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Age:** {Age}")
            st.write(f"**BMI:** {BMI}")
            st.write(f"**Glucose:** {Glucose}")
        with col2:
            st.write(f"**Blood Pressure:** {BloodPressure}")
            st.write(f"**Insulin:** {Insulin}")
            st.write(f"**Pregnancies:** {Pregnancies}")

