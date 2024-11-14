import sys
from codecs import open
from os import path

from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = ['tests']

needs_mock = sys.version_info < (3, 3)
mock = ['mock'] if needs_mock else []

here = path.abspath(path.dirname(__file__))

version = "2.2.5"

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='telesign',
      version=version,
      description="TeleSign SDK",
      license="MIT",
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: MIT License",
          "Natural Language :: English",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2",
          "Programming Language :: Python :: 2.6",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3",
          "Programming Language :: Python :: 3.3",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
      ],
      long_description=long_description,
      keywords='telesign, sms, voice, mobile, authentication, identity, messaging',
      author='TeleSign Corp.',
      author_email='support@telesign.com',
      url="https://github.com/telesign/python_telesign",
      install_requires=['requests'],
      test_suite='nose.collector',
      tests_require=['nose', 'pytz'] + mock,
      packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
      )
