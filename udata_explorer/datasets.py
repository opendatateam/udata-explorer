"""Manipulate udata datasets"""

from .resources import instantiate_resource
from .base import HydratableObject


class Dataset(HydratableObject):

    def __init__(self, data):
        super().__init__(data)

    def __repr__(self):
        return '<Dataset {}>("{}" by "{}")'.format(
            self.data['id'],
            self.data['title'],
            self.data.get('organization', {}).get('name', 'NA')
        )

    @property
    def resources(self):
        return [
            instantiate_resource(
                r['format'], r
            ) for r in self.data.get('resources', [])
        ]
