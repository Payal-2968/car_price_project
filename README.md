# 🚗 Car Price Prediction System

A Machine Learning project that predicts the estimated price of a used car based on its brand, model, manufacturing year, mileage, and number of previous owners.

The project uses **Python, Scikit-learn, and Streamlit** to provide an interactive web application where users can enter car details and receive a predicted price.

## ✨ Features

* Select a car brand and model.
* Enter the manufacturing year.
* Enter the car's mileage.
* Specify the number of previous owners.
* Predict the estimated car price using a trained Linear Regression model.
* View the result through an interactive Streamlit interface.

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Streamlit
* Joblib
* Jupyter Notebook
* VS Code

## 📂 Project Structure

```text
car_price_ui/
├── app.py
├── model.pkl
├── brand_encoder.pkl
├── model_encoder.pkl
├── Requirement.txt
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

Replace `YOUR_GITHUB_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Open the project folder

```bash
cd car_price_ui
```

### 3. Install the required libraries

```bash
python -m pip install -r Requirement.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run app.py
```

The application will open in your browser, usually at:

`http://localhost:8501`

## 🧠 Machine Learning Model

The application uses a trained Linear Regression model to estimate car prices.

**Input features:**

* Brand
* Model
* Manufacturing Year
* Mileage
* Number of Previous Owners

The trained model and label encoders are loaded from saved `.pkl` files.

## 🚀 How to Use

1. Open the web application.
2. Select the car brand and model.
3. Enter the manufacturing year and mileage.
4. Enter the number of previous owners.
5. Click **Predict Car Price**.
6. View the estimated price.

## 📊 Output

The application displays the estimated car price based on the input details.

The prediction is an estimate and may differ from the actual market price.

## ⚠️ Limitations

* Prediction accuracy depends on the training dataset and model performance.
* The predicted price is not a guaranteed selling price.
* The currency should be verified against the original dataset.

## 👩‍💻 Author

**Payal Idhate**

Computer Engineering Student

Bharati Vidyapeeth's College of Engineering for Women, Pune

## 📄 License

This project is intended for educational and learning purposes.
