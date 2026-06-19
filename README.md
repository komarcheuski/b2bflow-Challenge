# B2B Flow Challenge

## Sobre o Projeto

Este projeto foi desenvolvido em Python com integração entre **Supabase** e **Z-API**, atendendo ao desafio proposto de leitura de contatos armazenados em banco de dados e envio automatizado de mensagens personalizadas via WhatsApp.

O sistema realiza a consulta dos contatos cadastrados no Supabase, limita o processamento aos três primeiros registros encontrados e envia uma mensagem personalizada para cada contato utilizando a API da Z-API.

Mensagem enviada:

```text
Olá, <nome_contato> tudo bem com você?
```

---

## Tecnologias Utilizadas

* Python 3.11
* Supabase
* Z-API
* Requests
* Python Dotenv
* Rich

---

## Estrutura do Projeto

```text
b2bflow-project/
│
├── services/
│   ├── __init__.py
│   ├── supabase_service.py
│   └── zapi_service.py
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## Fluxo da Aplicação

```text
Supabase
  ↓
Busca contatos cadastrados
  ↓
Limita até 3 registros
  ↓
Personaliza a mensagem
  ↓
Z-API
  ↓
WhatsApp
```

---

## Estrutura da Tabela no Supabase

Tabela: `contatos`

| Campo        | Tipo      |
| ------------ | --------- |
| id           | bigint    |
| nome_contato | text      |
| telefone     | text      |
| criado_em    | timestamp |

Exemplo:

| id | nome_contato | telefone      |
| -- | ------------ | ------------- |
| 1  | Rafaella     | 5541988322961 |
| 2  | Carla        | 5541999880389 |
| 3  | Joao         | 5541991150980 |

---

## Variáveis de Ambiente

Criar um arquivo `.env` na raiz do projeto:

```env
SUPABASE_URL=
SUPABASE_KEY=

ZAPI_INSTANCE_ID=
ZAPI_TOKEN=
ZAPI_CLIENT_TOKEN=
```

---

## Instalação

Criar ambiente virtual:

```bash
python -m venv venv
```

Ativar ambiente virtual (Windows):

```bash
venv\Scripts\activate
```

Instalar dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Executar o projeto:

```bash
python main.py
```

---

## Saída Esperada

O sistema exibirá:

* Tabela de contatos obtidos do Supabase.
* Status dos envios realizados.
* Resposta retornada pela Z-API.
* Informações detalhadas sobre cada mensagem enviada.

---

## Funcionalidades

* Consulta de contatos no Supabase.
* Limitação de até 3 contatos por execução.
* Personalização automática da mensagem.
* Integração com WhatsApp através da Z-API.
* Exibição amigável utilizando Rich.
* Tratamento de erros para variáveis de ambiente e falhas de integração.

---

## Exemplo de Mensagem

```text
Olá, Rafaella tudo bem com você?
```

```text
Olá, Carla tudo bem com você?
```

```text
Olá, Joao tudo bem com você?
```

---

## Autor

André Komarcheuski Rosa
