from sqlalchemy import Column, Integer, String

from database.app import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String)
