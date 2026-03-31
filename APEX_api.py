import requests

def carregar_alimentos():
    url = "https://oracleapex.com/ords/sulamita/api/alimentos"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()  # lista/dicionário dos alimentos
    else:
        raise Exception(f"Erro ao acessar API: {response.status_code}")

if __name__ == "__main__":
    alimentos = carregar_alimentos()
    for item in alimentos:
        print(item)