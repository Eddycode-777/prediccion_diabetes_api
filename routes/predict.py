from flask import Blueprint, request, jsonify
import numpy as np
from config.load_assets import load_model, load_scaler, load_columns

predict_bp = Blueprint("predict_bp", __name__)

# Cargar assets solo una vez (mejor rendimiento)
model = load_model()
scaler = load_scaler()
columns = load_columns()

@predict_bp.route("/predict", methods=["POST"])
def predict():
    data = request.json

    # Validación de parámetros
    for col in columns:
        if col not in data:
            return jsonify({"error": f"Falta el parámetro requerido: {col}"}), 400

    # Ordenar los valores en el mismo orden que el modelo espera
    try:
        input_values = np.array([data[col] for col in columns]).reshape(1, -1)
    except:
        return jsonify({"error": "Error procesando los valores. Verifica que sean numéricos."}), 400

    # Escalar datos
    input_scaled = scaler.transform(input_values)

    # Predicción
    prediction = model.predict(input_scaled)[0]

    # Probabilidad en porcentaje con símbolo %
    probability = model.predict_proba(input_scaled)[0][1] * 100  # Convertir a porcentaje
    probability = round(probability, 1)  # Redondear a 1 decimal
    probability_str = f"{probability}%"  # Convertir a string con %

    return jsonify({
        "prediction": int(prediction),
        "probability_of_diabetes": probability_str
    })
