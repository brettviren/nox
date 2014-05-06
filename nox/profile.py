#!/usr/bin/env python
'''
Implement behavior of nox profiles.

Profiles have a name which makes up a directory or a symlink.

'''

import os
import sys
import shutil
from collections import namedtuple
import path as pmod

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

    if not os.path.exists(p.area):
        os.makedirs(p.area)

    if link:
        link = pmod.expand(link)
        os.symlink(link, p.path)
        return
    if not os.path.exists(p.path):
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

# fixme: factor this policy somewhere user configurable
def pkg_record_dir(prof, pkg):
    return os.path.join(prof.path, '.packages', pkg.ident)
def pkg_record_installation_dir(prof, pkg):
    return os.path.join(pkg_record_dir(prof,pkg), 'installation')

def pkg_record_exists(prof, pkg):
    """Return True if record of package <pkg> in profile <prof> exists and is consistent."""
    prd = pkg_record_dir(prof, pkg)
    if not os.path.exists(prd):
        return False
    instdir = pkg_record_installation_dir(prof, pkg)
    if not os.path.exists(instdir):
        return False
    if not os.samefile(instdir, pkg.path):
        raise ValueError("Package exists but differs %s != %s" % (instdir, pkg.path))
    return prd

def pkg_record_add(prof, pkg):
    """Add a package record for <pkg> in profile <prof>."""
    if pkg_record_exists(prof,pkg):
        ValueError('Package "%s" in profile "%s" already exists' % (pkg.ident, prof.name))
    instdir = pkg_record_installation_dir(prof, pkg)
    os.makedirs(os.path.dirname(instdir))
    os.symlink(pkg.path, instdir)

def pkg_record_del(prof, pkg):
    """Remove a package record for <pkg> in profile <prof>."""
    if not pkg_record_exists(prof, pkg):
        return
    die = pkg_record_dir(prof, pkg)
    shutil.rmtree(die)

def addpkg(prof, pkg):
    """Add package <pkg> to the profile <prof>."""
    if pkg_record_exists(prof, pkg):
        OSError("Package %s exists in %s" % (pkg.ident, prof.path))
        return

    overlap = list()
    for f in pkg.files:
        ppath = os.path.join(prof.path,f)
        if os.path.exists(ppath):
            overlap.append(f)
    if overlap:
        raise OSError("Found %d existing files in profile %s from package %s" % \
                      (len(overlap), prof.name, pkg.ident))

    for d in pkg.dirs:
        dpath = os.path.join(prof.path,d)
        if os.path.exists(dpath):
            continue
        os.makedirs(dpath)
    for f in pkg.files:
        src = os.path.join(pkg.path, f)
        dst = os.path.join(prof.path, f)
        try:
            os.symlink(src, dst)
        except OSError:
            sys.stderr.write('symlink "%s" -> "%s"\n' % (src,dst))
            raise

    pkg_record_add(prof, pkg)


def delpkg(prof, pkg):
    """Delete package <pkg> from profile <prof>."""
    if not pkg_record_exists(prof, pkg):
        return

    for f in pkg.files:
        die = os.path.join(prof.path, f)
        if os.path.exists(die):
            os.remove(die)

    for d in pkg.dirs:
        maybe = os.path.join(prof.path, d)
        if os.listdir(maybe):
           continue 
        os.removedirs(maybe)

    
