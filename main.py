from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem


console = Console()


def exibir_contatos(contatos):
    tabela = Table(title="Contatos encontrados no Supabase")

    tabela.add_column("ID", justify="center")
    tabela.add_column("Nome", justify="left")
    tabela.add_column("Telefone", justify="center")

    for contato in contatos:
        tabela.add_row(
            str(contato["id"]),
            contato["nome_contato"],
            contato["telefone"]
        )

    console.print(tabela)

def exibir_resposta_zapi(resposta_json):
    tabela = Table(title="Resposta da Z-API")

    tabela.add_column("Campo", justify="left")
    tabela.add_column("Valor", justify="left")

    for chave, valor in resposta_json.items():
        tabela.add_row(
            str(chave),
            str(valor)
        )

    console.print(tabela)


def main():
    load_dotenv()

    try:
        contatos = buscar_contatos()

        if not contatos:
            console.print(
                "[yellow]Nenhum contato encontrado no Supabase.[/yellow]"
            )
            return

        exibir_contatos(contatos)

        console.print(
            "\n[bold blue]Testando envio pela Z-API...[/bold blue]"
        )

        resposta = enviar_mensagem(
            "5541988322961",
            "Teste de integração Z-API realizado com sucesso!! 😸"
        )

        console.print(
            f"\n[bold green]Mensagem enviada com sucesso![/bold green]"
            )

        console.print(
            f"[green]Status HTTP:[/green] {resposta.status_code}"
            )

        exibir_resposta_zapi(
            resposta.json()
        )

    except Exception as erro:
        console.print(
            f"[bold red]ERRO:[/bold red] {erro}"
        )


if __name__ == "__main__":
    main()