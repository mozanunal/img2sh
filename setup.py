#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='img2sh',
    version=__import__('img2sh').__version__,
    description=(
        'Show images directly on terminal using Xterm colors.'
    ),
    long_description=open('README.md').read(),
    author="Mehmet Ozan Unal",
    author_email='mehmetozanunal@gmail.com',
    maintainer="Mehmet Ozan Unal",
    maintainer_email='mehmetozanunal@gmail.com',
    license="MIT",
    packages=find_packages(),
    platforms=["all"],
    url='http://github.com/peter-wangxu/persist-queue',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Topic :: Software Development :: Libraries'
    ],
    entry_points={
        'console_scripts': ['img2sh=img2sh.cli:main'],
    },
)
