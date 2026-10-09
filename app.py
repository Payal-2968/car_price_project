
import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE SETTINGS ----------------
st.set_page_config(
    page_title="Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

# ---------------- WEBSITE TITLE ----------------
st.title("🚗 Car Price Prediction System")
st.write(
    "Enter your car details below to estimate "
    "the selling price using Machine Learning."
)

st.divider()

# ---------------- LOAD TRAINED MODEL ----------------
try:
    model = joblib.load("model.pkl")
    brand_encoder = joblib.load("brand_encoder.pkl")
    model_encoder = joblib.load("model_encoder.pkl")

except Exception as e:
    st.error(f"Unable to load model files: {e}")
    st.info(
        "Make sure model.pkl, brand_encoder.pkl, "
        "and model_encoder.pkl are in the same folder as app.py."
    )
    st.stop()

# ---------------- CAR INPUT FORM ----------------
st.subheader("Enter Car Details")

col1, col2 = st.columns(2)

with col1:
    brand = st.selectbox(
        "Select Car Brand",
        brand_encoder.classes_.tolist()
    )

    car_model = st.selectbox(
        "Select Car Model",
        model_encoder.classes_.tolist()
    )

    year = st.number_input(
        "Manufacturing Year",
        min_value=1990,
        max_value=2026,
        value=2020,
        step=1
    )

with col2:
    mileage = st.number_input(
        "Mileage (km)",
        min_value=0,
        value=50000,
        step=1000
    )

    owners = st.number_input(
        "Number of Previous Owners",
        min_value=0,
        max_value=20,
        value=1,
        step=1
    )

st.divider()

# ---------------- PREDICT PRICE ----------------
if st.button("🔍 Predict Car Price", type="primary"):

    try:
        # Encode brand and model
        brand_encoded = brand_encoder.transform([brand])[0]
        model_encoded = model_encoder.transform([car_model])[0]

        # Prepare input with the exact training feature names
        input_data = pd.DataFrame(
            [[
                brand_encoded,
                model_encoded,
                year,
                mileage,
                owners
            ]],
            columns=[
                "Brand",
                "Model",
                "Year",
                "Mileage",
                "Owner_Count"
            ]
        )

        # Predict price
        prediction = model.predict(input_data)[0]

        # Display result
        st.success("Prediction completed successfully!")

        st.subheader("Estimated Car Price")

        st.metric(
            label="Predicted Price",
           value=f"₹ {prediction:,.2f}"
        )

        st.caption(
            "Note: This is an estimated price generated "
            "by your trained Machine Learning model. "
            "The actual market price may differ."
        )

    except Exception as e:
        st.error(f"Prediction error: {e}")

# ---------------- FOOTER ----------------
st.divider()
st.caption("Car Price Prediction System | Machine Learning Project")