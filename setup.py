##############################################################################
#
# Copyright (c) 2008 Zope Corporation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################

import os
from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(here, 'README.txt')).read()
CHANGES = open(os.path.join(here, 'CHANGES.txt')).read()

long_description = "\n\n".join((README, CHANGES))
long_description = long_description.decode('utf-8')

install_requires =[
    'setuptools',
    'Chameleon',
    'zope.interface',
    'zope.component',
    'zope.configuration',
    'zope.security',
    'zope.testing',
    'repoze.bfg',
    ]

setup(name='repoze.bfg.skins',
      version = '0.17',
      description='Skin support for BFG.',
      long_description=long_description,
      keywords = "zope3 repoze bfg",
      classifiers = [
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Zope Public License',
          'Programming Language :: Python',
          'Natural Language :: English',
          'Operating System :: OS Independent',
          'Topic :: Internet :: WWW/HTTP',
          'Framework :: Zope3'],
      license='BSD',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['repoze', 'repoze.bfg'],
      install_requires=install_requires,
      include_package_data = True,
      zip_safe = False,
      tests_require = install_requires + [
          'manuel',
          'zope.testing==3.8.3',
          'zope.interface==3.5.2',
          'zope.component==3.7.1',
          'zope.security==3.7.1',
          'zope.i18n==3.7.1',
          'pyfsevents==0.3dev',
          ],
      test_suite="repoze.bfg.skins.tests",
      )
