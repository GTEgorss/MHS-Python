import click
from collections import deque

def output_last_n_lines(input_stream, n=10):
    last_n_lines = deque(maxlen=n)

    for line in input_stream:
        last_n_lines.append(line.rstrip())

    for line in last_n_lines:
        print(line)


@click.command()
@click.argument(
    'files',
    nargs=-1,
    type=click.Path(exists=True),
    required=False,
    default=None)
def tail(files):
    if len(files) == 0:
        output_last_n_lines(click.get_text_stream('stdin'), 17)
    else:
        for file in files:
            if len(files) > 1:
                print(f'==> {file} <==')

            output_last_n_lines(open(file, 'r'))

if __name__ == '__main__':
    tail()