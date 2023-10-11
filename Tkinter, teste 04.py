import tkinter as tk

class Produto:
    def __init__(self, nome, marca, quantidade):
        self.nome = nome
        self.marca = marca
        self.quantidade = quantidade

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Produtos")
        master.geometry("600x400")

        # Frames
        input_frame = tk.Frame(master)
        input_frame.pack(pady=20)
        button_frame = tk.Frame(master)
        button_frame.pack(pady=20)
        list_frame = tk.Frame(master)
        list_frame.pack(fill=tk.BOTH, expand=True)

        # Labels
        nome_label = tk.Label(input_frame, text="Nome", font=("Arial", 14))
        nome_label.grid(row=0, column=0, padx=10, pady=10)
        marca_label = tk.Label(input_frame, text="Marca", font=("Arial", 14))
        marca_label.grid(row=1, column=0, padx=10, pady=10)
        quantidade_label = tk.Label(input_frame, text="Quantidade", font=("Arial", 14))
        quantidade_label.grid(row=2, column=0, padx=10, pady=10)

        # Entradas de texto
        self.nome_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)
        self.marca_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.marca_entry.grid(row=1, column=1, padx=10, pady=10)
        self.quantidade_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.quantidade_entry.grid(row=2, column=1, padx=10, pady=10)

        # Botões
        cadastrar_button = tk.Button(button_frame, text="Cadastrar", font=("Arial", 14), command=self.cadastrar_produto)
        cadastrar_button.pack(side=tk.LEFT, padx=10, pady=10)
        alterar_button = tk.Button(button_frame, text="Alterar", font=("Arial", 14), command=self.alterar_produto)
        alterar_button.pack(side=tk.LEFT, padx=10, pady=10)
        deletar_button = tk.Button(button_frame, text="Deletar", font=("Arial", 14), command=self.deletar_produto)
        deletar_button.pack(side=tk.LEFT, padx=10, pady=10)

        # ListBox
        self.lista_produtos = tk.Listbox(list_frame, font=("Arial", 14))
        self.lista_produtos.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def cadastrar_produto(self):
        nome = self.nome_entry.get()
        marca = self.marca_entry.get()
        quantidade = self.quantidade_entry.get()
        produto = Produto(nome, marca, quantidade)
        self.lista_produtos.insert(tk.END, produto.nome)

    def alterar_produto(self):
        # TODO: implementar
        pass

    def deletar_produto(self):
        selection = self.lista_produtos.curselection()
        if len(selection) > 0:
            self.lista_produtos.delete(selection[0])

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastro(root)
    root.mainloop()
