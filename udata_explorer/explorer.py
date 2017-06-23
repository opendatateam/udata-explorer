"""Explorer base module"""

import requests

from .datasets import Dataset


class Explorer(object):
    """Explorer base class"""

    def __init__(self, url):
        self.base_url = url
        r = requests.get(self.base_url)
        if r.status_code != 200:
            raise Exception('Could not reach %s' % self.base_url)

    def get_datasets(self, **kwargs):
        """Get datasets w/ kwargs filters

        Maps to GET /datasets/
        """
        r = requests.get('{}datasets/'.format(self.base_url), params=kwargs)
        if r.status_code != 200:
            raise Exception('Error fetching datasets (%s)' % kwargs)
        return [
            Dataset(**d) for d in r.json()['data']
        ]

    def get_dataset(self, d_id):
        """Get a dataset by id

        Maps to GET /datasets/<id>/
        """
        r = requests.get('{}/datasets/{}/'.format(self.base_url, d_id))
        if r.status_code != 200:
            raise Exception('Error fetching dataset w/ id %s' % d_id)
        return Dataset(**r.json())
