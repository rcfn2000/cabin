import tkinter as tk
from tkinter import font
import qrcode
from io import BytesIO
from tkinter import messagebox
from PIL import Image, ImageTk
from shipay_integration import generate_qr_code  # Import the generate_qr_code function


class TelaFormasPagamento:
    def __init__(self, janela, valor):
        self.janela = janela
        self.valor = valor

        # Define a imagem de fundo
        self.imagem_fundo = tk.PhotoImage(file="imagem_de_fundo.png")
        self.fundo = tk.Label(self.janela, image=self.imagem_fundo)
        self.fundo.place(x=0, y=0, relwidth=1, relheight=1)

        # Define a fonte para a saudação
        self.fonte = tk.font.Font(family="Poppins", size=24)

        # Saudação
        self.saudacao = tk.Label(
            self.janela,
            text=f"Escolha a forma de pagamento para R$ {self.valor}",
            font=self.fonte,
            fg="purple",
        )
        self.saudacao.place(relx=0.5, rely=0.1, anchor="center")

        # Botões
        self.botao_cartao = tk.Button(
            self.janela,
            text="Crédito/Débito",
            font=self.fonte,
            fg="black",
            command=self.pagar_com_cartao,
        )
        self.botao_cartao.place(relx=0.25, rely=0.5, anchor="center")

        self.botao_pix = tk.Button(
            self.janela,
            text="Pix",
            font=self.fonte,
            fg="black",
            command=self.pagar_com_pix,
        )
        self.botao_pix.place(relx=0.75, rely=0.5, anchor="center")

        # Widget para exibir o QR Code
        self.qr_code = tk.Label(self.janela)
        self.qr_code.place(relx=0.5, rely=0.5, anchor="center")

    def pagar_com_cartao(self):
        # lógica para pagar com cartão
        pass

    def pagar_com_pix(self):
        # Gera o QR Code usando a função generate_qr_code()
        qr_img = generate_qr_code()

        if qr_img:
            # Converte a imagem do QR Code em PhotoImage para exibir no tkinter
            qr_img = qr_img.resize((250, 250), Image.ANTIALIAS)
            qr_photo = ImageTk.PhotoImage(qr_img)

            # Exibe o QR Code no widget
            self.qr_code.config(image=qr_photo)
            self.qr_code.image = qr_photo
        else:
            messagebox.showerror("Erro", "Não foi possível gerar o QR Code.")
