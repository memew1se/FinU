from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.engine import Engine
from sqlalchemy.ext.declarative import as_declarative
from sqlalchemy.orm.session import sessionmaker, Session


@as_declarative()
class Base(object):
    id = Column(Integer(), primary_key=True, autoincrement=True)


class User(Base):
    __tablename__ = "USERS"

    nickname = Column(String(60), nullable=False, unique=True)
    password = Column(String(60), nullable=False)


class Database:
    DATABASE = 'sqlite'
    DB_NAME = 'rsc/usr.sqlite3'
    engine: Engine = create_engine(f"{DATABASE}:///{DB_NAME}", echo=False)
    session: Session = sessionmaker(bind=engine)()


if __name__ == '__main__':
    Base.metadata.create_all(Database.engine)