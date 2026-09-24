import tkinter as tk 
from banco import *

janela = tk.Tk()

janela.title("Cadastro de Usuário")
janela.configure(bg="#F1F5F9")

#Titulo
titulo = tk.Label(
    janela, 
    text="CADASTRO DE USUÁRIO",
    font=("Arial", 24, "bold"),
    bg="#0F172A",
    fg="white",
    pady=20
)
titulo.grid(row = 0, column=0, columnspan=3, sticky="nsew")

#Janelas Cadastro, Busca, Exluir e Alterar 
frame_cadastro = tk.LabelFrame(
    janela, 
    text="Cadastrar Usuário"
)
frame_cadastro.configure(background="lightblue")

frame_cadastro.grid(
    row=1,
    column=0,
    padx=5
)

frame_busca = tk.LabelFrame(
    janela,
    text="Buscar Usuarios"
)
frame_busca.grid(
    row=1,
    column=2,
    padx=5
)

frame_excluir = tk.LabelFrame(
    janela,
    text="Excluir Usuário"
)
frame_excluir.grid(
    row=2,
    column=0,
    padx=5
)

frame_alterar = tk.LabelFrame(
    janela,
    text="Alterar Usuário"
)
frame_alterar.grid(
    row=3,
    column=0,
    padx=20,
    pady=10,
    sticky="nsew"
)

frame_pesquisar = tk.LabelFrame(
    janela,
    text="Pesquisar por Cidade"
)
frame_pesquisar.grid(row=2, column=2)


#Nome, Idade e Cidade

nome = tk.Label(
    frame_cadastro, 
    text="Nome: ",
    font=("Arial", 10)
)

idade = tk.Label(
    frame_cadastro, 
    text="Idade: ",
    font=("Arial", 10)
)

cidade = tk.Label(
    frame_cadastro, 
    text="Cidade: ",
    font=("Arial", 10)
)

label_id = tk.Label(
    frame_excluir,
    text="Id do usuário:",
)
label_id.grid(row=0, column=0)

nome.grid(row=0, column=0, padx=10, pady=8)
idade.grid(row=1, column=0, padx=10, pady=8)
cidade.grid(row=2, column=0, padx=10, pady=8)

entrada_nome = tk.Entry(frame_cadastro, width=30)
entrada_idade = tk.Entry(frame_cadastro, width=30) 
entrada_cidade = tk.Entry(frame_cadastro, width=30)

entrada_nome.grid(row=0, column=1, padx=10, pady=8)
entrada_idade.grid(row=1, column=1, padx=10, pady=8)
entrada_cidade.grid(row=2, column=1, padx=10, pady=8)


def cadastrar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    cidade = entrada_cidade.get()

    if nome == "":
        cadastro.configure(text="⚠️ Digite seu nome!")
    elif idade == "":
        cadastro.configure(text="⚠️ Digite sua idade!")
    elif cidade == "":
        cadastro.configure(text="⚠️ Digite sua Cidade!")
    else: 
        try:
            idade_convertida = int(idade)
            if idade_convertida < 18:
                cadastro.configure(
                text=f"Olá {nome}\nVocê tem {idade_convertida} anos\nMora em {cidade}\nVocê é menor de idade."
        )
            else:
                cadastro.configure(
            text=f"Olá {nome}\nVocê tem {idade_convertida} anos\nMora em {cidade}\nVocê é maior de idade."
        )
            insert(nome=nome, idade_convertida=idade_convertida, cidade=cidade)
        except ValueError:
            cadastro.configure(
            text="⚠️ A idade precisa ser um número!"
            )


        
    
#Botão Cadastrar
botao_cadastro = tk.Button(
    frame_cadastro, 
    text="Cadastro",
    command=cadastrar
)
botao_cadastro.grid(row=3, column=0, columnspan=2, pady=15)

#Exibir

cadastro = tk.Label(
    janela,
    text="",
)
cadastro.grid(row=3, column=2, columnspan=3, pady=10)

#Limpando

def limpar():
     entrada_nome.delete(0, tk.END)
     entrada_idade.delete(0, tk.END)
     entrada_cidade.delete(0, tk.END)

     cadastro.configure(text="Tela Limpa")
     lista.delete(0, tk.END)

limpa = tk.Button(
    frame_busca,
    text="🗑️ Limpar",
    command=limpar

)
limpa.grid(row=2, column=0)

#buscar Users

def exibir_user():
     usuarios = buscar_user()
     lista.delete(0, tk.END)

     for usuarios in usuarios:
            lista.insert(tk.END, usuarios)
            cadastro.configure(
                text="Usuários Listados"
            )
            

buscar = tk.Button(
     frame_busca,
     text="Buscar Usuário",
     command=exibir_user
)
buscar.grid(row=0, column=0, pady=10, padx=10)

lista = tk.Listbox(frame_busca)
lista.grid(row=1, column=0)

entrada_id = tk.Entry(frame_excluir,width=30)
entrada_id.grid (row=0, column=1, pady=10, padx=10)


#Excluir Users

def excluir_user():
    id_recebido = entrada_id.get()

    if id_recebido == "":
        cadastro.configure(
            text="O Campo Não pode ficar vazio"
        )
    else:
        try:
            id_convert = int(id_recebido)
            deletar_user(id_convert)
            cadastro.configure(
                text="Usuario Removido"
            )
        except ValueError:
            cadastro.configure(
                text="Digite um ID valido"
            )
        
excluir = tk.Button(
    frame_excluir,
    text="Excluir User",
    command=excluir_user
)
excluir.grid (row=1, column=0, columnspan=2, padx=10, pady=10)

#Atualizando Users

def atualizar_user1():
    id_alterar = id_alterado.get()
    nome_alterar = nome_alterado.get()
    idade_alterar = idade_alterado.get()

    id_alterar = int(id_alterado.get())
    idade_alterar = int(idade_alterado.get())

    atualizar_user(id_alterar, nome_alterar, idade_alterar)
    cadastro.configure(
        text="Usuário atualizado com sucesso!"
    )


id_alterado = tk.Entry(frame_alterar)
nome_alterado = tk.Entry(frame_alterar)
idade_alterado = tk.Entry(frame_alterar)

id_alterado.grid(row=0, column=1, padx=10, pady=8)
nome_alterado.grid(row=1, column=1, padx=10, pady=8)
idade_alterado.grid(row=2, column=1, padx=10, pady=8)

id_atulizar = tk.Label(
    frame_alterar,
    text="ID Alterado:",
    font=("Arial", 10)
)

nome_atualizar = tk.Label(
    frame_alterar,
    text="Nome Alterado:",
    font=("Arial", 10)
)

idade_atualizar = tk.Label(
    frame_alterar,
    text="Idade Alterada:",
    font=("Arial", 10)
)

id_atulizar.grid(row=0, column=0)
nome_atualizar.grid(row=1, column=0)
idade_atualizar.grid(row=2, column=0)

editar = tk.Button(
    frame_alterar, 
    text="Alterar campos",
    command=atualizar_user1
)
editar.grid(row=3, column=1, columnspan=2)

entrada_pesquisa = tk.Entry(frame_pesquisar)
entrada_pesquisa.grid(
    row=1,
    column=0
)

def pesquisar_cidade1():
    cidade_pesquisa = entrada_pesquisa.get()

    usuarios = pesquisar_cidade(cidade_pesquisa)
    for usuarios in usuarios:
        lista.insert(tk.END, usuarios)

    cadastro.configure(
        text="Usuários Listado p/ Cidade"
    )
    
    
    
pesquisar_botao = tk.Button(frame_pesquisar, text="Pesquisar", command=pesquisar_cidade1)
pesquisar_botao.grid(row=2, column=0, columnspan=2)

janela.mainloop()