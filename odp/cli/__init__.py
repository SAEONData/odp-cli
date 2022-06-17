import click

from odp.api import ODPClient
from odp.cli import catalog


@click.group()
@click.pass_context
def odp(ctx):
    ctx.obj = ODPClient()


odp.add_command(catalog.catalog)
