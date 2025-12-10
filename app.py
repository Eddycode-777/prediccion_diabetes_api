from flask import Flask
from routes.predict import predict_bp

app = Flask(__name__)

# Registrar Blueprint
app.register_blueprint(predict_bp)

@app.route("/", methods=["GET"])
def home():
    return {"message": "API de predicción de diabetes funcionando"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
