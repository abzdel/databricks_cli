#!./venv/bin/python

import os
from databricks import sql

def querydb(query):
    """
    Default query, selects top two rows from fortune100 table.
    Returns result from our query.
    """

    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM default.fortune_1000 LIMIT 2")
            result = cursor.fetchall()

        for row in result:
            print(row)

    return result



def custom_query(rank):
    """
    Custom query - user enters a rank (for fortune 1000).
    Returns and prints company associated with rank.
    """

    assert rank < 1001
    assert rank > 0

    with sql.connect(server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME"),
                 http_path       = os.getenv("DATABRICKS_HTTP_PATH"),
                 access_token    = os.getenv("DATABRICKS_TOKEN")) as connection:

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT name FROM default.fortune_1000 WHERE rank = {rank} LIMIT 1")
            result = cursor.fetchone()

    print(f"{result[0]} is rank {rank} in our dataset.")


    return result