import tkinter as tk
from tela_principal import TelaPrincipal

# Cria a janela principal
janela = tk.Tk()
janela.title("Meu Sistema")
janela.geometry("800x800")

# Cria a tela principal
tela_principal = TelaPrincipal(janela)

janela.mainloop()
