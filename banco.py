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