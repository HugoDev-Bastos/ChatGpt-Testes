import tkinter as tk

class Cronometro:
    def __init__(self, janela):
        self.janela = janela
        self.tempo = 0
        self.lbl_tempo = tk.Label(self.janela, text="00:00:00", font=("Arial", 36))
        self.lbl_tempo.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
        self.btn_iniciar = tk.Button(self.janela, text="Iniciar", font=("Arial", 16), width=8, command=self.iniciar_cronometro)
        self.btn_iniciar.grid(row=1, column=0, padx=5, pady=5)
        self.btn_parar = tk.Button(self.janela, text="Parar", font=("Arial", 16), width=8, command=self.parar_cronometro)
        self.btn_parar.grid(row=1, column=1, padx=5, pady=5)
        self.btn_reset = tk.Button(self.janela, text="Reset", font=("Arial", 16), width=8, command=self.reset_cronometro)
        self.btn_reset.grid(row=1, column=2, padx=5, pady=5)
        self.executando = False
        
    def iniciar_cronometro(self):
        self.executando = True
        self.contar_tempo()
        
    def parar_cronometro(self):
        self.executando = False
        
    def reset_cronometro(self):
        self.tempo = 0
        self.lbl_tempo.config(text="00:00:00")
        
    def contar_tempo(self):
        if self.executando:
            self.tempo += 1
            minutos = self.tempo // 60
            segundos = self.tempo % 60
            horas = minutos // 60
            minutos = minutos % 60
            tempo_formatado = "{:02d}:{:02d}:{:02d}".format(horas, minutos, segundos)
            self.lbl_tempo.config(text=tempo_formatado)
            self.janela.after(1000, self.contar_tempo)

janela = tk.Tk()
janela.title("Cronômetro")
janela.geometry("400x150")
janela.resizable(False, False)
janela.configure(bg='#F8F8FF')
cronometro = Cronometro(janela)
janela.mainloop()
