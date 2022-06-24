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
Configuration is read from a `.env` file, which SAEON will provide upon request
for authorized clients. See `.env.example` for an example.

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
