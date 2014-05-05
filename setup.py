from setuptools import setup, find_packages

setup(
    name='nox',
    version='0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        nox-store=nox.cli.store:main
        nox-profile=nox.cli.profile:main
    ''',
)
