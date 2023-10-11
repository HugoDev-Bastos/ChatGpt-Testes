import tkinter as tk

def cadastrar_produto():
    # obtém os valores dos campos
    nome = nome_entry.get()
    marca = marca_entry.get()
    quantidade = quantidade_entry.get()
    valor = valor_entry.get()

    # exibe as informações do produto cadastrado
    print("Produto cadastrado:")
    print("Nome:", nome)
    print("Marca:", marca)
    print("Quantidade:", quantidade)
    print("Valor:", valor)

# cria a janela principal
janela = tk.Tk()
janela.title("Cadastro de Produtos")

# cria um frame para os campos de entrada
formulario_frame = tk.Frame(janela, pady=10, padx=10)
formulario_frame.pack()

# cria os campos para nome, marca, quantidade e valor
nome_label = tk.Label(formulario_frame, text="Nome:", font=("Arial", 14))
nome_label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
nome_entry = tk.Entry(formulario_frame, font=("Arial", 14))
nome_entry.grid(row=0, column=1, padx=5, pady=5)

marca_label = tk.Label(formulario_frame, text="Marca:", font=("Arial", 14))
marca_label.grid(row=1, column=0, sticky="w", padx=5, pady=5)
marca_entry = tk.Entry(formulario_frame, font=("Arial", 14))
marca_entry.grid(row=1, column=1, padx=5, pady=5)

quantidade_label = tk.Label(formulario_frame, text="Quantidade:", font=("Arial", 14))
quantidade_label.grid(row=2, column=0, sticky="w", padx=5, pady=5)
quantidade_entry = tk.Entry(formulario_frame, font=("Arial", 14))
quantidade_entry.grid(row=2, column=1, padx=5, pady=5)

valor_label = tk.Label(formulario_frame, text="Valor:", font=("Arial", 14))
valor_label.grid(row=3, column=0, sticky="w", padx=5, pady=5)
valor_entry = tk.Entry(formulario_frame, font=("Arial", 14))
valor_entry.grid(row=3, column=1, padx=5, pady=5)

# cria um botão para cadastrar o produto
cadastrar_button = tk.Button(janela, text="Cadastrar Produto", font=("Arial", 14), bg="green", fg="white", command=cadastrar_produto)
cadastrar_button.pack(pady=10)

# inicia o loop principal da janela
janela.mainloop()
