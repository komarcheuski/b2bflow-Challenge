import os
from supabase import create_client


def buscar_contatos():
    supabase_url = os.getenv("SUPABASE_URL")
    supabase_key = os.getenv("SUPABASE_KEY")

    if not supabase_url and not supabase_key:
        raise ValueError(">>>error: SUPABASE_URL e SUPABASE_KEY não encontradas")
    elif not supabase_url:
        raise ValueError(">>>error: SUPABASE_URL não encontrada")
    elif not supabase_key:
        raise ValueError(">>>error: SUPABASE_KEY não encontrada")

    supabase = create_client(supabase_url, supabase_key)

    resposta = (
        supabase
        .table("contatos")
        .select("id, nome_contato, telefone")
        .limit(3)
        .execute()
    )

    return resposta.data