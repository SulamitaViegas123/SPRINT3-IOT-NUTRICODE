from flask import Flask, request, jsonify
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)

df = pd.read_csv("alimentos.csv", encoding="latin-1")
df = df.fillna(0)

colunas_entrada = [
    "CALORIAS",
    "PROTEINA",
    "ACUCAR",
    "GORDURA",
    "CARBOIDRATO"
]

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


def traduzir_classificacao(classificacao):
    mapa = {
        "MUITO_SAUDAVEL": "Excelente",
        "SAUDAVEL": "Bom",
        "MODERADO": "Moderado",
        "ALTO_RISCO": "Alto Risco",
        "CRITICO": "Crítico"
    }

    return mapa.get(classificacao, classificacao)


@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "mensagem": "API NutriCode IA funcionando",
        "modelo": "Decision Tree Classifier",
        "status": "online",
        "descricao": "API responsável por classificar alimentos com Inteligência Artificial e retornar o resultado para o Oracle APEX."
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
    classificacao_original = encoder.inverse_transform(resultado)[0]
    classificacao_formatada = traduzir_classificacao(classificacao_original)

    return jsonify({
        "classificacao": classificacao_formatada,
        "classificacao_original": classificacao_original,
        "entrada": dados
    })


if __name__ == "__main__":
    app.run(debug=True)