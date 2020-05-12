from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class A(Base):
    __tablename__ = 'key_a'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    quantity = Column(Integer, nullable=False)


class B(Base):
    __tablename__ = 'key_b'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    type = Column(String(20), nullable=False)
    quantity = Column(Integer, nullable=False)


class C(Base):
    __tablename__ = 'key_c'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(20), nullable=False)
    code = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)


class D(Base):
    __tablename__ = 'key_d'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(20), nullable=False)
    code = Column(Integer, nullable=False)
    ip = Column(String(20), nullable=False)


class E(Base):
    __tablename__ = 'key_e'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(20), nullable=False)
    code = Column(Integer, nullable=False)
    ip = Column(String(20), nullable=False)
