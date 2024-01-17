def gerar_cart(): 
  import sqlite3
  import tkinter as tk
  from tkinter import ttk
  from reportlab.pdfgen import canvas
  from reportlab.lib.pagesizes import letter

  # Funções 
  def buscar_dados():
    valor_busca = campo_busca.get()

    # A busca é por CPF, tenta converter o valor para um número
    try:
        valor_busca = int(valor_busca)
    except ValueError:
        tk.messagebox.showerror("Erro", "CPF deve ser um número")
        return

    cursor.execute("SELECT * FROM alunos WHERE cpf=?", (valor_busca,))
    rows = cursor.fetchall()

    for i in tabela.get_children():
        tabela.delete(i)

    for row in rows:
      tabela.insert('', 'end', values=row)

    # Habilita o botão "Gerar" se há itens na tabela
    if tabela.get_children():
      gerar_button['state'] = 'normal'
    else:
      gerar_button['state'] = 'disabled'

  def fechar_janela():
      window.destroy()

  def limpar_mensagem_sucesso():
      label_sucesso['text'] = ""

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

  def editando():
    item_selecionado = tabela.selection()[0]  # Pega o item selecionado
    dados = tabela.item(item_selecionado)['values']  # Pega os valores do item

    # Cria um novo PDF
    c = canvas.Canvas(f"pdf_editado/{dados[0]}_carteira_estudante.pdf", pagesize=(3.34*72, 2.12*72))

    # Adiciona a imagem ao PDF
    c.drawImage("pdf_a_editar/fundo_pdf.png", 0, 0, width=3.34*72, height=2.12*72)

    c.setFont("Helvetica", 6)  # Defina o tamanho da fonte aqui

    # Adiciona os dados ao PDF
    #            Nome       CPF         data    Matricula   Unidade     Acesso   Curso
    posicoes = [(12, 49), (86, 63), (86, 80), (88, 116), (88, 135), (88, 98), (12, 33)]
    for i, dado in enumerate(dados):
        x, y = posicoes[i]
        c.drawString(x, y, str(dado))

    # Salva o novo PDF
    c.save()

    # Mostra uma mensagem de sucesso
    label_sucesso['text'] = "PDF gerado com sucesso"

    # Limpa o campo de entrada e a tabela
    campo_busca.delete(0, 'end')
    for i in tabela.get_children():
        tabela.delete(i)

    # Limpa a mensagem de sucesso após 4 segundos
    window.after(4000, limpar_mensagem_sucesso)





  # conectando ao banco de dados
  conn = sqlite3.connect('banco_dados/banco_carteirinhas.db')
  cursor = conn.cursor()

  # interface grafica 
  window = tk.Tk()
  window.title("Informações cadastradas")
  window.geometry("570x320")

  # Adicinando o label e o campo de busca
  cpf_label = tk.Label(window, text="CPF:")
  cpf_label.pack()
  cpf_label.place(x=10, y=10)
  # Adiciona campo de entrada
  campo_busca = tk.Entry(window)
  campo_busca.pack()
  campo_busca.place(x=15, y=30, width=180, height=25)

  # botão de  busca 
  buscar_button = tk.Button(window, text="Buscar", command=buscar_dados)
  buscar_button.pack()
  buscar_button.place(x=200, y=30, width=60 , height=25)

  # Cria um frame com uma borda
  frame = tk.Frame(window, borderwidth=2, relief="groove")
  frame.place(x=15, y=80, width=520, height=200)

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

  # Criando botão para fechar janela  
  fechar_button = tk.Button(window, text="Fechar", command=fechar_janela)
  fechar_button.pack()
  fechar_button.place(x=466, y=285)

  # Adiciona o botão "Gerar"
  gerar_button = tk.Button(window, text="Gerar", command=editando )  # O botão começa desabilitado "state" para modificar se o botão esta habilitado ou n? 
  gerar_button.pack()
  gerar_button.place(x=270, y=30, width=60, height=25)

  # Adiciona um label para a mensagem de sucesso
  label_sucesso = tk.Label(window, text="")
  label_sucesso.pack()
  label_sucesso.place(x=15, y=60)


  # Botão para carregar os dados do banco de dados
  carregar_button = tk.Button(window, text="Carregar", command=carregar_dados)
  carregar_button.pack()
  carregar_button.place(x=15, y=285)

  # adicionando a função do botão "limpar"
  limpar_button = tk.Button(window, text="Limpar", command=limpar_dados)
  limpar_button.pack()
  limpar_button.place(x=100, y=285)


  window.mainloop()

  # Fecha a conexão com o banco de dados
  conn.close()

