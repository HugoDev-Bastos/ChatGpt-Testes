import tkinter as tk

class Produto:
    def __init__(self, nome, marca, quantidade, valor):
        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade
        self.valor = valor

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Produtos")

        # Labels
        self.nome_label = tk.Label(master, text="Nome")
        self.marca_label = tk.Label(master, text="Marca")
        self.quantidade_label = tk.Label(master, text="Quantidade")
        self.valor_label = tk.Label(master, text="Valor")

        # Entradas de texto
        self.nome_entry = tk.Entry(master)
        self.marca_entry = tk.Entry(master)
        self.quantidade_entry = tk.Entry(master)
        self.valor_entry = tk.Entry(master)

        # Botões
        self.cadastrar_button = tk.Button(master, text="Cadastrar", command=self.cadastrar_produto)
        self.alterar_button = tk.Button(master, text="Alterar", command=self.alterar_produto)
        self.deletar_button = tk.Button(master, text="Deletar", command=self.deletar_produto)

        # ListBox
        self.lista_produtos = tk.Listbox(master)

        # Posicionamento dos widgets na janela
        self.nome_label.grid(row=0, column=0)
        self.marca_label.grid(row=1, column=0)
        self.quantidade_label.grid(row=2, column=0)
        self.valor_label.grid(row=3, column=0)

        self.nome_entry.grid(row=0, column=1)
        self.marca_entry.grid(row=1, column=1)
        self.quantidade_entry.grid(row=2, column=1)
        self.valor_entry.grid(row=3, column=1)

        self.cadastrar_button.grid(row=4, column=0)
        self.alterar_button.grid(row=4, column=1)
        self.deletar_button.grid(row=4, column=2)

        self.lista_produtos.grid(row=5, columnspan=3)

    def cadastrar_produto(self):
        produto = Produto(self.nome_entry.get(), self.marca_entry.get(), int(self.quantidade_entry.get()), float(self.valor_entry.get()))
        self.lista_produtos.insert(tk.END, f"{produto.nome} - {produto.marca} - {produto.quantidade} - R${produto.valor:.2f}")

    def alterar_produto(self):
        if self.lista_produtos.curselection():
            index = self.lista_produtos.curselection()[0]
            produto = Produto(self.nome_entry.get(), self.marca_entry.get(), int(self.quantidade_entry.get()), float(self.valor_entry.get()))
            self.lista_produtos.delete(index)
            self.lista_produtos.insert(index, f"{produto.nome} - {produto.marca} - {produto.quantidade} - R${produto.valor:.2f}")

    def deletar_produto(self):
        if self.lista_produtos.curselection():
            self.lista_produtos.delete(self.lista_produtos.curselection())

root = tk.Tk()
tela_cadastro = TelaCadastro(root)
root.mainloop()
