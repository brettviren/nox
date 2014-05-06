#!/usr/bin/env python
import common

import nox.profile

import tempfile

def test_create():
    temp = tempfile.mkdtemp()
    name = "test-profile"
    
