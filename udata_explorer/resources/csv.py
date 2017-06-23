"""CSV resource module"""

import pandas as pd

from .base import BaseResource


class CSVResource(BaseResource):

    def get_data(self):
        """
        Load CSV data into a Panda dataframe
        """
        if not self.url:
            raise Exception('Missing resource url')
        return pd.read_csv(self.url)
