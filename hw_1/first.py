import click

@click.command()
@click.argument(
    'file',
    type=click.File('r'),
    required=False,
    default=None)
def nl(file):
    input_stream = file if file else click.get_text_stream('stdin')

    for idx, line in enumerate(input_stream):
        print(idx + 1, line.rstrip('\n'))

if __name__ == '__main__':
    nl()