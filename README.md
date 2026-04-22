# Monitor de Preços 🔎

Aplicação que monitora o preço de produtos no Mercado Livre e envia um alerta por e-mail automaticamente quando o preço cai abaixo do limite definido.

## Funcionalidades
- Busca o preço atual de qualquer produto no Mercado Livre
- Compara com o limite de preço definido pelo usuário
- Envia e-mail de alerta quando o preço está abaixo do limite

## Tecnologias utilizadas
- Python
- Requests
- BeautifulSoup4
- smtplib

## Como usar
1. Clone o repositório
2. Instale as dependências: `pip install requests beautifulsoup4 python-dotenv`
3. Crie um arquivo `.env` com sua senha de app do Gmail:
4. EMAIL_SENHA=sua_senha_aqui
5. 4. Execute: `python main.py`
5. Insira a URL do produto e o limite de preço

## Autor
Matheus Rodrigues
