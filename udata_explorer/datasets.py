"""Manipulate udata datasets"""

from .resources import instantiate_resource
from .base import HydratableObject


class Dataset(HydratableObject):

    def __init__(self, **kwargs):
        self._resources = kwargs.pop('resources', [])
        super().__init__(**kwargs)

    def __repr__(self):
        return '<Dataset {}>("{}" by "{}")'.format(
            self.id,
            self.title,
            self.organization['name'] if self.organization else 'NA'
        )

    @property
    def resources(self):
        return [
            instantiate_resource(r['format'], r) for r in self._resources
        ]
