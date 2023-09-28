import tkinter as tk
from tkinter import messagebox, ttk

produtos = []

def cadastrar_produto():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()
    disponivel = var_disponivel.get()

    if nome and valor:
        produtos.append({"Nome": nome, "Descrição": descricao, "Valor": valor, "Disponível": disponivel})
        limpar_campos()
        atualizar_listagem()
    else:
        messagebox.showerror("Erro", "Por favor, preencha o nome e o valor do produto.")

def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    var_disponivel.set(0)

def atualizar_listagem():
    listbox.delete(0, tk.END)
    produtos.sort(key=lambda x: x["Valor"])
    for produto in produtos:
        listbox.insert(tk.END, f"{produto['Nome']} - R${produto['Valor']:.2f}")

def cadastrar_e_listar():
    cadastrar_produto()
    aba_control.hide(aba_cadastro)
    aba_control.select(aba_listagem)

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro e Listagem de Produtos")

# Janela de cadastro
aba_cadastro = tk.Frame(root)
aba_cadastro.pack(fill="both", expand=True)

label_nome = tk.Label(aba_cadastro, text="Nome do Produto:")
label_nome.pack()
entry_nome = tk.Entry(aba_cadastro)
entry_nome.pack()

label_descricao = tk.Label(aba_cadastro, text="Descrição do Produto:")
label_descricao.pack()
entry_descricao = tk.Entry(aba_cadastro)
entry_descricao.pack()

label_valor = tk.Label(aba_cadastro, text="Valor do Produto:")
label_valor.pack()
entry_valor = tk.Entry(aba_cadastro)
entry_valor.pack()

label_disponivel = tk.Label(aba_cadastro, text="Disponível para Venda:")
label_disponivel.pack()
var_disponivel = tk.StringVar(value="Sim")
radio_sim = tk.Radiobutton(aba_cadastro, text="Sim", variable=var_disponivel, value="Sim")
radio_nao = tk.Radiobutton(aba_cadastro, text="Não", variable=var_disponivel, value="Não")
radio_sim.pack()
radio_nao.pack()

botao_cadastrar = tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar_e_listar)
botao_cadastrar.pack()

# Janela de listagem
aba_listagem = tk.Frame(root)
aba_listagem.pack(fill="both", expand=True)

listbox = tk.Listbox(aba_listagem)
listbox.pack(fill="both", expand=True)

botao_novo = tk.Button(aba_listagem, text="Novo Produto", command=lambda: aba_control.forget(aba_listagem) or aba_control.select(aba_cadastro))
botao_novo.pack()

aba_control = ttk.Notebook(root)
aba_control.add(aba_cadastro, text="Cadastro")
aba_control.add(aba_listagem, text="Listagem")
aba_control.pack(fill="both", expand=True)

root.mainloop()