import click

@click.command()
@click.option(
    '--file',
    type=click.File('r'),
    default=None,
    help='File path')
def nl(file):
    input_stream = file if file else click.get_text_stream("stdin")

    for idx, line in enumerate(input_stream):
        print(idx, line.rstrip('\n'))

if __name__ == "__main__":
    nl()