#!/usr/bin/env python

import os

import common

import nox.package

storedir = common.create_store()

def test_get():
    for ident in common.package_idents():
        p = nox.package.get(ident)
        assert p
        for f in p.files:
            assert os.path.exists(os.path.join(p.path,f)), f

def tear_down():
    common.remove_storedir(storedir)


if '__main__' == __name__:
    test_get()
    tear_down()
