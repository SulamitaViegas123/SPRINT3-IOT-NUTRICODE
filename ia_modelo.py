import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder

# Carregar dados
df = pd.read_csv("alimentos.csv", encoding="latin-1")

from nutricode_api import carregar_alimentos

alimentos = carregar_alimentos()
print(alimentos)

# 🔥 NORMALIZA COLUNAS
df.columns = df.columns.str.upper().str.strip()

print("Colunas:", df.columns)

# Features
X = df[["CALORIAS", "PROTEINA", "ACUCAR", "GORDURA", "CARBOIDRATO"]]

# Target
y = df["CLASSIFICACAO"]

# Encoder
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.3, random_state=42)

# Modelo
modelo = DecisionTreeClassifier(max_depth=5)
modelo.fit(X_train, y_train)

# Avaliação
accuracy = modelo.score(X_test, y_test)
print(f"Acurácia: {accuracy:.2f}")

# Teste
import pandas as pd
novo = pd.DataFrame([[200, 5, 20, 10, 30]],
columns=["CALORIAS", "PROTEINA", "ACUCAR", "GORDURA", "CARBOIDRATO"])
prev = modelo.predict(novo)

print("Resultado:", le.inverse_transform(prev))