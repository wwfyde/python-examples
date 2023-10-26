import json
import os

import psycopg
from psycopg.rows import dict_row, args_row, namedtuple_row, Row

with psycopg.connect(os.getenv('POSTGRESQL_DSN')) as conn:
    with conn.cursor(row_factory=dict_row) as cursor:
        cursor.execute("select version()")
        version: dict | None

        version = cursor.fetchone()
        # print(f"Version: {version.get('version', '')}")
        print(f"Version: {json.dumps(version)}")
        cursor.execute("select id, name from test")

        id: int
        name: str
        id, name = cursor.fetchone().values()
        print(f"id: {id}, name: {name}")

        cursor.execute("select current_database()")
        db_name: dict | None = cursor.fetchone()
        print(f"db_name: {db_name.get('current_database')}")

        cursor.row_factory = namedtuple_row
        test: Row = cursor.execute("select id, name from test").fetchone()
        print(test.id)

if __name__ == '__main__':
    pass
