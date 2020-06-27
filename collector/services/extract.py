# -*- coding: utf-8 -*-

import io
import json

import pandas as pd
import requests

from .sources import COVID, ECONOMIC


class ExtractService:
    def __init__(self):
        self._datasets = {}
        self._covid_urls = COVID
        self._economic_urls = ECONOMIC

        self.__header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.11 (KHTML, like Gecko) "
        }

    @property
    def datasets(self):
        return self._datasets

    def __make_requests(self, url: str) -> pd.DataFrame:
        df_content = pd.DataFrame()
        response = requests.get(url, headers=self.__header)
        if "json" in url:
            content = response.json()
            df_content = pd.json_normalize(content)
        else:
            content = io.StringIO(response.content.decode("utf-8"))
            df_content = pd.read_csv(content)

        return df_content

    def __fetch_datasets(self):
        sources = self._covid_urls.copy()
        sources.update(self._economic_urls)
        for key, url in sources.items():
            self._datasets[key] = self.__make_requests(url)

    def execute(self):
        self.__fetch_datasets()
