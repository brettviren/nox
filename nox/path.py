#!/usr/bin/env python

import os
def expand(p):
    return os.path.expanduser(os.path.expandvars(p))

def assure(p):
    """Assure the path exists as a directory."""
    if os.path.exists(p):
        return
    os.makedirs(p)

def contents(p):
    """Return tuple of list of (dirs, files) relative to path <p>."""
    alldirs, allfiles = list(), list()
    for root, dirs, files in os.walk(p):
        print root
        rel = os.path.relpath(root, p)
        alldirs += [os.path.join(rel, d) for d in dirs]
        allfiles += [os.path.join(rel, f) for f in files]

    alldirs = [d[2:] if d.startswith('./') else d for d in alldirs]
    allfiles = [d[2:] if d.startswith('./') else d for d in allfiles]
    return (alldirs, allfiles)

