# ⚡ Energy Output Prediction

## 📌 Overview

Energy Output Prediction is a machine learning project that predicts electrical energy output using environmental and operational measurements. It combines data analysis, model training, evaluation, and a web application that allows users to submit input values and receive predictions.

The project demonstrates an end-to-end machine learning workflow, from model development to API integration and frontend interaction.

## 🎯 Objectives

- Analyze the relationship between input variables and energy output.
- Train and compare different machine learning algorithms.
- Evaluate models using appropriate regression metrics.
- Build an interactive prediction application.
- Expose the trained model through a FastAPI REST API.

## 📊 Dataset Features

The model uses four input features:

| Feature | Description |
|---|---|
| `AT` | Ambient Temperature |
| `V` | Exhaust Vacuum |
| `AP` | Ambient Pressure |
| `RH` | Relative Humidity |
| `PE` | Electrical Energy Output — target variable |

## 🤖 Models Explored

The project explores multiple approaches to regression:

- Linear Regression
- Polynomial Regression
- Decision Tree Regression
- Artificial Neural Network (ANN) / Multilayer Perceptron (MLP)

Models are compared using regression evaluation metrics to understand their predictive performance.

## 📈 Evaluation Metrics

- **MAE (Mean Absolute Error):** Measures the average absolute prediction error.
- **RMSE (Root Mean Squared Error):** Penalizes larger prediction errors more heavily.
- **R² Score:** Measures how much variation in the target is explained by the model.

## 🛠️ Technologies Used

- Python
- Pandas and NumPy
- Scikit-learn
- TensorFlow (for ANN/MLP experiments)
- FastAPI
- Uvicorn
- HTML, CSS, and JavaScript
- Git and GitHub

## 🌐 Application Architecture

1. The user enters environmental measurements in the frontend.
2. JavaScript sends the values to the FastAPI `/predict` endpoint.
3. The API prepares the input features and passes them to the trained model.
4. The model generates an energy output prediction.
5. The frontend displays the result to the user.

## 🚀 Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/brandonmutua/Energy_output_prediction.git
cd Energy_output_prediction
```

### 2. Create and activate a virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the FastAPI server

```bash
uvicorn main:app --reload
```

### 5. Open the application

- Frontend: http://127.0.0.1:8000/app
- API documentation: http://127.0.0.1:8000/docs
- Health check: http://127.0.0.1:8000/health

Ensure the trained model file is present in the expected location before starting the server.

## 📁 Project Structure

```text
Energy_output_prediction/
├── main.py
├── index.html
├── energy_output_model.joblib
├── requirements.txt
├── .gitignore
└── README.md
```

Additional notebooks, datasets, or model artifacts may be included if they are part of the repository.

## 🔮 Future Improvements

- Deploy the application to a cloud hosting platform.
- Improve model performance through feature engineering and hyperparameter tuning.
- Add model monitoring and input validation.
- Expand the user interface and improve prediction visualization.

## 👨‍💻 Author

**Brandon Mutua**

GitHub: [@brandonmutua](https://github.com/brandonmutua)

---

*An applied machine learning project focused on regression, model evaluation, API development, and interactive prediction.*
