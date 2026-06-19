from dotenv import load_dotenv
from rich.console import Console
from rich.table import Table

from services.supabase_service import buscar_contatos
from services.zapi_service import enviar_mensagem


console = Console()

PALETA = [
    "#678c99",  # azul acinzentado
    "#b8c7cc",  # azul claro
    "#fff1cf",  # creme
    "#d6c292",  # bege
    "#b59e67"   # dourado
]


def exibir_contatos(contatos):

    tabela = Table(title="Contatos encontrados no Supabase")

    tabela.add_column("ID", justify="center")
    tabela.add_column("Nome", justify="left")
    tabela.add_column("Telefone", justify="center")

    cores_linhas = PALETA[::2]

    for i, contato in enumerate(contatos):
        cor = cores_linhas[i % len(cores_linhas)]

        tabela.add_row(
            f"[{cor}]{contato['id']}[/{cor}]",
            f"[{cor}]{contato['nome_contato']}[/{cor}]",
            f"[{cor}]{contato['telefone']}[/{cor}]"
    )

    console.print(tabela)


def exibir_resultado_envio(nome, telefone, status_code, resposta_json):

    CORES = {
        "Nome": PALETA[0],
        "Telefone": PALETA[1],
        "Status HTTP": PALETA[2],
        "zaapId": PALETA[2],
        "messageId": PALETA[3],
        "id": PALETA[4]
    }

    tabela = Table(title=f"Envio para {nome}")

    tabela.add_column("Campo", justify="left")
    tabela.add_column("Valor", justify="left")

    campos_fixos = {
        "Nome": nome,
        "Telefone": telefone,
        "Status HTTP": status_code
    }

    for campo, valor in campos_fixos.items():

        cor = CORES.get(campo, PALETA[0])

        tabela.add_row(
            f"[{cor}]{campo}[/{cor}]",
            f"[{cor}]{valor}[/{cor}]"
        )

    for chave, valor in resposta_json.items():

        cor = CORES.get(
            chave,
            PALETA[0]
        )

        tabela.add_row(
            f"[{cor}]{chave}[/{cor}]",
            f"[{cor}]{valor}[/{cor}]"
        )

    console.print(tabela)


def main():
    load_dotenv()

    try:
        contatos = buscar_contatos()

        if not contatos:
            console.print("[yellow]Nenhum contato encontrado no Supabase.[/yellow]")
            return

        exibir_contatos(contatos)

        console.print("\n[bold blue]Enviando mensagens pela Z-API...[/bold blue]")

        for contato in contatos[:3]:
            nome = contato["nome_contato"]
            telefone = contato["telefone"]
            mensagem = f"Olá, {nome} tudo bem com você?"

            resposta = enviar_mensagem(telefone, mensagem)

            console.print(f"\n[bold green]Mensagem enviada para {nome}![/bold green]")

            exibir_resultado_envio(
                nome,
                telefone,
                resposta.status_code,
                resposta.json()
            )

    except Exception as erro:
        console.print(f"[bold red]ERRO:[/bold red] {erro}")


if __name__ == "__main__":
    main()