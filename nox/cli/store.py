import os
from glob import glob
from . import _click as click

@click.group()
def main():
    """Operate on Nox stores."""
    pass

@main.command(name="list")
def _list():
    """List available Nox stores and their packages."""
    
    # fixme: factor this out into a nox.module
    path = os.environ.get('NOX_PACKAGE_PATH')
    if not path:
        return
    for p in path.split(':'):
        print p
        for f in os.listdir(p):
            d = os.path.join(p,f)
            if os.path.isdir(d) or os.path.islink(d):
                print '\t'+f
    pass

@main.command(name="search")
@click.argument('pattern')
def _search(pattern):
    path = os.environ.get('NOX_PACKAGE_PATH')
    if not path:
        return
    matches = list()
    for p in path.split(':'):
        matches.extend(sorted(glob(os.path.join(p, pattern))))
    for m in matches:
        click.echo('%s %s' % (os.path.basename(m), os.path.dirname(m)))

