# -*- coding: utf-8 -*-
from setuptools import setup

import datetime
import os

import redirector

package_list = []
for root, dirs, files in os.walk('src'):
    for dir_ in dirs:
        if dir_ != '__pycache__':
            package_list.append(os.path.relpath(root + os.path.sep + dir_, 'src').replace(os.path.sep,'.'))

setup(
    name = 'Redirector',
    version = tm.__version__ + 'dev-' + datetime.datetime.now().strftime("%Y%m%d"),
    #version = tm.__version__ + 'b1',
    #version = tm.__version__,
    packages = package_list,
    package_dir = {'redirector': os.path.join('src','tm')},
)
