"""Base resource module"""

from ..base import HydratableObject


class BaseResource(HydratableObject):

    def __repr__(self):
        return '<{}>("{}")'.format(
            self.__class__.__name__,
            self.title
        )
