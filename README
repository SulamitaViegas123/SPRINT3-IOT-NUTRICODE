# 🥗 NutriCode IA - Classificação Inteligente de Alimentos

## 📌 Objetivo

O projeto NutriCode IA tem como objetivo analisar alimentos com base em seus dados nutricionais e gerar classificações inteligentes utilizando Inteligência Artificial.

A solução auxilia usuários na tomada de decisão alimentar através da análise de:

- Calorias
- Proteínas
- Açúcar
- Gordura
- Carboidratos

Inicialmente, o projeto foi planejado para integração completa via Oracle APEX utilizando ORDS/REST. Porém, devido a instabilidades temporárias do serviço ORDS durante o desenvolvimento da sprint, foi utilizada uma abordagem híbrida com arquivo CSV como fonte confiável de dados para treinamento do modelo.

---

# 🤖 Modelo de Inteligência Artificial

O modelo utilizado foi:

## Decision Tree Classifier (Árvore de Decisão)

A escolha foi feita devido às seguintes vantagens:

- Alta interpretabilidade
- Fácil implementação
- Boa performance com dados numéricos
- Capacidade de identificar padrões nutricionais
- Baixo custo computacional

O modelo foi desenvolvido em Python utilizando a biblioteca Scikit-learn.

---

# 📊 Base de Dados

Os dados foram extraídos da tabela `ALIMENTOS` no Oracle APEX através do SQL Commands.

A base contém atributos como:

- ID
- Nome
- Calorias
- Proteína
- Açúcar
- Gordura
- Carboidrato
- Classificação

Os dados foram exportados para CSV e utilizados no treinamento do modelo.

Atualmente a base possui mais de 40 registros alimentares, podendo ser expandida futuramente.

---

# 🔄 Fluxo da Solução

O funcionamento da aplicação ocorre da seguinte forma:

1. O usuário preenche os dados nutricionais no Oracle APEX
2. O Oracle APEX envia os dados via REST API
3. A API Flask recebe os dados em formato JSON
4. O modelo treinado processa as informações
5. A IA retorna a classificação nutricional
6. O Oracle APEX exibe o resultado ao usuário

---

# ☁️ Hospedagem da API

A API foi hospedada em nuvem utilizando a plataforma Render.

## Endpoint principal

```txt
https://nutricode-ia-api.onrender.com
```

Esse endpoint responde via método GET e demonstra que a API está online.

## Endpoint de previsão

```txt
https://nutricode-ia-api.onrender.com/prever
```

Esse endpoint utiliza o método POST, sendo responsável pelas previsões da IA.

---

# ⚙️ Tecnologias Utilizadas
Python, Flask, Pandas, Scikit-learn, Oracle APEX, Oracle SQL, REST API, Render Cloud e CSV.

---

# 📁 Estrutura dos Arquivos

| Arquivo | Função |
|---|---|
| `app.py` | API principal Flask |
| `alimentos.csv` | Base de dados utilizada |
| `requirements.txt` | Dependências do projeto |
| `modelo.py` | Treinamento/testes auxiliares da IA |
| `CSV_api.py` | Versão alternativa da API utilizando CSV |
| `APEX_api.py` | Integração experimental via Oracle APEX |

> Obs: devido às instabilidades temporárias do ORDS/APEX durante a sprint, o arquivo `APEX_api.py` não está sendo utilizado atualmente.

---

# ▶️ Como Executar Localmente

## 1. Instalar dependências

```bash
pip install -r requirements.txt
```

Ou manualmente:

```bash
pip install flask pandas scikit-learn oracledb
```

## 2. Executar a aplicação

```bash
py app.py
```

## 3. Acessar a API

```txt
http://127.0.0.1:5000
```

# 🧪 Testando a IA

## Endpoint de previsão

```txt
POST /prever
```

## Exemplo JSON

```json
{
  "calorias": 200,
  "proteina": 10,
  "acucar": 5,
  "gordura": 8,
  "carboidrato": 20
}
```

# 📈 Classificações da IA

## O modelo foi treinado para retornar classificações como:
Excelente, Bom, Moderado, Alto Risco e Crítico.

# ✅ Resultados Obtidos
## Durante os testes realizados:
- A API foi integrada com sucesso ao Oracle APEX
- O modelo conseguiu classificar alimentos nutricionalmente
- A aplicação respondeu corretamente via REST API
- O deploy em nuvem via Render funcionou corretamente
- O sistema apresentou comportamento consistente durante os testes
Mesmo sendo um protótipo acadêmico, a solução demonstrou potencial de expansão para aplicações reais na área nutricional e alimentícia.

# 👨‍💻 Integrantes
- RM560914 – Lucas Almeida de Siqueira
- RM561090 – Matteus Viegas dos Santos
- RM561089 – Sulamita Viegas dos Santos
