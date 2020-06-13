# -*- coding: utf-8 -*-

from dotenv import load_dotenv

from ..interfaces.database_interface import DataBaseInterface

load_dotenv()


def get_query(query):
    database = DataBaseInterface()
    data = database.execute_fetchall(query)
    database.close_connection()
    return data


def get_city_data(name):
    query = f"SELECT * FROM covid.cities WHERE covid.cities.city = '{name}'"
    return get_query(query)


def get_state_data(name):
    query = f"SELECT * FROM covid.states WHERE state = '{name}'"
    return get_query(query)


def get_predict_data(predict_type):
    table_name = "cases" if predict_type == "confirmados" else "deaths"
    query = f"SELECT * FROM covid.prediction_{table_name}"
    return get_query(query)


def get_economic_data():
    query = "SELECT * FROM covid.economic"
    return get_query(query)
