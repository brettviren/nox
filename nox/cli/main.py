from . import _click as click

@click.group()
def main():
    """The Nox Package System."""
    click.echo('Hello World!')
