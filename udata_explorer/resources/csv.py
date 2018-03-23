"""CSV resource module"""
import os
import csv

from tempfile import NamedTemporaryFile

import chardet
import requests

from pandas.io.parsers import ParserError, ParserWarning

import warnings

import pandas as pd

from .base import BaseResource

MAX_HEADER_ROWS_DETECTION = 30
SNIFFING_SIZE = 32768

# ParserWarning: https://github.com/pandas-dev/pandas/issues/18845
warnings.simplefilter(action='ignore', category=ParserWarning)


class CSVResource(BaseResource):

    def detect_encoding(self):
        tf = open(self.tf.name, 'rb')
        res = chardet.detect(tf.read(SNIFFING_SIZE))
        tf.close()
        return res['encoding']

    def detect_dialect(self, encoding):
        with open(self.tf.name, 'r', encoding=encoding) as csvfile:
            dialect = csv.Sniffer().sniff(csvfile.read(SNIFFING_SIZE),
                                          delimiters=[',', ';', '\t'])
        return dialect

    def parse_df(self, encoding, dialect):
        for i in range(MAX_HEADER_ROWS_DETECTION):
            try:
                df = pd.read_csv(self.tf.name, dialect=dialect,
                                 encoding=encoding, skiprows=i)
                break
            except ParserError:
                pass
        return df

    def get_df(self):
        self.tf = NamedTemporaryFile(delete=False)

        r = requests.get(self.data['url'])
        self.tf.write(r.content)
        self.tf.close()

        encoding = self.detect_encoding()
        dialect = self.detect_dialect(encoding)
        df = self.parse_df(encoding, dialect)

        self.tf.close()
        os.unlink(self.tf.name)

        return df

    def get_data(self, read_csv_options=None):
        """
        Load CSV data into a Panda dataframe
        """
        if not self.data.get('url'):
            raise Exception('Missing resource url')
        if not read_csv_options:
            return self.get_df()
        else:
            return pd.read_csv(self.data['url'], **read_csv_options)
