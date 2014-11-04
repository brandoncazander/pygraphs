# Skeleton of a CLI

import click

import pygraphs


@click.command('pygraphs')
@click.argument('count', type=int, metavar='N')
def cli(count):
    """Echo a value `N` number of times"""
    for i in range(count):
        click.echo(pygraphs.has_legs)
