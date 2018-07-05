# -*- coding: utf-8 -*-
# pylint: disable=broad-except
"""qatestlink module can be installed and configured from here"""

from os import path
from setuptools import setup, find_packages
from testlinktests.core.utils import read_file
from testlinktests.core.utils import path_format


VERSION = '0.0.0'
CURR_PATH = "{}{}".format(path.abspath(path.dirname(__file__)), '/')


def read(file_name=None, is_encoding=True, ignore_raises=False):
    """Read file"""
    if file_name is None:
        raise Exception("File name not provided")
    if ignore_raises:
        try:
            return read_file(is_encoding=is_encoding,
                             file_path=path_format(
                                 file_path=CURR_PATH,
                                 file_name=file_name,
                                 ignore_raises=ignore_raises))
        except Exception:
            # TODO: not silence like this,
            # must be on setup.cfg, README path
            return 'NOTFOUND'
    return read_file(is_encoding=is_encoding,
                     file_path=path_format(
                         file_path=CURR_PATH,
                         file_name=file_name,
                         ignore_raises=ignore_raises))


setup(
    name='testlinktests',
    version=VERSION,
    license=read("LICENSE", is_encoding=False, ignore_raises=True),
    packages=find_packages(exclude=['tests']),
    description='Main automation lib to ensure behaviour of Testlink WebApp',
    long_description=read("README.rst"),
    author='TestLinkOpenSourceTRMS',
    author_email='netzuleando@gmail.com', # Can be replaced
    url='https://github.com/TestLinkOpenSourceTRMS/testlink-tests',
    download_url=("https://github.com/TestLinkOpenSourceTRMS"
                  "/testlink-tests/tarball/v{}").format(VERSION),
    keywords=[
        'testing',
        'logging',
        'functional',
        'http',
        'test',
        'testlink',
        'XMLRPC',
        'requests',
        'webapp',
        'selenium',
        'functional'
    ],
    install_requires=[
        'qatestlink'
    ],
    setup_requires=[
        'tox',
        'pytest-runner',
    ],
    tests_require=[
        'pytest',
        'pytest-raises',
        'pytest-html',
        'pytest-dependency',
        'pytest-benchmark',
        'pytest-benchmark[histogram]',
        'coverage==4.3.4',
        'pytest-cov==2.5.0',
        'flake8'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)