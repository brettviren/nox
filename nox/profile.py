#!/usr/bin/env python
'''
Implement behavior of nox profiles.

Profiles have a name which makes up a directory or a symlink.

'''

import os
import shutil
from .utils import path as pmod
from collections import namedtuple

default_profile_area = "~/.profiles"

def Profile(name, area = None):
    area = pmod.expand(area or default_profile_area)
    path = os.path.join(area, name)
    return namedtuple('Profile','name area path')(name, area, path)

def get(name, area = None):
    """Return the named profile if it exists or None"""
    p = Profile(name, area)
    if os.path.exists(p.path):
        return p
    return None

def create(name, area = None, link = None):
    """Create a profile named <name>.

    The profile is created under <area>.

    If <link> is not None the profile is made as a link to <link>.

    If successful,  profile object is returned.  Else none.
    """
    p = Profile(name, area)

    if os.path.exists(p.path):
        OSError("Profile exists '%s'" % p.path)

    if not os.path.exits(p.area):
        os.makedirs(p.area)

    if link:
        link = pmod.expand(link)
        os.symlink(link, p.path)
        return
    if not os.path.exits(p.path):
        os.makedirs(p.path)
    return p

def remove(prof):
    """Remove the profile"""
    if not os.path.exists(prof.path):
        return
    if os.path.islink(prof.path):
        os.remove(prof.path)
        return
    shutil.rmtree(prof.path)
    return

def addpkg(prof, pkg):
    """Add package <pkg> to the profile <prof>."""
    pkgrecdir = os.path.join(prof.path, '.packages')
    if not pkgrecdir:
        os.makedirs(pkgrecdir)

    pkgrec = os.path.join(pkgrecdir, pkg.ident)
    if os.path.exists(pkgrec):
        OSError("Package %s exists in %s" % (pkg.ident, prof.path))
        return

    overlap = list()
    for f in pkg.files:
        ppath = os.path.join(prof.path,f)
        if os.path.exist(ppath):
            overlap.append(f)
    if overlap:
        OSError("Found %d existing files in profile %s from package %s" % (len(overlap), prof.name, pkg.ident))

    for d in pkg.dirs:
        dpath = os.path.join(prof.path,d)
        if os.path.exists:
            continue
        os.makedirs(dpath)
    for f in pkg.files:
        src = os.path.join(pkg.path, f)
        dst = os.path.join(prof.path, f)
        os.symlink(src, dst)

    os.symlink(pkg.path, pkgrec)
