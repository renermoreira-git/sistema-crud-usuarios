# Sistema CRUD de Usuários

Sistema de cadastro de usuários desenvolvido em Python, utilizando Tkinter para a interface gráfica e PostgreSQL para armazenamento dos dados.

O sistema permite realizar as operações CRUD:

- **Create** — cadastrar usuários
- **Read** — consultar usuários
- **Update** — atualizar usuários
- **Delete** — excluir usuários

## Tecnologias utilizadas

- Python
- Tkinter
- PostgreSQL
- Psycopg
- python-dotenv

## Funcionalidades

O sistema possui as seguintes funcionalidades:

- Cadastro de usuários
- Consulta de usuários cadastrados
- Exclusão de usuários pelo ID
- Atualização de dados de usuários
- Pesquisa de usuários por cidade
- Validação dos campos do formulário
- Conexão com banco de dados PostgreSQL

## Interface

O sistema possui uma interface gráfica desenvolvida com Tkinter, organizada em diferentes seções:

- **Cadastrar Usuário**
- **Buscar Usuários**
- **Excluir Usuário**
- **Alterar Usuário**
- **Pesquisar por Cidade**

## Banco de dados

Os dados dos usuários são armazenados em um banco de dados PostgreSQL.

A tabela utilizada possui os seguintes campos:

| Campo | Tipo | Descrição |
|---|---|---|
| id | INTEGER | Identificador do usuário |
| nome | VARCHAR | Nome do usuário |
| idade | INTEGER | Idade do usuário |
| cidade | VARCHAR | Cidade do usuário |

## Estrutura do projeto

```text
sistema/
├── .venv/
├── .env
├── .gitignore
├── banco.py
├── main.py
└── README.md