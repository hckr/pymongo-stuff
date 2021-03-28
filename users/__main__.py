import click

import db


@click.group()
def cli():
    pass


@click.command(help="Register a new user")
@click.argument('login', required=True, type=click.STRING)
@click.argument('password', required=True, type=click.STRING)
def register(login: str, password: str):
    try:
        db.register(login, password)
    except db.UserAlreadyExists:
        print('User with this login already exists.')


@click.command(help="Register a new user")
@click.argument('login', required=True, type=click.STRING)
@click.argument('password', required=True, type=click.STRING)
def login(login: str, password: str):
    try:
        user = db.login(login, password)
        print(f'Successfully logged in as {user}')
    except db.AuthenticationError:
        print('Wrong login or password.')


cli.add_command(register)
cli.add_command(login)

if __name__ == '__main__':
    cli()
