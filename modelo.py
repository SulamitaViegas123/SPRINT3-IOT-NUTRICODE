import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

def treinar_modelo():
    print("🔥 Iniciando treinamento...")

    df = pd.read_csv("alimentos.csv", encoding="latin-1")
    df = df.fillna(0)

    X = df[["CALORIAS", "PROTEINA", "ACUCAR", "GORDURA", "CARBOIDRATO"]]
    y = df["CLASSIFICACAO"]

    le = LabelEncoder()
    y_encoded = le.fit_transform(y)

    # divisão mais segura
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded,
        test_size=0.3,   # aumenta o teste
        random_state=42,
        stratify=y_encoded  # 🔥 MUITO IMPORTANTE
    )

    # Decision Tree otimizada
    model = DecisionTreeClassifier(
        max_depth=4,              # evita overfitting
        min_samples_split=5,      # exige mais dados por divisão
        min_samples_leaf=2,       # evita árvore "decorando"
        random_state=42
    )

    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)

    print("✅ Modelo treinado com sucesso")
    print(f"🎯 Acurácia: {acc:.2f}")

    return model, le, acc


if __name__ == "__main__":
    treinar_modelo()