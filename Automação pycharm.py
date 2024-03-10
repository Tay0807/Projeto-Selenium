# eu estou importando o própio webdriver que vai controlar meu navega#unicodedata -->  biblioteca que possui as acentuações etc
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import pandas as pd
from modulo_tk import *
from email.message import EmailMessage
import ssl
import smtplib


def envia_email():
    email = 'taynamacedo0804@gmail.com'
    senha = 'puds oypv xyrj jdzv'
    email_destinatario = entrada_email.get()
    assunto = 'Sua Análise Automatizada Está Concluída - Oportunidade à Vista!'
    body = f""""
               Fico feliz em informar que a análise automática das 
               cotações de commodities foi concluída com sucesso!

               O "Pricing" analisou as condições atuais do mercado, 
               considerando os valores ideais de cada produto. 
               
               Após uma análise criteriosa, identificamos quais 
               commodities são favoráveis para compra, obtendo 
               insights importantes. 
               
               Esses detalhes podem ser visualizados no link abaixo. 
               
               Segue um link do Power BI:
               https://app.powerbi.com/view?r=eyJrIjoiZDZhZDM5OWUtNmM5Yi00NjEwLTk0ZmUtNzRjYTVlY2MzZmI5IiwidCI6IjEwMmI4YTVlLTcyNDctNGZkYS1iZDBiLTIxNzExNGRiYjZhZSJ9
                 
            """

    em = EmailMessage()

    em['From'] = email
    em['To'] = email_destinatario
    em['subject'] = assunto
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email, senha)
        smtp.sendmail(email, email_destinatario, em.as_string())

    Fim()
def Fim():
    tela_inicial.withdraw()
    tela_final = criar_janela('Pricing', '400x500', 2, False, False, 'Light')
    tela_final.iconbitmap('icon.ico')
    backgraund_fim = Fundo(tela_final, "2.png", 400, 500)


def RealizarCotacao():
    tabela = pd.read_excel("commodities.xlsx")

    servico = Service(ChromeDriverManager().install())
    # abre uma aba no google chrome
    navegador = webdriver.Chrome(service=servico)

    # abre um site -->  get pega e quit()fecha
    navegador.get("https://www.google.com.br/")
    # tabela.index --> linhas da tabela
    for linha in tabela.index:

        produtos = tabela.loc[linha, 'Produto']

        link = f"https://www.melhorcambio.com/{produtos}-hoje"
        link = link.replace('á', 'a').replace('ó', 'o').replace('é', 'e').replace('ç', 'c').replace('ã', 'a').replace(
            'ú',
            'u')
        # entrando no site para pegar as cotações
        navegador.get(link)

        # pegando o elemento de dentro do input
        cotacao = navegador.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
        # .send_keys("digita algo") --> digita no elemento
        # .click() --> clica no elemento
        # .get_attribute('oq eu quero pegar') -->  pega o valor do elemento

        # .replace vai trocar a virgula e o ponto --> float vai transformar em múmero
        cotacao = cotacao.replace('.', '').replace(',', '.')
        cotacao = float(cotacao)

        # mudando o valor na tabela -->  tabela.loc[linha, 'coluna']
        tabela.loc[linha, 'Preço Atual'] = cotacao

        # verificação se pode ou nn comprar
        if (cotacao > tabela.loc[linha, 'Preço Ideal']):
            tabela.loc[linha, 'Comprar'] = "Não comprar"
        else:
            tabela.loc[linha, 'Comprar'] = "Comprar"

        # 2 forma --> tabela["Comprar"] = tabela["preço Atual"] < tabela["preço ideal] --> retorna true and false

    tabela.to_excel("commodities_novo.xlsx", index=False)
    navegador.quit()
    envia_email()



tela_inicial = criar_janela('Pricing','400x500',1,False,False,'Light')
tela_inicial.iconbitmap('icon.ico')

backgraund_inicio = Fundo(tela_inicial,"1.png", 400,500)

entrada_email = criar_caixa_texto(tela_inicial, 250, 30, 11, 6)
entrada_email.configure(bg_color='#3D7D94')

bnt = criar_botao(tela_inicial,'Realizar Cotação',RealizarCotacao,12,6,150,30)
bnt.configure(bg_color='#3D7D94', fg_color='white', hover_color='green', text_color='#3D7D94')





tela_inicial.mainloop()


