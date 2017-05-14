#! python.exe
#  coding=utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import ConfigParser
BaseModel = declarative_base()
cp = ConfigParser.SafeConfigParser()
cp.read("../config/develop.conf")
dbconnectStr = 'mysql+mysqldb://%s:%s@%s/%s?charset=utf8' % (cp.get("db", "user"), cp.get("db", "pass"),
                                                             cp.get("db", "host"), cp.get("db", "db"))
engine = create_engine(dbconnectStr, echo=False)
DB_Session = sessionmaker(bind=engine)
session = DB_Session()
