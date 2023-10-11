import tkinter as tk

class TelaCadastro:
    def __init__(self, master):
        self.master = master
        master.title("Cadastro de Pontuações")
        master.geometry("400x300")

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
        pontuacao_label = tk.Label(input_frame, text="Pontuação", font=("Arial", 14))
        pontuacao_label.grid(row=1, column=0, padx=10, pady=10)

        # Entradas de texto
        self.nome_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.nome_entry.grid(row=0, column=1, padx=10, pady=10)
        self.pontuacao_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.pontuacao_entry.grid(row=1, column=1, padx=10, pady=10)

        # Botões
        cadastrar_button = tk.Button(button_frame, text="Cadastrar", font=("Arial", 14), command=self.cadastrar_pontuacao)
        cadastrar_button.pack(side=tk.LEFT, padx=10, pady=10)
        limpar_button = tk.Button(button_frame, text="Limpar", font=("Arial", 14), command=self.limpar_campos)
        limpar_button.pack(side=tk.LEFT, padx=10, pady=10)

        # ListBox
        self.lista_pontuacoes = tk.Listbox(list_frame, font=("Arial", 14))
        self.lista_pontuacoes.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    def cadastrar_pontuacao(self):
        nome = self.nome_entry.get()
        pontuacao = self.pontuacao_entry.get()
        self.lista_pontuacoes.insert(tk.END, f"{nome}: {pontuacao}")
        self.limpar_campos()

    def limpar_campos(self):
        self.nome_entry.delete(0, tk.END)
        self.pontuacao_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TelaCadastro(root)
    root.mainloop()
