from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

# Carrega os dados locais exportados/preparados
df = pd.read_csv("alimentos.csv", encoding="latin-1")

# Preenche valores vazios com 0
df = df.fillna(0)

# Colunas usadas pela IA
colunas_entrada = [
    "CALORIAS",
    "PROTEINA",
    "ACUCAR",
    "GORDURA",
    "CARBOIDRATO"
]

# Resultado que a IA aprende a prever
coluna_saida = "CLASSIFICACAO"

X = df[colunas_entrada]
y = df[coluna_saida]

encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

modelo = DecisionTreeClassifier(
    max_depth=4,
    random_state=42
)

modelo.fit(X, y_encoded)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API NutriCode IA funcionando",
        "modelo": "Decision Tree Classifier",
        "status": "online"
    })


@app.route("/prever", methods=["POST"])
def prever():
    dados = request.get_json()

    entrada = [[
        float(dados["calorias"]),
        float(dados["proteina"]),
        float(dados["acucar"]),
        float(dados["gordura"]),
        float(dados["carboidrato"])
    ]]

    resultado = modelo.predict(entrada)
    classificacao = encoder.inverse_transform(resultado)[0]

    return jsonify({
        "classificacao": classificacao,
        "entrada": dados
    })


if __name__ == "__main__":
    app.run(debug=True)