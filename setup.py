from setuptools import setup, find_packages
from easy_karabiner.__version__ import __version__

setup(
    name='easy_karabiner',
    version=__version__,
    description='A tool to generate key remap configuration for Karabiner',
    author='loggerhead',
    author_email='i@loggerhead.me',
    url='https://github.com/loggerhead/Easy-Karabiner',
    keywords=('Karabiner', 'configer', 'remap', 'key'),
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=[
        'xmlformatter >= 0.1.1',
        'docopt >= 0.6.1',
    ],
    entry_points='''
        [console_scripts]
        easy_karabiner=easy_karabiner:main
    '''
)