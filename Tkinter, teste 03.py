# importando o módulo tkinter
import tkinter as tk

# criando a janela
janela = tk.Tk()

# adicionando o título na janela
janela.title("Cadastro de Produtos")

# criando os labels e campos para nome, marca, quantidade e valor
nome_label = tk.Label(janela, text="Nome", width=15, anchor="w")
nome_label.grid(row=0, column=0)
nome_entry = tk.Entry(janela)
nome_entry.grid(row=0, column=1)

marca_label = tk.Label(janela, text="Marca", width=15, anchor="w")
marca_label.grid(row=1, column=0)
marca_entry = tk.Entry(janela)
marca_entry.grid(row=1, column=1)

quantidade_label = tk.Label(janela, text="Quantidade", width=15, anchor="w")
quantidade_label.grid(row=2, column=0)
quantidade_entry = tk.Entry(janela)
quantidade_entry.grid(row=2, column=1)

valor_label = tk.Label(janela, text="Valor (R$)", width=15, anchor="w")
valor_label.grid(row=3, column=0)
valor_entry = tk.Entry(janela)
valor_entry.grid(row=3, column=1)

# criando o botão para cadastrar os produtos
def cadastrar_produto():
    nome = nome_entry.get()
    marca = marca_entry.get()
    quantidade = quantidade_entry.get()
    valor = valor_entry.get()
    produtos_listbox.insert(tk.END, f"{nome:<20} {marca:<20} {quantidade:<10} R${valor:>8}")
    
    # limpando os campos de entrada após a adição do produto
    nome_entry.delete(0, tk.END)
    marca_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    valor_entry.delete(0, tk.END)

cadastrar_button = tk.Button(janela, text="Cadastrar Produto", command=cadastrar_produto, bg="lightblue", fg="white", width=25)
cadastrar_button.grid(row=4, column=0, columnspan=2)

# adicionando o Listbox para exibir os produtos cadastrados
produtos_listbox = tk.Listbox(janela, width=70)
produtos_listbox.grid(row=5, column=0, columnspan=2)

# criando o botão para excluir produtos da lista
def excluir_produto():
    # verificando se algum item da lista foi selecionado
    if produtos_listbox.curselection():
        produtos_listbox.delete(produtos_listbox.curselection())

excluir_button = tk.Button(janela, text="Excluir Produto", command=excluir_produto, bg="red", fg="white", width=25)
excluir_button.grid(row=6, column=0, columnspan=2)

# rodando a janela
janela.mainloop()
