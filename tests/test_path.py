#!/usr/bin/env python

import os
import common
import nox.path

def test_find_contents():
    d,f = nox.path.contents(os.path.join(common.testdir,'store/bar-v1/'))
    print 'DIRS:\n\t' + '\n\t'.join(d)
    print 'FILES:\n\t' + '\n\t'.join(f)

if '__main__' == __name__:
    test_find_contents()

