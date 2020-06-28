# -*- coding: utf-8 -*-

import pandas as pd

class TransformService:
    def __init__(self):
        self.__datasets = {}

    @property
    def datasets(self) -> dict:
        return self.__datasets

    @datasets.setter
    def datasets(self, datasets: dict):
        self.__datasets = datasets

    def __covid_transformation(self):
        self.__datasets["covid"] = self.__datasets["covid"].rename(
            columns={"city_ibge_code": "codigo_ibge"}
        )
        self.__datasets["covid"]["date"] = pd.to_datetime(
            self.__datasets["covid"]["date"], errors="raise"
        )

    def execute(self):
        self.__covid_transformation()
