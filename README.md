# CRUD Python + MySQL

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-000000?style=for-the-badge\&logo=flask\&logoColor=white)](https://flask.palletsprojects.com/)
[![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?style=for-the-badge\&logo=mysql\&logoColor=white)](https://www.mysql.com/)
[![python-dotenv](https://img.shields.io/badge/python--dotenv-Environment%20Variables-3776AB?style=for-the-badge\&logo=python\&logoColor=white)](https://pypi.org/project/python-dotenv/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-181717?style=for-the-badge\&logo=github\&logoColor=white)](https://github.com/leonardodiello/CRUD_Python)

## Sobre o projeto

CRUD desenvolvido em **Python**, utilizando **Flask** para a aplicação web e **MySQL** para armazenamento dos dados.

O projeto foi desenvolvido com o objetivo de praticar a integração entre uma aplicação web e um banco de dados relacional, implementando as quatro operações fundamentais de um CRUD:

* **Create** — Inserção de registros
* **Read** — Consulta de registros
* **Update** — Atualização de registros
* **Delete** — Exclusão de registros

Além da parte de banco de dados, o projeto possui uma interface web desenvolvida com **HTML e CSS**, integrada ao backend através do Flask.

## Tecnologias utilizadas

* **Python**
* **Flask**
* **MySQL**
* **MySQL Connector/Python**
* **python-dotenv**
* **HTML**
* **CSS**
* **Jinja2**

## Funcionalidades

* Cadastro de produtos
* Listagem dos produtos cadastrados
* Atualização do valor de um produto
* Exclusão de produtos
* Integração entre Flask e MySQL
* Interface web para interação com o banco de dados
* Utilização de variáveis de ambiente para configuração do banco

## Estrutura do projeto

```text
CRUD_Python/
│
├── static/
│   └── arquivos estáticos
│
├── templates/
│   └── index.html
│
├── app.py
├── conexao.py
├── .gitignore
└── README.md
```

### Principais arquivos

**`app.py`**

Arquivo principal da aplicação Flask. É responsável pelas rotas e pelas operações do CRUD.

As principais rotas são:

```text
/              → Lista os produtos
/create        → Cadastra um produto
/update/<id>   → Atualiza o valor de um produto
/delete/<id>   → Exclui um produto
```

**`conexao.py`**

Responsável por estabelecer a conexão entre a aplicação Python e o banco de dados MySQL.

**`templates/`**

Armazena os templates HTML utilizados pela aplicação.

**`static/`**

Armazena os arquivos estáticos utilizados pela interface, como arquivos CSS e JavaScript.

## Funcionamento

A aplicação segue um fluxo simples:

```text
                  Interface Web
                       │
                       ▼
                  ┌─────────┐
                  │  Flask  │
                  └────┬────┘
                       │
                       ▼
                  ┌──────────┐
                  │ conexao  │
                  │   .py    │
                  └────┬─────┘
                       │
                       ▼
                  ┌─────────┐
                  │  MySQL  │
                  └────┬─────┘
                       │
             ┌─────────┼─────────┐
             ▼         ▼         ▼
           CREATE     READ     UPDATE
                                  │
                                  ▼
                                DELETE
```

As operações de inserção e atualização utilizam parâmetros na consulta SQL.

Exemplo:

```python
cursor.execute(
    'INSERT INTO vendas (nome_produto, valor) VALUES (%s, %s)',
    (nome_produto, valor)
)
```

## Configuração

### 1. Clone o repositório

```bash
git clone https://github.com/leonardodiello/CRUD_Python.git
cd CRUD_Python
```

### 2. Crie um ambiente virtual

No macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

No Windows:

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 3. Instale as dependências

```bash
pip install Flask mysql-connector-python python-dotenv
```

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto:

```env
DB_HOST=localhost
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
DB_NAME=seu_banco
```

> O arquivo `.env` não deve ser enviado para o GitHub. Utilize o `.gitignore` para manter as credenciais fora do repositório.

### 5. Crie o banco de dados

Exemplo de estrutura utilizada pelo projeto:

```sql
CREATE DATABASE crud_python;

USE crud_python;

CREATE TABLE vendas (
    idVendas INT AUTO_INCREMENT PRIMARY KEY,
    nome_produto VARCHAR(100) NOT NULL,
    valor DECIMAL(10, 2) NOT NULL
);
```

### 6. Execute a aplicação

```bash
python app.py
```

Com o servidor iniciado, acesse a aplicação pelo endereço exibido no terminal.

Durante o desenvolvimento, o projeto utiliza o modo `debug` do Flask. Esse modo deve ser utilizado apenas no ambiente de desenvolvimento.

## Fluxo das operações

### Create

O usuário preenche o formulário com o nome e o valor do produto. O Flask recebe os dados através de `request.form` e realiza um `INSERT` na tabela `vendas`.

### Read

Ao acessar a página inicial, a aplicação executa um `SELECT` na tabela `vendas` e envia os registros para o template HTML.

### Update

O usuário informa um novo valor para o produto. A aplicação utiliza o **`idVendas`** do registro para executar um `UPDATE`.

```sql
UPDATE vendas
SET valor = %s
WHERE idVendas = %s;
```

### Delete

A aplicação utiliza o **`idVendas`** do produto para executar um `DELETE`.

```sql
DELETE FROM vendas
WHERE idVendas = %s;
```

Após as operações de alteração, o Flask redireciona o usuário para a página principal.

## Objetivos do projeto

Este projeto foi desenvolvido para praticar:

* Desenvolvimento web com Python
* Utilização do framework Flask
* Criação de rotas
* Manipulação de requisições HTTP
* Renderização de templates HTML
* Integração entre Python e MySQL
* Consultas SQL
* Operações CRUD
* Utilização de variáveis de ambiente
* Organização básica de uma aplicação web

## Próximos passos

Algumas melhorias que podem ser implementadas futuramente:

* Melhorar a interface da aplicação
* Adicionar validação dos dados recebidos
* Implementar tratamento de exceções
* Criar mensagens de sucesso e erro
* Separar melhor a camada de acesso ao banco de dados
* Adicionar testes automatizados
* Criar `requirements.txt`
* Estruturar o projeto utilizando Blueprints
* Adicionar autenticação de usuários
* Criar uma API REST com Flask ou FastAPI
* Containerizar a aplicação com Docker

## Autor

**Leonardo Diello Charão**

Estudante de Engenharia de Software no IFAM.

* GitHub: [@leonardodiello](https://github.com/leonardodiello)
* Projeto: [CRUD_Python](https://github.com/leonardodiello/CRUD_Python)
