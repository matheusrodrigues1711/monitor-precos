# 📉 Monitor de Preços

Este projeto monitora o preço de um produto online e envia um alerta por
e-mail quando o valor fica abaixo do limite definido.

## 🚀 Funcionalidades

-   Captura o preço de produtos via scraping
-   Permite definir um preço limite
-   Envia e-mail automático quando o preço baixa
-   Utiliza variáveis de ambiente para segurança

## 🛠️ Tecnologias utilizadas

-   Python
-   Requests
-   BeautifulSoup
-   SMTP (envio de e-mail)

## ⚙️ Como usar

### 1. Clone o repositório

``` bash
git clone https://github.com/matheusrodrigues1711/monitor-precos.git
cd monitor-precos
```

### 2. Instale as dependências

``` bash
pip install requests beautifulsoup4 python-dotenv
```

### 3. Configure o arquivo `.env`

Crie um arquivo `.env` na raiz do projeto:

    EMAIL_SENHA=sua_senha_ou_token

⚠️ Nunca compartilhe esse arquivo publicamente.

### 4. Execute o projeto

``` bash
python seu_arquivo.py
```

## 🔮 Melhorias futuras

-   Monitoramento contínuo em intervalos de tempo
-   Notificações via Telegram ou SMS
-   Interface web para controle dos produtos

## 📁 .gitignore

Inclua:

    .env
    __pycache__/

## 📌 Observações

-   O funcionamento depende da estrutura do site (HTML pode mudar)
-   Ideal para fins educacionais e projetos pessoais
