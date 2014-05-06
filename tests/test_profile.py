#!/usr/bin/env python

import os
import tempfile
import shutil

import common

import nox.profile
import nox.package

storedir = common.create_store()

profile_area = tempfile.mkdtemp(prefix='nox-test-profile-area-')
profile_name = 'nox-test-profile'

def test_create():
    prof = nox.profile.create(profile_name, profile_area)
    assert prof, prof

def test_add():
    prof = nox.profile.get(profile_name, profile_area)
    assert prof
    for ident in common.package_idents():
        p = nox.package.get(ident)
        assert p
        nox.profile.addpkg(prof, p)
    print prof
    print os.listdir(prof.path)

def test_del():
    prof = nox.profile.get(profile_name, profile_area)
    assert prof
    for ident in common.package_idents():
        p = nox.package.get(ident)
        assert p
        nox.profile.delpkg(prof, p)
    print os.listdir(prof.path)

def tear_down():
    shutil.rmtree(profile_area)
    common.remove_storedir(storedir)

if '__main__' == __name__:
    test_create()
    test_add()
    test_del()
    tear_down()

