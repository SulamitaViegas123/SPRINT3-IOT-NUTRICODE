from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# ===== TREINA MODELO UMA VEZ =====
df = pd.read_csv("alimentos.csv", encoding="latin-1")
df = df.fillna(0)

X = df[["CALORIAS", "PROTEINA", "ACUCAR", "GORDURA", "CARBOIDRATO"]]
y = df["CLASSIFICACAO"]

le = LabelEncoder()
y_encoded = le.fit_transform(y)

model = DecisionTreeClassifier(max_depth=5)
model.fit(X, y_encoded)

# ===== ROTA API =====
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

    return jsonify({"classificacao": resultado[0]})

if __name__ == "__main__":
    app.run(debug=True)