import json
from datetime import datetime
from pathlib import Path

import click


@click.command()
@click.argument('title')
@click.option('--content', prompt=True, help='The content of the book')
@click.option('--version', type=int, default=1, help='The version of the book')
# @click.option('--author', default='Anonymous', help='The author of the book')
def create(title: str, content: str, version: int) -> None:
    # Create a new not
    notes_directory = Path("notes")
    note_name = f"{title}.txt"
    if (notes_directory / note_name).exists():
        click.echo(f"Note {title} already exists!")
        exit(1)

    note_data = {
        "title": title,
        "version": version,
        "content": content,
        "created_at": datetime.now().isoformat()
    }
    with open(notes_directory / note_name, "a+") as file:
        json.dump(note_data, file)
    click.echo(f"Note {title} created successfully!")
