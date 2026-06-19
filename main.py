from dotenv import load_dotenv
from services.supabase_service import buscar_contatos


def main():
    load_dotenv()

    contatos = buscar_contatos()

    print("\nCONTATOS ENCONTRADOS NO SUPABASE")
    print("-" * 60)
    print(f"{'ID':<5} {'NOME':<20} {'TELEFONE':<20}")
    print("-" * 60)

    for contato in contatos:
        print(
            f"{contato['id']:<5} "
            f"{contato['nome_contato']:<20} "
            f"{contato['telefone']:<20}"
        )


if __name__ == "__main__":
    main()