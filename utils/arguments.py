from os import path
import argparse

DEFAULT_LIST_PATH = path.join('data', 'abreviaturas.csv')


def args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'lang', help='Language of the text. See spaCy language modules.')
    parser.add_argument(
        '--abbrev-path', help='File with abbreviation list', default=DEFAULT_LIST_PATH)
    return parser.parse_args()
