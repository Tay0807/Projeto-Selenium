import customtkinter as tk
from PIL import Image
from tkcalendar import *

# Criar janela =========================================================================================================
def criar_janela(titulo,tamanho,tipo,cor=0,redimensionar=False,aparencia=0):
    if aparencia != 0:
        tk.set_appearance_mode(aparencia)
    if tipo == 1:
        janela = tk.CTk()
    else:
        janela = tk.CTkToplevel()

    janela.title(titulo)
    if cor != 0:
        janela.configure(fg_color=cor)
    if redimensionar == True:
        janela.resizable(width=True,height=True)
    else:
        janela.resizable(width=False,height=False)
    colunas = list(range(13))
    linha = list(range(13))
    janela.grid_columnconfigure(colunas, weight=1)
    janela.grid_rowconfigure(linha,weight=1)
    janela.geometry(tamanho)
    return janela


# criar botão ==========================================================================================================
def criar_botao(local,texto,comando,linha,coluna,largura,altura,cor=0,corHvover = 0):
    botao = tk.CTkButton(local,text=texto,command=comando,width=largura,height=altura)
    botao.grid(row = linha,column = coluna)
    if cor != 0:
        botao.configure(fg_color=cor)
    if corHvover != 0:
        botao.configure(hover_color=corHvover)
    return botao


#criar caixa de texto ==================================================================================================
def criar_caixa_texto(local,largura,altura,linha,coluna,texto = 0, password=False):
    caixa = tk.CTkEntry(local,width=largura,height=altura)
    caixa.grid(row = linha, column = coluna)
    if texto != 0:
        caixa.configure(placeholder_text=texto)
    if password != 0:
        caixa.configure(show='*')
    return caixa



# criar label ==========================================================================================================
def criar_label(local,texto,linha,coluna,color_text = 'black'):
    label = tk.CTkLabel(local,text=texto,text_color=color_text)
    label.grid(row = linha,column = coluna)
    if color_text != 'black':
        label._text_color = color_text
    return label



# criar checkbox =======================================================================================================
def criar_checkbox(local,coluna,linha,text=0,comando=0):
    check = tk.CTkCheckBox(local)
    check.grid(column = coluna, row = linha)
    if text != 0:
        check.configure(text=text)
    if comando != 0:
        check.configure(command=comando)
    return check


# criar switch =========================================================================================================

def criar_switch(local,texto,coluna,linha,comando=0):
    switch = tk.CTkSwitch(local,text=texto)
    switch.grid(column = coluna, row = linha)
    if comando != 0:
        switch.configure(command=comando)
    return switch

# criar combo box ======================================================================================================
def criar_combox(local,valor,linha,coluna,altura,largura,comando=0):
    combo = tk.CTkComboBox(local,values=valor,width=largura,height=altura)
    combo.grid(column = coluna, row=linha)
    if comando != 0:
        combo.configure(command=comando)
    return combo

# progressbar ==========================================================================================================
def criar_progressbar(local,largura,altura,coluna,linha):
    progress = tk.CTkProgressBar(local,width=largura,height=altura)
    progress.grid(column = coluna,row=linha)
    progress.set(0)
    return progress


# slider ===============================================================================================================
def criar_slider(local,largura,altura,coluna,linha):
    slider = tk.CTkSlider(local,width=largura,height=altura)
    slider.grid(column = coluna, row = linha)
    return slider


# imagem ===============================================================================================================

def criar_imagem(local,caminho,linha,coluna,altura,largura):
    imagem_pillow = Image.open(caminho)
    imageTk = tk.CTkImage(imagem_pillow,size=[largura,altura])
    image = tk.CTkLabel(local, image=imageTk, text='')
    image.grid(row = linha,column = coluna)
    return image


# frame ================================================================================================================
def criar_frame(local,largura,altura, linha, coluna):
    frame = tk.CTkFrame(local,width=largura, height=altura)
    frame.grid(row = linha, column = coluna)
    tamanho = list(range(13))
    frame.grid_rowconfigure(tamanho,weight=1)
    frame.grid_columnconfigure(tamanho,weight=1)
    frame.grid_propagate(False)
    return frame



def criar_aba(local,linha,coluna,largura,altura,*quant):
    aba = tk.CTkTabview(local,width=largura,height=altura)
    for arg in quant:
        aba.add(arg)
        tamanho = list(range(13))
        aba.tab(arg).grid_rowconfigure(tamanho, weight=1)
        aba.tab(arg).grid_columnconfigure(tamanho, weight=1)

    aba.grid(row = linha, column = coluna)
    return aba


def CriarCaixaData(Local,Linha,Coluna):
    data = DateEntry(Local,date_pattern="dd/mm/y",locale = "pt_BR" ,font= ("Arial",14),)
    data.grid(row=Linha,column = Coluna)
    return data

def Fundo(local,caminho,largura,altura):
    imagem_pillow = Image.open(caminho)
    imageTk = tk.CTkImage(imagem_pillow, size=[largura, altura])
    image = tk.CTkLabel(local, image=imageTk, text='')
    image.place(x=0,y=0)
    return image
