import json
from dataclasses import asdict

import click

from odp.api import ODPResponse


def echo(response: ODPResponse):
    click.echo(
        json.dumps(asdict(response), indent=4, ensure_ascii=False)
    )
