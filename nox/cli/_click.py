"""
Import Click with some augmentation.
"""

from click import *
from click.utils import *

import sys
def error(msg, code=1):
    sys.stderr.write(msg + '\n')
    sys.exit(code)
