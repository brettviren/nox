#!/usr/bin/env python
'''
Represent Nox packages
'''
import os
from collections import namedtuple
import path as pmod


def Package(ident, area):
    area = pmod.expand(area)
    path = os.path.join(area, ident)
    P = namedtuple('Package','ident area path dirs files')
    return P(ident, area, path, list(), list())


def fill(pkg):
    """Fill a package object.

    This fills the .files and .dirs attributes with the files and
    directories relative to the packages <.area>/<.ident>/ direcotry.
    """
    d,f = pmod.contents(pkg.path)
    pkg.dirs.extend(d)
    pkg.files.extend(f)
    return pkg


def get(ident, pathlist=None):
    """Return the named profile if it exists or None"""
    if not pathlist:
        pathlist = pmod.package_path()
    for area in pathlist:
        p = Package(ident, area)
        if os.path.exists(p.path):
            return fill(p)
    return None
