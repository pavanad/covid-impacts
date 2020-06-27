# -*- coding: utf-8 -*-

from .extract import ExtractService


class TransformService:
    def __init__(self, datasets: ExtractService):
        self.datasets = datasets
