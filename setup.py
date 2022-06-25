# Copyright (C) 2022 by Vd.
#
# This file is part of AsyncChainedCallWrapper, a small library that allows you to make chained calls of asynchronous
# functions.
#
# AsyncChainCall is released under the MIT License (see LICENSE).


from os.path import join, dirname

import setuptools

setuptools.setup(
    name='AsyncChainedCall',
    version='0.0.0',
    author='Vd',
    author_email='vd@vd2.org',
    url='https://github.com/vd2org/async-chained-call',
    license='MIT',
    description='A small library that allows you to make chained calls of asynchronous functions.',
    long_description=open(join(dirname(__file__), 'README.md')).read(),
    long_description_content_type='text/markdown',
    packages=setuptools.find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Utilities',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
