import click
import crud


@click.group()
def cli() -> None:
    print('Note CLI is working!')


cli.add_command(crud.create)
