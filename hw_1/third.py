import click

def count_lines_words_characters(input_stream):
    lines = 0
    words = 0
    characters = 0

    for line in input_stream:
        if line[len(line) - 1] == '\n':
            lines += 1

        stripped_line = line.strip()
        words += 0 if len(stripped_line) == 0 else len(line.strip().split(' '))

        characters += len(line)

    return 0 if lines == -1 else lines, words, characters

@click.command()
@click.argument(
    'files',
    nargs = -1,
    type=click.Path(exists=True),
    required=False)
def wc(files):
    if len(files) == 0:
        (lines, words, characters) = count_lines_words_characters(click.get_text_stream('stdin'))
        print(lines, words, characters)
    else:
        for file in files:
            (lines, words, characters) = count_lines_words_characters(open(file, 'r'))
            print(lines, words, characters, file)

if __name__ == '__main__':
    wc()