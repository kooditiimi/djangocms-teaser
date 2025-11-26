#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_teaser import __version__

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Framework :: Django :: 4.0',
    'Framework :: Django :: 4.1',
    'Framework :: Django :: 4.2',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
]

setup(
    name='djangocms-teaser',
    version=__version__,
    description='Teaser plugin for django CMS',
    author='Divio AG',
    author_email='info@divio.ch',
    url='https://github.com/divio/djangocms-teaser',
    packages=[
        'djangocms_teaser',
        'djangocms_teaser.migrations',
    ],
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'django-cms>=4.0',
        'Django>=4.0',
        'Pillow',
    ],
    python_requires='>=3.8',
)
