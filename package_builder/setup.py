from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'EPA NCC Python Implementation'

setup(
    name = "epa_ncc",
    version = VERSION,
    author = 'Aubrey Leary',
    author_email='leary.aubrey@epa.gov',
    description= DESCRIPTION,
    packages= ['ncc_categories'],
    package_data = {'ncc_categories':['data/raw/*']},
    include_package_data = True,
    install_requires = ['pandas','rdkit','numpy','datetime','pathlib', 'regex'],
    keywords = ['chemical', 'categories','python']
)