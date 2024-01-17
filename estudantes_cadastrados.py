def estudante_cad():
  import sqlite3
  import tkinter as tk
  from tkinter import ttk

  # Funções 
  def buscar_dados():
    tipo_busca = var.get()
    valor_busca = campo_busca.get()

    cursor.execute(f"SELECT * FROM alunos WHERE {tipo_busca}=?", (valor_busca,))
    rows = cursor.fetchall()

    for i in tabela.get_children():
        tabela.delete(i)

    for row in rows:
        tabela.insert('', 'end', values=row)

  def carregar_dados():
    cursor.execute("SELECT * FROM alunos")
    rows = cursor.fetchall()

    for i in tabela.get_children():
        tabela.delete(i)

    for row in rows:
        tabela.insert('', 'end', values=row)

  def limpar_dados():
    for i in tabela.get_children():
        tabela.delete(i)
    campo_busca.delete(0, tk.END)

  def fechar_janela():
    window.destroy()

  # Conecta ao banco de dados SQLite
  conn = sqlite3.connect('banco_dados/banco_carteirinhas.db')
  cursor = conn.cursor()

  # Criando interface gráfica
  window = tk.Tk()
  window.title("Informações cadastradas")
  window.geometry("570x300")

  # Adiciona botões de rádio
  var = tk.StringVar(value="nome")
  r1 = tk.Radiobutton(window, text='Nome', variable=var, value='nome')
  r2 = tk.Radiobutton(window, text='CPF', variable=var, value='cpf')
  r1.pack()
  r2.pack()
  r1.place(x=15, y=15)
  r2.place(x=100, y=15)	

  # Adiciona campo de entrada
  campo_busca = tk.Entry(window)
  campo_busca.pack()
  campo_busca.place(x=15, y=40, width=180, height=25)

  # botão de  busca 
  buscar_button = tk.Button(window, text="Buscar", command=buscar_dados)
  buscar_button.pack()
  buscar_button.place(x=200, y=40, width=60 , height=25)

  # Cria um frame com uma borda
  frame = tk.Frame(window, borderwidth=2, relief="groove")
  frame.place(x=15, y=70, width=520, height=200)

  # Tabela para exibir os dados
  colunas = ('Nome', 'CPF','Data', 'Matricula','Unidade','Acesso', 'Curso')
  tabela = ttk.Treeview(
      frame, columns=colunas,
      show='headings')  # Adiciona a tabela ao frame em vez da janela
  for coluna in colunas:
      tabela.heading(coluna, text=coluna)
      tabela.column('Nome')
      tabela.column('CPF')
      tabela.column('Data')
      tabela.column('Matricula')
      tabela.column('Unidade')
      tabela.column('Acesso')
      tabela.column('Curso')
      tabela.pack(fill="both",
                  expand=True)  # Use pack em vez de place para preencher o frame

  # Botão para carregar os dados do banco de dados
  carregar_button = tk.Button(window, text="Carregar", command=carregar_dados)
  carregar_button.pack()
  carregar_button.place(x=15, y=270)

  # Botão para limpar os dados da tabela e o campo de entrada
  limpar_button = tk.Button(window, text="Limpar", command=limpar_dados)
  limpar_button.pack()
  limpar_button.place(x=100, y=270)

  # Criando botão para fechar janela  
  fechar_button = tk.Button(window, text="Fechar", command=fechar_janela)
  fechar_button.pack()
  fechar_button.place(x=466, y=270)

  # aviso de bug 
  label_avisando = tk.Label(window, text="--> Aviso: Pesquisa por CPF em manutenção")
  label_avisando.pack()
  label_avisando.place(x=160, y=15)	
  
  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()
