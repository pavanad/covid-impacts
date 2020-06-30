# -*- coding: utf-8 -*-

import timeit

from services.extract import ExtractService
from services.transform import TransformService


def main():
    start = timeit.default_timer()
    extract = ExtractService()
    extract.execute()

    transform = TransformService()
    transform.datasets = extract.datasets
    transform.execute()

    timelapse = timeit.default_timer() - start
    print(f"timelapse: {timelapse}")


if __name__ == "__main__":
    main()
