# CRUD Python + MySQL

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)](https://www.mysql.com/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-Environment%20Variables-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://pypi.org/project/python-dotenv/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/leonardodiello/CRUD_Python)

CRUD desenvolvido em **Python** integrado ao **MySQL**, com o objetivo de praticar operações básicas de manipulação de dados em um banco de dados relacional.

O projeto implementa as quatro operações fundamentais de um CRUD:

* **Create** — Inserção de registros.
* **Read** — Consulta de registros.
* **Update** — Atualização de registros.
* **Delete** — Exclusão de registros.

## Tecnologias utilizadas

* Python.
* MySQL.
* MySQL Connector/Python.
* python-dotenv.

## Estrutura do projeto

```text
CRUD_Python/
│
├── conexao.py
├── create.py
├── read.py
├── update.py
├── delete.py
├── .env
└── .gitignore
```

### `conexao.py`

Responsável por estabelecer a conexão entre a aplicação Python e o banco de dados MySQL.

As credenciais são obtidas por meio de variáveis de ambiente utilizando `python-dotenv`.

### `create.py`

Responsável pela criação de novos registros na tabela `vendas`.

### `read.py`

Responsável pela consulta dos registros armazenados no banco de dados.

### `update.py`

Responsável pela atualização de informações existentes na tabela `vendas`.

### `delete.py`

Responsável pela exclusão de registros na tabela `vendas`.

## Como funciona

O projeto utiliza uma tabela chamada `vendas` para armazenar os dados.

As operações são executadas diretamente através de comandos SQL enviados pelo Python ao MySQL.

O fluxo básico é:

```text
Python
   │
   ▼
conexao.py
   │
   ▼
MySQL
   │
   ├── CREATE
   ├── READ
   ├── UPDATE
   └── DELETE
```

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/leonardodiello/CRUD_Python.git
```

Entre na pasta:

```bash
cd CRUD_Python
```

### 2. Crie um ambiente virtual

```bash
python3 -m venv .venv
```

Ative o ambiente virtual:

**macOS/Linux:**

```bash
source .venv/bin/activate
```

**Windows:**

```bash
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install mysql-connector-python python-dotenv
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

O arquivo `.env` não deve ser enviado para o GitHub, pois contém informações sensíveis de acesso ao banco de dados.

### 5. Configure o banco de dados

Crie o banco de dados no MySQL:

```sql
CREATE DATABASE crud_python;
```

Depois, selecione o banco:

```sql
USE crud_python;
```

Crie a tabela utilizada pelo projeto:

```sql
CREATE TABLE vendas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);
```

Atualize o arquivo `.env`:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=crud_python
```

## Executando o projeto

Cada operação do CRUD está separada em seu próprio arquivo.

### Create

Para inserir um novo registro:

```bash
python create.py
```

### Read

Para consultar os registros:

```bash
python read.py
```

### Update

Para atualizar um registro:

```bash
python update.py
```

### Delete

Para excluir um registro:

```bash
python delete.py
```

## Conceito de CRUD

CRUD é um acrônimo para as quatro operações fundamentais utilizadas na manipulação de dados:

| Operação | SQL      | Descrição                      |
| -------- | -------- | ------------------------------ |
| Create   | `INSERT` | Cria um novo registro.         |
| Read     | `SELECT` | Consulta registros.            |
| Update   | `UPDATE` | Atualiza registros existentes. |
| Delete   | `DELETE` | Remove registros.              |

## Objetivo do projeto

Este projeto foi desenvolvido com foco no aprendizado de:

* Integração entre Python e MySQL.
* Conexão com banco de dados.
* Execução de comandos SQL através do Python.
* Manipulação de registros.
* Utilização de variáveis de ambiente.
* Organização de operações CRUD em diferentes módulos.

## Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* Criar uma interface de usuário.
* Implementar um menu interativo no terminal.
* Utilizar consultas parametrizadas para aumentar a segurança.
* Adicionar tratamento de exceções.
* Implementar validação dos dados.
* Utilizar classes para organizar o acesso ao banco.
* Criar uma API utilizando FastAPI.
* Adicionar testes automatizados.
* Implementar `requirements.txt` ou `pyproject.toml`.

## Autor

**Leonardo Diello Charão**

Estudante de Engenharia de Software.

GitHub: [leonardodiello](https://github.com/leonardodiello)
