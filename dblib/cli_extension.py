#!./venv/bin/python

import sys
import click
from querydb import querydb, custom_query


# build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""


# build a click command
@cli.command()
@click.option(
    "--query",
    # defaults to selecting the top two rows from fortune1000 table
    default="SELECT * FROM default.fortune_1000 LIMIT 2",
    help="SQL query to execute",
)
def cli_query(query):
    """Execute a SQL query."""
    querydb(query)


@cli.command()
@click.option(
    "--rank",
    # defaults to selecting the first company (rank 1)
    # should be Walmart in our dataset
    default="SELECT name FROM default.fortune_1000 WHERE rank = 1 LIMIT 1",
    help="SQL query to execute",
)

def rank_query(rank):
    """
    Query fortune1000 table based on the rank of a company.
    Takes rank as a command line argument.
    Calls custom_query from querydb.py.

    """

    if not len(sys.argv) == 4:
        print("must enter ONE integer value when using --rank")
        exit()
    if not sys.argv[3].isdigit():
        print("must enter an integer value for rank")
        exit()

    rank = int(sys.argv[3])

    custom_query(rank)

# run the CLI
if __name__ == "__main__":
    cli()