import os
import requests


def enviar_mensagem(telefone, mensagem):
    instance_id = os.getenv("ZAPI_INSTANCE_ID")
    token = os.getenv("ZAPI_TOKEN")
    client_token = os.getenv("ZAPI_CLIENT_TOKEN")

    if not instance_id:
        raise ValueError("ZAPI_INSTANCE_ID não encontrado")

    if not token:
        raise ValueError("ZAPI_TOKEN não encontrado")

    if not client_token:
        raise ValueError("ZAPI_CLIENT_TOKEN não encontrado")

    url = (
        f"https://api.z-api.io/instances/"
        f"{instance_id}/token/{token}/send-text"
    )

    payload = {
        "phone": telefone,
        "message": mensagem
    }

    headers = {
        "Client-Token": client_token,
        "Content-Type": "application/json"
    }

    resposta = requests.post(
        url,
        json=payload,
        headers=headers,
        timeout=30
    )

    return resposta