import click

from odp.api import ODPClient
from odp.cli.utils import echo


@click.group()
@click.pass_obj
def catalog(api: ODPClient):
    pass


@catalog.command()
@click.pass_obj
def ls(api: ODPClient):
    r = api.get('/catalog')
    echo(r)


@catalog.command()
@click.argument('catalog_id')
@click.pass_obj
def get(api: ODPClient, catalog_id: str):
    r = api.get(f'/catalog/{catalog_id}')
    echo(r)


@catalog.command()
@click.argument('catalog_id')
@click.option('--page-num', default=1, show_default=True, help='page number')
@click.option('--page-size', default=100, show_default=True, help='page size (0 = unlimited)')
@click.pass_obj
def harvest(api: ODPClient, catalog_id: str, page_num: int, page_size: int):
    r = api.get(f'/catalog/{catalog_id}/records?page={page_num}&size={page_size}')
    echo(r)
