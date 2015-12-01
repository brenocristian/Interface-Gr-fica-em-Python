from tkinter import *

janelaVendedor = Tk()
janelaVendedor.geometry("500x200")
janelaVendedor.title("Vendedor")
janelaVendedor.configure(background='light blue')  

barraMenu = Menu(janelaVendedor)
janelaVendedor.config(menu = barraMenu)
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
barraMenu.add_cascade(label="Pesquisar",menu=subMenu3)
subMenu3.add_command(label="Cód.Vendedor")
subMenu3.add_command(label="Nome do Vendedor")
subMenu3.add_command(label="Por Data de Admissão")
subMenu3.add_command(label="Telefone")
subMenu3.add_command(label="Endereço")
subMenu3.add_command(label="CPF")
subMenu3.add_command(label="RG")

frameCampos = Frame(janelaVendedor,background='light blue')

separator1 = Frame(janelaVendedor,height=2, bd=1, relief=RAISED)
separator2 = Frame(janelaVendedor,height=2, bd=1, relief=RAISED)

labelTitulo = Label(text = "REGISTRO DE VENDEDORES",background='light blue')

labelCód = Label(frameCampos,text = "Código do Vendedor:",background='light blue')
entryCód = Entry(frameCampos,width=7)
labelCód.grid(column=0, row=0)
entryCód.grid(columnspan=5,column=1,row=0,sticky=W)

labelNome = Label(frameCampos, text = "Nome do Vendedor:",background='light blue')
entryNome = Entry(frameCampos,width=35)
labelNome.grid(column=0, row=1,sticky=E)
entryNome.grid(column=1,row=1,sticky=W)

labelData = Label(frameCampos, text = "Data de Admissão:",background='light blue')
entryData = Entry(frameCampos, width=11)
labelData.grid(column=0, row=2,sticky=E)
entryData.grid(column=1,row=2,sticky=W)

labelTelefone = Label(frameCampos,text = "Telefone:",background='light blue')
entryTelefone = Entry(frameCampos,width=18)
labelTelefone.grid(column = 0, row=3,sticky=E)
entryTelefone.grid(column = 1, row=3,sticky=W)

labelEndereço = Label(frameCampos,text = "Endereço:",background='light blue')
entryEndereço = Entry(frameCampos,width=26)
labelEndereço.grid(column = 0, row=3,sticky=E)
entryEndereço.grid(column = 1, row=3,sticky=W)

labelNum = Label(frameCampos,text = "Nº:",background='light blue')
entryNum = Entry(frameCampos,width=6)
labelNum.grid(column = 2, row=3,sticky=E)
entryNum.grid(column = 3, row=3,sticky=W)

labelCPF = Label(frameCampos,text = "CPF:",background='light blue')
entryCPF = Entry(frameCampos,width=17)
labelCPF.grid(column=2, row =4,sticky=E)
entryCPF.grid(column=3, row =4,sticky=W)

labelRG = Label(frameCampos,text="RG:",background='light blue')
entryRG = Entry(frameCampos,width=25)
labelRG.grid(column=0, row =4,sticky=E)
entryRG.grid(column=1, row =4,sticky=W)

botNovo = Button(text = "Novo",background='light green')
botRegistrar = Button(text = "Registrar",background='light green')
botAlterar = Button(text = "Alterar",background='light green')
botExcluir = Button(text = "Excluir",background='red')

labelTitulo.pack()
separator1.pack(fill=X, padx=5, pady=5)
frameCampos.pack()

separator2.pack(fill=X, padx=5, pady=5)
botNovo.pack(side = LEFT,padx = 10)
botRegistrar.pack(side = LEFT,padx = 10)
botAlterar.pack(side = LEFT,padx = 10)
botExcluir.pack(side = LEFT,padx = 10)

janelaVendedor.mainloop
