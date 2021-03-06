
# -*- coding: utf-8 -*-
"""
Useful utility decorators.
"""


class renamed:
    """Decorator to mark functions are renamed and will be removed some later
    ```
    @pg.renamed(newname, '1.2')
    def oldname(args, kwargs):
        pass
    ```
    """
    def __init__(self, newFunc, removed=''):
        self.newFunc = newFunc
        self.removed = removed

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            import pygimli as pg
            pg.warning(func.__name__ + ' had been renamed to ' + \
                       self.newFunc.__name__ + \
                       ' and will be removed in: ' + self.removed)
            return self.newFunc(*args, **kwargs)
        return wrapper


import functools
def singleton(cls):
    """Make a class a Singleton class (only one instance)"""
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        if wrapper.instance is None:
            wrapper.instance = cls(*args, **kwargs)
        return wrapper.instance
    wrapper.instance = None
    return wrapper
