# Cadê o Carregador? API

Este é um projeto de mapeamento e gerenciamento de carregadores de veículos elétricos na cidade de São José dos Campos.

## 🚀 Funcionalidades

- Adicionar, atualizar, remover e visualizar carregadores.
- Documentação automática da API com Swagger, Redoc ou RapiDoc.

## 🛠️ Configuração do Ambiente

Siga as etapas abaixo para configurar o ambiente local e executar o projeto.

### 1. Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas:

- Python 3.10 ou superior
- `pip` (gerenciador de pacotes do Python)
- Git (opcional, para clonar o repositório)

### 2. Clonar o Repositório (Opcional)

Se você estiver utilizando Git, clone o repositório:

```bash
git clone https://github.com/hrichardvieira/api_cade_carregador
cd api_cade_carregador
```

### 3. Crie e ative um ambiente virtual

Crie um ambiente virtual para isolar as dependências do projeto:

```bash
python3 -m venv venv
```

Ative o ambiente virtual:
- Linux/MacOS
```bash
source venv/bin/activate
```

- Windows
```bash
venv\Scripts\activate
```

### 4. Instale as dependências

Com o ambiente virtual ativado, instale as dependências listadas no arquivo requirements.txt:

```bash
pip install -r [requirements.txt]
```

## ▶️ Como Executar o Projeto

1. Certifique-se de que o ambiente virtual está ativado.
2. Execute o arquivo principal app.py:

```bash
(env)$ flask run --host 0.0.0.0 --port 5000
```
3. Acesse a documentação da API no navegador em: http://127.0.0.1:5000/openapi

## 🗂️ Estrutura do Projeto

```bash
api_cade_carregador/
├── app.py              # Arquivo principal da aplicação FastAPI
├── database/           # Conexão com o banco de dados SQLite
├── model/              # Modelos SQLAlchemy (ORM)
├── routes/             # Rotas da API organizadas por entidade
├── schemas/            # Schemas Pydantic para validação e resposta
├── requirements.txt    # Dependências do projeto
└── README.md           # Documentação do projeto (este arquivo)
```
## ✉️ Contato

Caso tenha dúvidas ou sugestões, entre em contato:

- Nome: Hugo Vieira