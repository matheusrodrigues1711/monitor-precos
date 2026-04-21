# 📉 Monitor de Preços

Este projeto monitora o preço de um produto online e envia um alerta por e-mail quando o valor fica abaixo do limite definido.

## 🚀 Funcionalidades

- Captura o preço de produtos via scraping
- Permite definir um preço limite
- Envia e-mail automático quando o preço baixa
- Utiliza variáveis de ambiente para segurança

## 🛠️ Tecnologias utilizadas

- Python
- Requests
- BeautifulSoup
- SMTP (envio de e-mail)

## ⚙️ Como usar

### 1. Clone o repositório
```bash
git clone https://github.com/matheusrodrigues1711/monitor-precos.git
cd monitor-precos
Instale as dependências
pip install requests beautifulsoup4 python-dotenv
3. Configure o arquivo .env

Crie um arquivo .env na raiz do projeto:

EMAIL_SENHA=sua_senha_ou_token

⚠️ Nunca compartilhe esse arquivo publicamente.

4. Execute o projeto
python seu_arquivo.py
