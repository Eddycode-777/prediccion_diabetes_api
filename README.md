# API de Predicción de Diabetes

Esta API permite predecir la probabilidad de diabetes a partir de un conjunto de características clínicas, utilizando un modelo de Machine Learning entrenado con Random Forest.  
El modelo se entrenó en Google Colab y se despliega mediante Flask.

---

## Tecnologías utilizadas

- Python 
- Flask
- Scikit-learn
- Joblib
- Render (para despliegue en la nube)

---

## Estructura del proyecto

diabetes-api/
│── app.py
│── config/
│ └── load_assets.py
│── models/
│ ├── diabetes_model.pkl
│ ├── scaler.pkl
│ └── columns.json
│── routes/
│ └── predict.py
│── requirements.txt
│── README.md

yaml
Copiar código

---

## Endpoint principal

### POST `/predict`

Recibe un JSON con los valores de las 8 características y devuelve la predicción y la probabilidad de diabetes.

#### Características requeridas:

- Pregnancies
- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI
- DiabetesPedigreeFunction
- Age

#### Ejemplo de JSON de entrada

```json
{
    "Pregnancies": 2,
    "Glucose": 120,
    "BloodPressure": 70,
    "SkinThickness": 25,
    "Insulin": 80,
    "BMI": 28.5,
    "DiabetesPedigreeFunction": 0.35,
    "Age": 30
}
Ejemplo de respuesta
json
Copiar código
{
  "prediction": 1,
  "probability_of_diabetes": "82.4%"
}
prediction = 1 → El modelo predice diabetes

prediction = 0 → El modelo NO predice diabetes