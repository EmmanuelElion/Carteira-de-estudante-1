def cad_estudante(): 
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from tkcalendar import DateEntry

  # Conecta ao banco de dados SQLite
  conn = sqlite3.connect('banco_dados/banco_carteirinhas.db')
  cursor = conn.cursor()

  # Cria a tabela se ela não existir
  cursor.execute('''
  CREATE TABLE IF NOT EXISTS alunos(
    nome TEXT,
    cpf INT,
    data DATE,
    matricula INT,
    unidade TEXT,
    acesso INT,  
    curso TEXT
    )
  ''')

  window = tk.Tk()
  window.title("Cadastro Carteirinha")
  window.geometry("500x350")

  # Criação do input de nome
  nome_label = tk.Label(window, text="Nome:")
  nome_label.pack()
  nome_entry = tk.Entry(window)
  nome_entry.pack()

  # Criação do input de CPF
  cpf_label = tk.Label(window, text="CPF:")
  cpf_label.pack()
  cpf_entry = tk.Entry(window)
  cpf_entry.pack()

  # Criação do input de data de vencimento
  data_label = tk.Label(window, text="Data Vencimento:")
  data_label.pack()
  data_entry = DateEntry(window)
  data_entry.pack()

  # Criação do input de Unidade
  unidade_label = tk.Label(window, text="Unidade:")
  unidade_label.pack()
  unidade_entry = tk.Entry(window)
  unidade_entry.pack()

  # Criação do input de Curso
  curso_label = tk.Label(window, text="Curso:")
  curso_label.pack()
  curso_entry = tk.Entry(window)
  curso_entry.pack()

  # Criação do label de status
  status_label = tk.Label(window, text="")
  status_label.pack()

  # Botão para salvar os dados no banco de dados
  def salvar_dados():
    cpf = cpf_entry.get()
    if len(cpf) != 11:
      status_label.config(text="CPF deve ter 11 dígitos.")
      return
    acesso = cpf[:3]
    matricula = cpf[3:6]
    cursor.execute('''
        INSERT INTO alunos VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (nome_entry.get(), cpf, data_entry.get(), matricula, unidade_entry.get(), acesso, curso_entry.get()))
    conn.commit()
    status_label.config(text="Informações enviadas com sucesso para o banco de dados.")
    # Limpa todos os campos de entrada
    nome_entry.delete(0, 'end')
    cpf_entry.delete(0, 'end')
    data_entry.delete(0, 'end')
    unidade_entry.delete(0, 'end')
    curso_entry.delete(0, 'end')

  salvar_button = tk.Button(window, text="Salvar", command=salvar_dados)
  salvar_button.pack()

  # Criando botão para fechar janela 
  def fechar_janela():
    window.destroy()

  fechar_button = tk.Button(window, text="Fechar", command=fechar_janela)
  fechar_button.pack()

  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()


if __name__ == "__main__":
  # Este código só será executado se cadastrar_valores.py for executado diretament
  cad_estudante()
