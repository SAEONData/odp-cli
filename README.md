# odp-cli
A Python client and command line interface for the SAEON Open Data Platform API.

## Installation
Requires Python 3.7+

Clone this repository, then `cd` to the `odp-cli/` directory.

Set up a new Python virtual environment, if needed:

    python -m venv .venv
    source .venv/bin/activate
    pip install -U pip setuptools

Install the odp-cli package along with its dependencies:

    pip install -e .

## Configuration
Configuration is read from the environment. If a `.env` file is present, it will
be loaded automatically. See `.env.example` for an example.

SAEON will provide the appropriate configuration upon request for authorized clients.

## CLI usage
Currently only the catalog API endpoints have been implemented in the CLI.

List catalog definitions:

    odp catalog ls

Get a catalog definition:

    odp catalog get CATALOG_ID

List published catalog records:

    odp catalog harvest CATALOG_ID

The harvest result set is paged; to see paging options, type:

    odp catalog harvest --help

## Python client usage
Example of retrieving the list of project definitions from the project API:

    from odp.api import ODPClient
    client = ODPClient()
    r = client.get('/project')

To 'pretty print' the response as the CLI does:

    from odp.cli.utils import echo
    echo(r)
