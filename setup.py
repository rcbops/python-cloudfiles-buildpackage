#!/usr/bin/python
from setuptools import setup, find_packages
from cloudfiles.consts import __version__

setup(name='python-cloudfiles',
      version=__version__,
      description='CloudFiles client library for Python',
      classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: System :: Distributed Computing',
        'Topic :: Utilities',
        ],
      author='Rackspace',
      author_email='please_report_on_github@rackspace.com',
      url='https://github.com/rackspace/python-cloudfiles',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[],
      setup_requires=[],
      test_suite='nose.collector',
      namespace_packages=[],
      )
