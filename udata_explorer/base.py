"""Base module"""


class HydratableObject(object):
    """A mixin to hold some dict data in `data` attribute"""

    def __init__(self, data):
        self.data = data
