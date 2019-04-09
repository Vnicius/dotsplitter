import pandas as pd


def read_table(path):
    '''
        Read a csv file and return a DataFrame object

        Params:
            path(str): file's path 
    '''
    df = pd.read_csv(path, encoding='utf-8')

    return df
