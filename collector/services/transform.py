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

    def save_to_database(self):
        pass

    def __covid_transformation(self):
        self.__datasets["covid"] = self.__datasets["covid"].rename(
            columns={"city_ibge_code": "codigo_ibge"}
        )
        self.__datasets["covid"]["date"] = pd.to_datetime(
            self.__datasets["covid"]["date"], errors="raise"
        )

    def __economic_transformation(self):
        self.__datasets["dolar"] = self.__datasets["dolar"][
            self.__datasets["dolar"]["dataHoraCotacao"].between(
                "2019-01-01", "2020-12-31"
            )
        ]
        self.__datasets["dolar"]["dataHoraCotacao"] = pd.to_datetime(
            self.__datasets["dolar"]["dataHoraCotacao"], errors="raise"
        )

        for key, _ in self.__datasets.items():
            dataset = self.__datasets[key]
            if "data" in dataset.columns:
                dataset.set_axis(["data", f"valor_{i}".lower()], axis=1, inplace=True)
                dataset["year"] = pd.DatetimeIndex(dataset["data"]).year
                dataset["month"] = pd.DatetimeIndex(dataset["data"]).month

    def execute(self):
        self.__covid_transformation()
        self.__economic_transformation()

        for key, value in self.__datasets.items():
            print(key)
            print(self.__datasets[key].columns)
