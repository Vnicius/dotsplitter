from os import path
from utils.readtable import read_table

DEFAULT_LIST_PATH = path.join('data', 'abreviaturas.csv')


class CheckAbbreviations:
    def __init__(self, list_path=DEFAULT_LIST_PATH):
        self.abbrev_list = self.__lower_abbreviations(read_table(list_path))

    def check(self, abbrev):

        result = self.abbrev_list.loc[self.abbrev_list['abbrev'] == abbrev.lower()]

        if result.empty:
            result = self.abbrev_list.loc[self.abbrev_list['abbrev'] == abbrev.replace('.', '').lower()]

        return not result.empty

    def __lower_abbreviations(self, df):
        df['abbrev'] = df['abbrev'].apply(lambda x: x.lower())
        return df
