"""
Operate on Nox stores.


"""

import os

class Store(object):
    def __init__(self):
        self._dir = None
        
def path():
    """Return the Nox store path"""
    p = os.path.environ.get('NOX_STORE_PATH')
    if not p: return list()
    return p.split(':')

