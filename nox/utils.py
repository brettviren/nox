#!/usr/bin/env python

import os
def expand_path(path):
    return os.path.expanduser(os.path.expandvars(path))
