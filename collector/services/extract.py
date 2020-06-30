# -*- coding: utf-8 -*-

import io
import json

import pandas as pd
import requests

from .sources import COVID, ECONOMIC


class ExtractService:
    def __init__(self):
        self.__datasets = {}
        self.__covid_urls = COVID
        self.__economic_urls = ECONOMIC
        self.__header = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) "
            "AppleWebKit/537.11 (KHTML, like Gecko) "
            "Chrome/23.0.1271.64 Safari/537.11",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Charset": "ISO-8859-1,utf-8;q=0.7,*;q=0.3",
            "Accept-Encoding": "none",
            "Accept-Language": "en-US,en;q=0.8",
            "Connection": "keep-alive",
        }

    @property
    def datasets(self):
        return self.__datasets

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
        sources = self.__covid_urls.copy()
        sources.update(self.__economic_urls)
        for key, url in sources.items():
            self.__datasets[key] = self.__make_requests(url)

    def execute(self):
        self.__fetch_datasets()
