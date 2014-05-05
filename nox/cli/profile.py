import os
from . import _click as click

@click.group()
def main():
    """Operate on Nox profiles."""
    pass

@main.command(name="list")
def _list():
    """List known Nox profiles."""
    pass

@main.command(name="new")
@click.argument('name')
@click.option('--path', '-p', nargs=1, default='~/.nox/profiles',
              help='Set and explicit path to directory holding profile.')
@click.option('--link', '-l', nargs=1,
              help='Make profile a link to an existing one.')
def _new(name, path, link):
    """Create a new Nox profile."""
    # fixme: factor this out into a nox.module
    path = os.path.expanduser(path)
    if not os.path.exists(path):
        os.makedirs(path)
    pass
    fullpath = os.path.join(path,name)
    if os.path.exists(fullpath):
        click.error("File exists: %s" % fullpath)
    if link:
        click.error('linking not implemented')
        if not os.path.exists(link):
            click.error("No such file or directory: %s" % link)
        os.symlink(link, fullpath)
        click.error('created %s as link to %s' % (name, link))
        return
    os.mkdir(fullpath)
    click.echo('created profile %s in %s' % (name, path))
        
@main.command(name="del")
@click.argument('name')
def _del(name):
    """Remove a profile."""
    pass

@main.command(name="add")
@click.argument('name')
@click.argument('package')
def _add(name, package):
    """Add a package to a profile"""
    pass

@main.command(name="dup")
@click.argument('src')
@click.argument('dst')
def _dup(src, dst):
    """Duplicate <src> profile to <dst>"""
    pass

