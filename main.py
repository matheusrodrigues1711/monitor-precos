import requests
import smtplib
import mysql.connector
import os
from bs4 import BeautifulSoup
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()

EMAIL_REMETENTE = input("Insira seu email: ")
EMAIL_SENHA = os.getenv("EMAIL_SENHA")
EMAIL_DESTINATARIO = input("Insira o email do destinatário: ")

def conectar_banco():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )

def salvar_preco(url, preco, preco_limite):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO historico_precos (url, preco, preco_limite)
        VALUES (%s, %s, %s)
    """, (url, preco, preco_limite))

    conn.commit()
    cursor.close()
    conn.close()
    print("Preço salvo no histórico!")

def buscar_historico(url):
    conn = conectar_banco()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT preco, data_verificacao 
        FROM historico_precos 
        WHERE url = %s 
        ORDER BY data_verificacao DESC 
        LIMIT 10
    """, (url,))

    historico = cursor.fetchall()
    cursor.close()
    conn.close()
    return historico

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

    salvar_preco(url, preco_atual, preco_limite)

    historico = buscar_historico(url)
    if len(historico) > 1:
        print("Histórico de preços:")
        for preco, data in historico:
            print(f"  R$ {preco} — {data.strftime('%d/%m/%Y %H:%M')}")
        print()

    if preco_atual < preco_limite:
        print("ALERTA! Preço abaixo do limite!")
        enviar_email(preco_atual, preco_limite, url)
    else:
        print("Preço ainda alto. Continuando monitorando...")

url = input("Insira a URL do produto: ")
preco_limite = int(input("Insira seu limite de preço: "))

monitorar(url, preco_limite)