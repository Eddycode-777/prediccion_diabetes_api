# API de Predicción de Diabetes

Esta API permite predecir la probabilidad de diabetes a partir de un conjunto de características clínicas, utilizando un modelo de Machine Learning entrenado con Random Forest.  
El modelo se entrenó en Google Colab y se despliega mediante Flask. [memory:4]

## Tecnologías utilizadas

- Python 
- Flask
- Scikit-learn
- Joblib
- Render (para despliegue en la nube)

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

text

## URL Pública de la API

[![Render](https://img.shields.io/badge/Render-000000?style=for-the-badge&logo=render&logoColor=white)](https://prediccion-diabetes-api.onrender.com)

## Endpoint principal

### `POST /predict`

Recibe un JSON con los valores de las 8 características y devuelve la predicción y la probabilidad de diabetes.

#### Características requeridas:

| Parámetro                  | Descripción                      |
|----------------------------|----------------------------------|
| `Pregnancies`             | Número de embarazos             |
| `Glucose`                 | Glucosa en sangre               |
| `BloodPressure`           | Presión arterial                |
| `SkinThickness`           | Grosor de pliegue cutáneo       |
| `Insulin`                 | Insulina sérica                 |
| `BMI`                     | Índice de masa corporal         |
| `DiabetesPedigreeFunction`| Función de pedigrí de diabetes  |
| `Age`                     | Edad                            |

#### Ejemplo de JSON de entrada

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

text

#### Ejemplo de respuesta

{
"prediction": 0,
"probability_of_diabetes": "26.3%"
}

text

**prediction = 1** → El modelo predice diabetes  
**prediction = 0** → El modelo NO predice diabetes

## Cómo probar la API

### Con Postman:

Método: POST
URL: https://prediccion-diabetes-api.onrender.com/predict
Body: raw JSON (ejemplo arriba)

text

### Con cURL:

curl -X POST https://prediccion-diabetes-api.onrender.com/predict
-H "Content-Type: application/json"
-d '{"Pregnancies":2,"Glucose":120,"BloodPressure":70,"SkinThickness":25,"Insulin":80,"BMI":28.5,"DiabetesPedigreeFunction":0.35,"Age":30}'

text

## Notas

- La API está desplegada en Render con instancia gratuita; puede demorar unos segundos en "despertar" si no hay actividad reciente.
- El modelo fue entrenado usando **scikit-learn 1.6.1** y debe usarse con las mismas versiones de librerías para evitar errores.

---