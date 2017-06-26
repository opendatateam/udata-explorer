"""resources module"""

from .base import BaseResource
from .csv import CSVResource


def instantiate_resource(r_type, resource_dict):
    """Instantiate a resource based on its type

    TODO: load dynamically from resource type / format based on the files /
    classes present in `resources` module.
    """
    if r_type:
        if r_type.lower() == 'csv':
            return CSVResource(resource_dict)

    return BaseResource(resource_dict)
