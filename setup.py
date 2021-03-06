import os
from carbonate import __version__
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="carbonate",
    version=__version__,
    author="Scott Sanders",
    author_email="scott@jssjr.com",
    description=("Tools for managing federated carbon clusters."),
    license = "MIT",
    keywords = "graphite carbon",
    url = "https://github.com/jssjr/carbonate",
    include_package_data = True,
    packages=find_packages(),
    long_description = read('README.txt'),
    #install_requires = [
    #  "carbon >= 0.9.12",
    #  "whisper >= 0.9.12",
    #],
    entry_points = {
        'console_scripts': [
            'carbon-lookup = carbonate.lookup:main',
            'carbon-sync = carbonate.sync:main',
            'carbon-sieve = carbonate.sieve:main',
            'carbon-list = carbonate.list:main',
            'carbon-hosts = carbonate.hosts:main',
            'whisper-fill = carbonate.fill:main',
            'whisper-aggregate = carbonate.aggregation:main'
            ]
        }
    )
