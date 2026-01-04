from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

from app.Database.DataBaseSqlAlchemy import Base


class Comment(Base):
    __tablename__ = "comment"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    post = Column(String, nullable=False)
    likescount = Column(Integer, nullable=True)




    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))


class Hosts(Base):
    __tablename__ = "hosts"

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    params = Column(String, nullable=False)
    name = Column(String, nullable=True)
    region = Column(String, nullable=True)



    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))

class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))