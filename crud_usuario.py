from banco import *
from models import UsuarioUpdate

def criar_usuario(nome, idade, cidade):
    insert (nome, idade, cidade)

def listar_user():
    return buscar_user()

def listar_por_id(id):
    id_retornado = listar_by_id(id)
    return id_retornado

def atualizar(id, usuario: UsuarioUpdate):
    dados = usuario.model_dump(exclude_unset=True)
    atualizar_api(id, dados)

def excluir(id):
    deletar_user(id)