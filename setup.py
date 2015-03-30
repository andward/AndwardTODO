#!/usr/bin/env python

from setuptools import setup, find_packages
import todo

setup(
    name='Andward.TODO',
    version='1.0',
    description='A TODO management and assignment system for Django.',
    author='Andward Xu',
    author_email='xulei.basketball@gmail.com',
    url=__url__,
    license=__license__,
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)