import click
import os


@click.command()
@click.option('--data', required=False, help='Number of greetings.')
@click.argument('command')
def main(command, data):
    text = f'You called command `{command}`'
    if data:
        exists = "exists" if os.path.exists(data) else " doesn't exist"
        text += f' and you passed file `{data}` which {exists}'
    print(text)


if __name__ == '__main__':
    main()
