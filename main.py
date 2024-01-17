import tkinter as tk
import sqlite3
from cadastro_estudante import cad_estudante 
from estudantes_cadastrados import estudante_cad
from gerar_carteira import gerar_cart

# Funções 
def fechar_janela(): 
  root.destroy()

def cadastrar_est():
  cad_estudante()

def estudantes_cad():
  estudante_cad()

def gerar_carte():
  gerar_cart()

def testando(): 
  pass
  
# INTERFACE PRINCIPAL 
root = tk.Tk()
root.title("Menu")
root.geometry("375x180")

botao1 = tk.Button(root, text="Cadastrar Estudante", command=cadastrar_est)
botao1.pack()
botao1.place(x=15, y=20, height=30, width=150)

botao2 = tk.Button(root, text="Estudantes cadastrados", command=estudantes_cad)
botao2.pack()
botao2.place(x=175, y=20, height=30, width=160)


botao3 = tk.Button(root, text="Carteira Estudante", command=gerar_carte)
botao3.pack()
botao3.place(x=15, y=60, height=30, width=150)

botao4 = tk.Button(root, text="Area de teste", command=testando)
botao4.pack()
botao4.place(x=175, y=60, height=30, width=160)

fechar_button = tk.Button(root, text="Fechar", background="red" ,command=fechar_janela)
fechar_button.pack()
fechar_button.place(x=265, y=120)


root.mainloop()
