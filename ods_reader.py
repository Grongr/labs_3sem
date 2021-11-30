import pandas as pd

from pandas_ods_reader import read_ods

def read_file(file_in, list_count = 1):
    data = []

    for i in range(1, list_count + 1):
        data.append(read_ods(file_in, i))
    
    return data

if __name__ == "__main__":

    FILE       = './334/data/334.ods'
    LIST_COUNT = 7

    data = read_file(FILE, LIST_COUNT)
