import customtkinter as ctk
from customtkinter import filedialog
import PyPDF2


# Criando a função que vai rodar quando clicar no botao

def abrir_arquivo():
    nome_arquivo = filedialog.askopenfilename(title='Abrir Arquivo PDF', filetypes=[('Arquivos PDF', '*.pdf')])   # Faz com que somente arquivos PDF possam ser selecionados
    lbl_nomearquivo.configure(text=nome_arquivo)    # Muda o nome do arquivo para o arquivo que o usuario abrir
    texto_saida.delete('1.0', ctk.END)  # Deleta qualquer texto que já estava na tela
    leitor_pdf = PyPDF2.PdfReader(nome_arquivo)

    for i in range(len(leitor_pdf.pages)):
        texto = leitor_pdf.pages[i].extract_text()
        texto_saida.insert(ctk.END, texto)


ctk.set_appearance_mode('system')   # A cor da janela vai ser a mesma que o usuario selecionou no windows
janela = ctk.CTk()    # Cria a janela
janela.title('Extrator de Texto PDF')   # Muda o título da janela


lbl_nomearquivo = ctk.CTkLabel(master=janela, text='Nenhum Arquivo Selecionado')
lbl_nomearquivo.grid(row=0, column=0, pady=5, padx=10)

texto_saida = ctk.CTkTextbox(janela, width=500, height=500)
texto_saida.grid(row=1, column=0, pady=10, padx=10, sticky=ctk.NSEW)

btn_abrirarquivo = ctk.CTkButton(janela, text='Abrir Arquivo', command=abrir_arquivo, border_color=('white'))
btn_abrirarquivo.grid(row=2, column=0, pady=5)


janela.mainloop()