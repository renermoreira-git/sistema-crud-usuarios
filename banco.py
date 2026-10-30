import psycopg
from dotenv import load_dotenv
import os 

load_dotenv()

def conectar():
    conexao = psycopg.connect(
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    return conexao


def insert(nome, idade_convertida, cidade):
    conexao = conectar()
    cursor = conexao.cursor()
    exe_insert(cursor, nome, idade_convertida, cidade)
    conexao.commit()
    fechar_conexao(conexao)
    fechar_cursor(cursor)

def fechar_conexao(conexao):
    conexao.close()
def fechar_cursor(cursor):
    cursor.close()
def exe_insert(cursor, nome, idade_convertida, cidade):
    cursor.execute(
            "INSERT INTO usuarios (nome, idade, cidade) VALUES (%s, %s, %s)" , (nome, idade_convertida, cidade)
        )
    

def listar_usuario(cursor):
    cursor.execute(
        "SELECT * FROM usuarios"
        )
    usuarios = cursor.fetchall()
    return usuarios


def listar_by_id(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "SELECT * FROM usuarios WHERE id = %s", (id,)
    )
    usuario = cursor.fetchone()
    fechar_cursor(cursor)
    fechar_conexao(conexao)
    return usuario


def buscar_user():
    conexao = conectar()
    cursor = conexao.cursor()

    usuarios = listar_usuario(cursor)

    fechar_cursor(cursor)
    fechar_conexao(conexao)
    return usuarios


def deletar_user(id):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "DELETE FROM usuarios WHERE id = %s", (id,)
    )
    conexao.commit()

    fechar_cursor(cursor)
    fechar_conexao(conexao)

def atualizar_user(id, nome, idade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "UPDATE usuarios SET nome = %s, idade = %s WHERE id = %s", (nome, idade, id)
    )
    conexao.commit()

    fechar_conexao(conexao)
    fechar_cursor(cursor)

def atualizar_api(id, dados):
    conexao = conectar()
    cursor = conexao.cursor()

    campos = []
    valores = []

    campos_permitidos = ["nome", "idade", "cidade"]

    for campo, valor in dados.items():
        if campo not in campos_permitidos:
            raise ValueError("Campo Não Permitido")
        
        campos.append(f"{campo}=%s")
        valores.append(valor)

    if not campos:
        raise ValueError("Nenhum campo atualizado")
    
    valores.append(id)

    cursor.execute(
        f"UPDATE usuarios SET {', '.join(campos)} WHERE id=%s", valores
        )
    conexao.commit()

    fechar_cursor(cursor)
    fechar_conexao(conexao)

#Pesquisar Por Cidades

def pesquisar_cidade(cidade):
    conexao = conectar()
    cursor = conexao.cursor()

    cursor.execute(
        "select * from usuarios where cidade = %s", (cidade,)
    )
    
    usuario = cursor.fetchall()
    
    fechar_conexao(conexao)
    fechar_cursor(cursor)
    
    return usuario