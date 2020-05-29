from sqlalchemy import Column, Integer, VARCHAR, SMALLINT, DATETIME
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class TestUsers(Base):
    __tablename__ = 'test_users'
    __table_args__ = {'mysql_charset': 'utf8'}
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(VARCHAR(16))
    password = Column(VARCHAR(255))
    email = Column(VARCHAR(64), nullable=False)
    access = Column(SMALLINT)
    active = Column(SMALLINT)
    start_active_time = Column(DATETIME)
