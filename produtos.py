import tkinter as tk
from tkinter import ttk, messagebox

# Lista de produtos
produtos = []

# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = entry_nome.get()
    descricao = entry_descricao.get()
    valor = entry_valor.get()
    disponivel = var_disponivel.get()

    if nome and valor:
        # Substitui a vírgula por ponto para garantir que seja um valor válido em ponto flutuante
        valor = valor.replace(",", ".")

        produtos.append({"Nome": nome, "Descrição": descricao, "Valor": float(valor), "Disponível": disponivel})
        limpar_campos()
        atualizar_listagem()
    else:
        messagebox.showerror("Erro", "Por favor, preencha o nome e o valor do produto.")

# Função para limpar os campos do formulário
def limpar_campos():
    entry_nome.delete(0, tk.END)
    entry_descricao.delete(0, tk.END)
    entry_valor.delete(0, tk.END)
    var_disponivel.set(0)

# Função para atualizar a listagem de produtos
def atualizar_listagem():
    listbox.delete(0, tk.END)
    produtos.sort(key=lambda x: x["Valor"])
    for produto in produtos:
        listbox.insert(tk.END, "{} - R${:.2f}".format(produto['Nome'], produto['Valor']))

# Configuração da janela principal
root = tk.Tk()
root.title("Cadastro e Listagem de Produtos")
root.geometry("400x250")

# Abas
aba_control = ttk.Notebook(root)
aba_cadastro = ttk.Frame(aba_control)
aba_listagem = ttk.Frame(aba_control)
aba_control.add(aba_cadastro, text="Cadastro")
aba_control.add(aba_listagem, text="Listagem")
aba_control.pack(fill="both", expand=True)

# Formulário de cadastro
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

botao_cadastrar = tk.Button(aba_cadastro, text="Cadastrar", command=cadastrar_produto)
botao_cadastrar.pack()

# Listagem de produtos
listbox = tk.Listbox(aba_listagem)
listbox.pack(fill="both", expand=True)

botao_novo = tk.Button(aba_listagem, text="Novo Produto", command=lambda: aba_control.select(aba_cadastro))
botao_novo.pack()

root.mainloop()
