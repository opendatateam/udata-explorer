"""Base module"""


class HydratableObject(object):

    def __init__(self, **kwargs):
        for key in kwargs:
            setattr(self, key, kwargs[key])
