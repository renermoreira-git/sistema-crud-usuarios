from tkinter import ttk


def configurar_estilos(janela):
    fundo = "#F1F5F9"
    principal = "#0F172A"
    destaque =  "#25BDEB"
    branco = "#FFFFFF"
    sucesso = "#16A34A"
    erro = "#DC2626"

    style = ttk.Style(janela)

    #Style do Botão

    style.configure(
        "Botao.TButton",
        font=("Arial", 10, "bold"),
        padding=5,
        foreground = branco, 
        background = principal
    )

    style.configure(
        "Texto.TLabel",
        font=("Roman", 10, "bold")
    )

    style.map(
        "Botao.TButton",
        background = [
            ("active", destaque)
        ]
    )

    style.configure(
        "Entrada.TEntry",
        font=("Roman", 10),
        paadiing = 5
    )

    

    
    return style