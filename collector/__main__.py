# -*- coding: utf-8 -*-

import timeit

from services.extract import ExtractService


def main():
    start = timeit.default_timer()
    extract = ExtractService()
    extract.execute()
    timelapse = timeit.default_timer() - start

    print(f"timelapse: {timelapse}")
    
if __name__ == "__main__":
    main()
