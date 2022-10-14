import requests
from tkinter import *

lista_semana = []
lista_data = []
lista_chance_chuva = []
descricao_lista = []




def pesquisar():

    api_key = "1234"


    url = f"http://apiadvisor.climatempo.com.br/api-manager/user-token/" + str(api_key) + "/locales"
    payload = "localeId[]=3907"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    requisicao = requests.put(url, headers=headers, data=payload)

    url2 = f"http://apiadvisor.climatempo.com.br/api/v1/forecast/locale/3907/days/15?token={api_key}"

    requisicao = requests.get(url2)

    print(requisicao.json())

    requisicao_dic = requisicao.json()

    global lista_semana
    global lista_data
    global lista_chance_chuva
    global descricao_lista


    for i in range(0, 7):
        chances_de_chuva = requisicao_dic['data'][i]['rain']['probability']
        data = requisicao_dic['data'][i]['date_br']
        lista_data.append(data)
        lista_chance_chuva.append(chances_de_chuva)
        descricao = requisicao_dic['data'][i]['text_icon']['text']['phrase']['reduced']
        descricao_lista.append(descricao)

        texto = f'''\n {data} : Possibilidade de chuva: {chances_de_chuva} %  '''
        lista_semana.append(texto)


    texto_informativo_data = Label(janela, text="Escolha uma data: ")
    texto_informativo_data.grid(column=1, row=4)


    for dias in lista_data:
        lista_opcao.insert(END, dias)
    lista_opcao.grid(column=1, row=5, padx=10)

    botao_verifica_data = Button(janela, text="Verificar data", command=verificar_data, bg="#4C21BD", fg="white",
                                 font="Times 10 bold")
    botao_verifica_data.grid(column=1, row=6, pady=5)

    botao_pesquisar['command'] = ""
    texto_inicial['text'] = ""

def verificar_data():
    lista_opcao.get(ACTIVE)

    if lista_opcao.get(ACTIVE) == lista_data[0]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[0]
        info = descricao_lista[0]
        texto_descricao["text"] = info.replace(".", ". \n")

        if lista_chance_chuva[0] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[0] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[0] >= 40 and lista_chance_chuva[0] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)

    elif lista_opcao.get(ACTIVE) == lista_data[1]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[1]
        info = descricao_lista[1]
        texto_descricao["text"] = info.replace(".", ". \n")


        if lista_chance_chuva[1] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[1] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[1] >= 40 and lista_chance_chuva[1] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)


    elif lista_opcao.get(ACTIVE) == lista_data[2]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[2]
        info = descricao_lista[2]
        texto_descricao["text"] = info.replace(".", ". \n")


        if lista_chance_chuva[2] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[2] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[2] >= 40 and lista_chance_chuva[2] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)


    elif lista_opcao.get(ACTIVE) == lista_data[3]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[3]
        info = descricao_lista[3]
        texto_descricao["text"] = info.replace(".", ". \n")

        if lista_chance_chuva[3] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[3] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[3] >= 40 and lista_chance_chuva[3] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)


    elif lista_opcao.get(ACTIVE) == lista_data[4]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[4]
        info = descricao_lista[4]
        texto_descricao["text"] = info.replace(".", ". \n")


        if lista_chance_chuva[4] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[4] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[4] >= 40 and lista_chance_chuva[4] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)


    elif lista_opcao.get(ACTIVE) == lista_data[5]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[5]
        info = descricao_lista[5]
        texto_descricao["text"] = info.replace(".", ". \n")

        if lista_chance_chuva[5] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[5] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[5] >= 40 and lista_chance_chuva[5] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)


    elif lista_opcao.get(ACTIVE) == lista_data[6]:
        texto_informativo["text"] = "Dia atual: " + lista_semana[6]
        info = descricao_lista[6]
        texto_descricao["text"] = info.replace(".", ". \n")

        if lista_chance_chuva[6] < 40:
            figura1 = Label(image=ensolarado)
            figura1.place(x=125, y=250)
        elif lista_chance_chuva[6] > 70:
            figura2 = Label(image=chuvoso)
            figura2.place(x=125, y=250)
        elif lista_chance_chuva[6] >= 40 and lista_chance_chuva[6] < 70:
            figura2 = Label(image=chuva_leve)
            figura2.place(x=125, y=250)





# Inicialização do programa:

janela = Tk()

#definições da janela do app.
largura = 600
altura = 500
largura_screen = janela.winfo_screenwidth()
altura_screen = janela.winfo_screenheight()
posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

janela.title("Take Your Umbrella")
#janela.geometry("600x500+200+200")
janela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
janela.resizable(False, False)

janela.iconbitmap("imagens/logotempo.ico")

#-------------------------------------------------------------------------


#Figuras
ensolarado = PhotoImage(file="imagens/ensolarado.png")
ensolarado = ensolarado.subsample(4, 4)
chuvoso = PhotoImage(file="imagens/chuvoso.png")
chuvoso = chuvoso.subsample(4, 4)
chuva_leve = PhotoImage(file="imagens/chuva_leve.png")
chuva_leve = chuva_leve.subsample(4, 4)
img_principal = PhotoImage(file="imagens/imgPrincipal2.png")
img_principal = img_principal.subsample(4, 4)


#menu principal

figura3 = Label(image=img_principal)
figura3.place(x=400, y=30)

botao_pesquisar = Button(janela, text="Pesquisar", command=pesquisar, bg="#4C21BD", fg="white", font="Times 10 bold",
                         padx=5, pady=5, justify="center")
botao_pesquisar.grid(column=0, row=3, pady=20)


texto_inicial = Label(janela, text="WELLCOME TO \n TAKE YOUR UMBRELLA!", fg="black", font="Constantia 20 bold")
texto_inicial.place(x=130, y=250)

texto_principal = Label(janela, text="Probabilidade de chuva em Lorena-SP: ", padx=10, pady=5,
                        width=50, height=5)
texto_principal.grid(column=0, row=2)


texto_informativo = Label(janela, text="", width=50)
texto_informativo.grid(column=0, row=4)

texto_descricao = Label(janela, text="", justify="center")
texto_descricao.grid(columnspan=2, row=7, padx=20, pady=20)


lista_opcao = Listbox(janela)


janela.mainloop()
