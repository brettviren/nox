#!/usr/bin/envy python

import os
import sys
import shutil
import tempfile

testdir = os.path.dirname(os.path.realpath(__file__))
pkgdir = os.path.dirname(testdir)
sys.path.insert(0, pkgdir)

package_names = ['pkg'+n for n in ['A','B','C']]
package_versions = ['v%d'%n for n in range(3)]
def package_idents():
    ret = list()
    for pname in package_names:
        for pver in package_versions:
            ret.append('%s-%s' % (pname, pver))
    return ret

def create_store():
    sdir = tempfile.mkdtemp(prefix='nox-test-')
    for ident in package_idents():
        bdir = os.path.join(sdir, ident, 'bin')
        os.makedirs(bdir)
        with open(os.path.join(bdir, 'prog%s'%ident[3]), 'w') as fp:
            fp.write('#!/bin/sh\ndate\npwd')
    print ("Populating test store directory at: %s" % sdir)
    os.environ['NOX_PACKAGE_PATH'] = sdir
    return sdir

def remove_storedir(sdir):
    print ("Deleting %s" % sdir)
    shutil.rmtree(sdir)
