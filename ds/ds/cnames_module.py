import inspect
import random
import csv


def get_classes(mod):
    """Return a list of all classes in module 'mod'"""
    return [
        name
        for name, name_type in inspect.getmembers(mod)
        if inspect.isclass(name_type) and name[0].isupper()
    ]
