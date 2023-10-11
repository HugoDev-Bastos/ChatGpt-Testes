import tkinter as tk
from tkinter import messagebox

class JogoDaVelha:
    def __init__(self, master):
        self.master = master
        master.title("Jogo da Velha")
        self.turno = "X"
        self.tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        
        # Frames
        tabuleiro_frame = tk.Frame(master)
        tabuleiro_frame.pack(pady=10)
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        # Botões do tabuleiro
        self.botoes = []
        for i in range(9):
            button = tk.Button(tabuleiro_frame, text=" ", font=("Arial", 24), width=4, height=2, command=lambda i=i: self.marcar(i))
            button.grid(row=i//3, column=i%3)
            self.botoes.append(button)

        # Botão para reiniciar o jogo
        restart_button = tk.Button(button_frame, text="Reiniciar", font=("Arial", 14), command=self.reiniciar)
        restart_button.pack(pady=10)

    def marcar(self, i):
        if self.tabuleiro[i] == " ":
            self.tabuleiro[i] = self.turno
            self.botoes[i].configure(text=self.turno)
            if self.verificar_vencedor():
                messagebox.showinfo("Fim do jogo", f"O jogador {self.turno} venceu!")
                self.reiniciar()
            elif " " not in self.tabuleiro:
                messagebox.showinfo("Fim do jogo", "Empate!")
                self.reiniciar()
            else:
                self.turno = "O" if self.turno == "X" else "X"

    def verificar_vencedor(self):
        for i in range(3):
            if self.tabuleiro[i*3] == self.tabuleiro[i*3+1] == self.tabuleiro[i*3+2] != " ":
                return True
            if self.tabuleiro[i] == self.tabuleiro[i+3] == self.tabuleiro[i+6] != " ":
                return True
        if self.tabuleiro[0] == self.tabuleiro[4] == self.tabuleiro[8] != " ":
            return True
        if self.tabuleiro[2] == self.tabuleiro[4] == self.tabuleiro[6] != " ":
            return True
        return False

    def reiniciar(self):
        self.turno = "X"
        self.tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
        for i in range(9):
            self.botoes[i].configure(text=" ")

if __name__ == "__main__":
    root = tk.Tk()
    app = JogoDaVelha(root)
    root.mainloop()
