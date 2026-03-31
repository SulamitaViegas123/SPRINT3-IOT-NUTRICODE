from flask import Flask, request, jsonify
from modelo import treinar_modelo

app = Flask(__name__)

# carrega modelo
model, le, acc = treinar_modelo()

@app.route("/")
def home():
    return "API NutriCode rodando 🚀"

@app.route("/prever", methods=["POST"])
def prever():
    data = request.json

    entrada = [[
        data["calorias"],
        data["proteina"],
        data["acucar"],
        data["gordura"],
        data["carboidrato"]
    ]]

    pred = model.predict(entrada)
    resultado = le.inverse_transform(pred)

    return jsonify({
        "classificacao": resultado[0],
        "fonte_dados": "CSV"
    })

if __name__ == "__main__":
    app.run(debug=True)