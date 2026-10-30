# Sistema CRUD de Usuários
 
Sistema de cadastro de usuários desenvolvido em Python, com duas formas de uso:
 
- **Interface gráfica** em Tkinter
- **API REST** em FastAPI
Ambas utilizam o mesmo banco PostgreSQL e permitem as operações CRUD:
 
- **Create** — cadastrar usuários
- **Read** — consultar usuários
- **Update** — atualizar usuários
- **Delete** — excluir usuários
## Tecnologias utilizadas
 
- Python 3.10+
- Tkinter
- FastAPI + Uvicorn
- Pydantic
- PostgreSQL
- Psycopg 3
- python-dotenv
## Funcionalidades
 
- Cadastro de usuários
- Consulta de todos os usuários cadastrados
- Consulta de usuário por ID (API)
- Atualização de dados de usuários
- Exclusão de usuários pelo ID
- Pesquisa de usuários por cidade (interface gráfica)
- Validação dos campos do formulário
- Conexão com banco de dados PostgreSQL via variáveis de ambiente
## Estrutura do projeto
 
```text
sistema-crud-usuarios/
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
├── main.py            # Interface gráfica (Tkinter)
├── estilos.py         # Estilos dos widgets ttk
├── api.py             # API REST (FastAPI)
├── models.py          # Modelos Pydantic (Usuario, UsuarioUpdate)
├── crud_usuario.py    # Camada intermediária entre a API e o banco
└── banco.py           # Conexão e consultas SQL (PostgreSQL)
```
 
## Banco de dados
 
A tabela utilizada possui os seguintes campos:
 
| Campo  | Tipo    | Descrição               |
|--------|---------|-------------------------|
| id     | INTEGER | Identificador do usuário |
| nome   | VARCHAR | Nome do usuário         |
| idade  | INTEGER | Idade do usuário        |
| cidade | VARCHAR | Cidade do usuário       |
 
Exemplo de criação da tabela:
 
```sql
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    idade INTEGER NOT NULL,
    cidade VARCHAR(100) NOT NULL
);
```
 
## Instalação
 
1. Clone o repositório e entre na pasta do projeto.
2. Crie e ative um ambiente virtual:
```bash
python -m venv .venv
 
# Linux/macOS
source .venv/bin/activate
 
# Windows
.venv\Scripts\activate
```
 
3. Instale as dependências:
```bash
pip install -r requirements.txt
```
 
> No Linux, o Tkinter pode precisar ser instalado separadamente
> (ex.: `sudo apt install python3-tk`).
 
## Configuração
 
Crie um arquivo `.env` na raiz do projeto com os dados de conexão:
 
```env
DB_HOST=localhost
DB_NAME=nome_do_banco
DB_USER=seu_usuario
DB_PASSWORD=sua_senha
```
 
## Como executar
 
### Interface gráfica
 
```bash
python main.py
```
 
### API
 
```bash
uvicorn api:app --reload
```
 
A documentação interativa fica disponível em `http://127.0.0.1:8000/docs`.
 
## Endpoints da API
 
| Método | Rota                        | Descrição                  |
|--------|-----------------------------|----------------------------|
| POST   | `/usuarios`                 | Cria um usuário            |
| GET    | `/usuarios`                 | Lista todos os usuários    |
| GET    | `/usuarios/{id}`            | Busca um usuário pelo ID   |
| PATCH  | `/usuarios?id={id}`         | Atualiza campos do usuário |
| DELETE | `/usuarios/deletar?id={id}` | Exclui um usuário          |
 
Exemplo de corpo para `POST /usuarios`:
 
```json
{
  "nome": "Maria",
  "idade": 25,
  "cidade": "Fortaleza"
}
```
 
No `PATCH`, todos os campos são opcionais; apenas os enviados são atualizados.
 
## Interface
 
A interface gráfica é organizada em seções:
 
- **Cadastrar Usuário**
- **Buscar Usuários**
- **Excluir Usuário**
- **Alterar Usuário**
- **Pesquisar por Cidade**