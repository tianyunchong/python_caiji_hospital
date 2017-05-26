#! python
# coding=utf-8

import sys,os
sys.path.append(os.path.dirname(os.getcwd()))
from models.hospital import *
print Hospital.__tablename__
