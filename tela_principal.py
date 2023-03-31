import tkinter as tk
from tkinter import font
from tela_formas_pagamento import TelaFormasPagamento


class TelaPrincipal:
    def __init__(self, janela):
        self.janela = janela

        # Define a imagem de fundo
        self.imagem_fundo = tk.PhotoImage(file="imagem_de_fundo.png")
        self.fundo = tk.Label(self.janela, image=self.imagem_fundo)
        self.fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Define a fonte para a saudação
        self.fonte = tk.font.Font(family="Poppins", size=34)

        # Saudação
        self.saudacao = tk.Label(
            self.janela, text="Bem-vindo PAI VEI!", font=self.fonte, fg="purple"
        )
        self.saudacao.place(relx=0.5, rely=0.1, anchor="center")

        # Botões
        self.botao_10_reais = tk.Button(
            self.janela,
            text="R$ 10",
            font=self.fonte,
            fg="black",
            command=lambda: self.abrir_tela_formas_pagamento(10),
        )
        self.botao_10_reais.place(relx=0.25, rely=0.8, anchor="center")

        self.botao_15_reais = tk.Button(
            self.janela,
            text="R$ 15",
            font=self.fonte,
            fg="black",
            command=lambda: self.abrir_tela_formas_pagamento(15),
        )
        self.botao_15_reais.place(relx=0.75, rely=0.8, anchor="center")

    def abrir_tela_formas_pagamento(self, valor):
        # Cria a tela de formas de pagamento
        self.tela_formas_pagamento = TelaFormasPagamento(self.janela, valor)

        # Remove os widgets da tela principal
        self.saudacao.destroy()
        self.botao_10_reais.destroy()
        self.botao_15_reais.destroy()

        # Exibe os widgets da tela de formas de pagamento
        self.tela_formas_pagamento.saudacao.pack()
        self.tela_formas_pagamento.botao_cartao.pack()
        self.tela_formas_pagamento.botao_pix.pack()
