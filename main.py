import requests
import smtplib
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_REMETENTE = input("Insira seu email: ")
from dotenv import load_dotenv
import os

load_dotenv()

EMAIL_SENHA = os.getenv("EMAIL_SENHA")

EMAIL_DESTINATARIO = input("Insira o email do destinatário: " )

def buscar_preco(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (Chrome/120.0.0.0 Safari/537.36)"
    }

    resposta = requests.get(url, headers=headers)
    soup = BeautifulSoup(resposta.content, "html.parser")
    preco = soup.find("span", class_="andes-money-amount__fraction")

    if preco:
        return int(preco.text.replace(".", ""))
    else:
        return None

def enviar_email(preco_atual, preco_limite, url):
    mensagem = MIMEMultipart()
    mensagem["From"] = EMAIL_REMETENTE
    mensagem["To"] = EMAIL_DESTINATARIO
    mensagem["Subject"] = "Alerta de preço! Hora de comprar!"

    corpo = f"""
    Boas notícias! O preço caiu abaixo do seu limite.

    Preço atual: R$ {preco_atual}
    Seu limite: R$ {preco_limite}
    Link do produto: {url}

    Corre lá antes que suba!
    """

    mensagem.attach(MIMEText(corpo, "plain"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as servidor:
        servidor.login(EMAIL_REMETENTE, EMAIL_SENHA)
        servidor.sendmail(EMAIL_REMETENTE, EMAIL_DESTINATARIO, mensagem.as_string())

    print("E-mail enviado com sucesso!")

def monitorar(url, preco_limite):
    print(f"Buscando preço...\n")
    preco_atual = buscar_preco(url)

    if preco_atual is None:
        print("Não foi possível encontrar o preço.")
        return

    print(f"Preço encontrado: R$ {preco_atual}")
    print(f"Seu limite: R$ {preco_limite}\n")

    if preco_atual < preco_limite:
        print("ALERTA! Preço abaixo do limite!")
        enviar_email(preco_atual, preco_limite, url)
    else:
        print("Preço ainda alto. Continuando monitorando...")

url = input("Insira a URL do produto: ")
preco_limite = int(input("Insira seu limite de preço: "))

monitorar(url, preco_limite)