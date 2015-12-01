from tkinter import *

janelaCliente = Tk()
janelaCliente.geometry("550x200")
janelaCliente.title("Clientes")
janelaCliente.configure(background='light blue') 

barraMenu = Menu(janelaCliente)
janelaCliente.config(menu = barraMenu)
subMenu = Menu(barraMenu)
barraMenu.add_cascade(label="Arquivo",menu=subMenu)
subMenu.add_command(label="Novo")
subMenu.add_command(label="Abrir")
subMenu.add_command(label="Salvar")
subMenu2 = Menu(barraMenu)
barraMenu.add_cascade(label="Editar",menu=subMenu2)
subMenu2.add_command(label="Desfazer")
subMenu2.add_command(label="Refazer")
subMenu3 = Menu(barraMenu)
barraMenu.add_cascade(label="Consultar",menu=subMenu3)
subMenu3.add_command(label="Nome do Cliente")
subMenu3.add_command(label="Telefone")
subMenu3.add_command(label="Endereço")
subMenu3.add_command(label="Bairro")
subMenu3.add_command(label="CPF")

frameCampos = Frame(janelaCliente,background='light blue')

separator1 = Frame(janelaCliente,height=2, bd=1, relief=RAISED)
separator2 = Frame(janelaCliente,height=2, bd=1, relief=RAISED)

labelTitulo = Label(text = "CADASTRO DE CLIENTES",background='light blue')

labelCód = Label(frameCampos,text = "Código do Cliente:",background='light blue')
entryCód = Entry(frameCampos,width=5)

labelNome = Label(frameCampos,text = "Nome do Cliente:",background='light blue')
entryNome = Entry(frameCampos,width=38)

labelEndereço = Label(frameCampos,text = "Endereço:",background='light blue')
entryEndereço = Entry(frameCampos,width=30)

labelCidade = Label(frameCampos,text = "Cidade:",background='light blue')
entryCidade = Entry(frameCampos,width=22)

labelBairro = Label(frameCampos,text = "Bairro:",background='light blue')
entryBairro = Entry(frameCampos,width=15)

labelTelefone = Label(frameCampos,text = "Telefone:",background='light blue')
entryTelefone = Entry(frameCampos,width=15)

labelNum = Label(frameCampos,text = "Nº:",background='light blue')
entryNum = Entry(frameCampos,width=6)

labelCPF = Label(frameCampos,text = "CPF:",background='light blue')
entryCPF = Entry(frameCampos,width=14)

botNovo = Button(text = "Novo",background='light green')
botRegistrar = Button(text = "Cadastrar",background='light green')
botAlterar = Button(text = "Alterar",background='light green')
botExcluir = Button(text = "Excluir",background='red')

labelCód.grid(column=0, row=0)
entryCód.grid(columnspan=5,column=1,row=0,sticky=W)

labelNome.grid(column=0, row=1,sticky=E)
entryNome.grid(column=1,row=1,sticky=W)

labelEndereço.grid(column = 0, row=2,sticky=E)
entryEndereço.grid(column = 1, row=2,sticky=W)

labelCidade.grid(column=0,row=3,sticky=E)
entryCidade.grid(column=1,row=3,sticky=W)

labelBairro.grid(column = 1, row=3,sticky=E)
entryBairro.grid(column = 2, row=3,sticky=W)

labelNum.grid(column = 1, row=2,sticky=E)
entryNum.grid(column = 2, row=2,sticky=W)

labelTelefone.grid(column = 0, row=4,sticky=E)
entryTelefone.grid(column = 1, row=4,sticky=W)

labelCPF.grid(column=0, row =5,sticky=E)
entryCPF.grid(column=1, row =5,sticky=W)

labelTitulo.pack()
separator1.pack(fill=X, padx=5, pady=5)

frameCampos.pack()

separator2.pack(fill=X, padx=5, pady=5)
botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botAlterar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaCliente.mainloop()
