#!/usr/bin/env python

import common

import nox.path

storedir = common.create_store()

def test_package_path():
    pp = nox.path.package_path()
    assert pp

def test_find_contents():
    d,f = nox.path.contents(storedir)
    #print 'DIRS:\n\t' + '\n\t'.join(d)
    #print 'FILES:\n\t' + '\n\t'.join(f)
    assert 9 == len(f)

def tear_down():
    common.remove_storedir(storedir)

if '__main__' == __name__:
    test_package_path()
    test_find_contents()
    tear_down()

