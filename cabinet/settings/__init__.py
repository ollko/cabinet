import pymysql

pymysql.install_as_MySQLdb()

import MySQLdb

from .base import *

from .production import *

try:
   from .local import *
except:
	pass