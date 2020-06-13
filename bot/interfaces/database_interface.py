from os import getenv

from sqlalchemy import create_engine, text


class DataBaseInterface(object):
    def __init__(self):
        database_config = {
            "name": getenv("DATABASE_NAME"),
            "user": getenv("DATABASE_USERNAME"),
            "password": getenv("DATABASE_PASSWORD"),
            "host": getenv("DATABASE_HOST"),
            "port": getenv("DATABASE_PORT"),
        }        
        self.database_name = database_config["name"]
        self.query_data = None

        self.db = create_engine(
            f"mysql:"
            f'//{database_config["user"]}'
            f':{database_config["password"]}'
            f'@{database_config["host"]}:{database_config["port"]}'
            f'/{database_config["name"]}'
        )

    def execute(self, query):
        try:
            q = self.db.execute(query)
            q.close()
        except Exception as err:
            raise Exception("Baseinterface: error on execute the query \n" + str(err))

    def execute_fetchall(self, query):
        try:
            q = self.db.execute(query)
            self.query_data = q.fetchall()
            q.close()
        except Exception as err:
            raise Exception(
                "Baseinterface: error on execute the query and fetch \n" + str(err)
            )
        return self.query_data

    def close_connection(self):
        self.db.dispose()
