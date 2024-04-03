import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()
class Follower(Base):
    __tablename__= 'follower'
    id=Column(Integer,primary_key=True)
    user_from_id= Column(Integer,ForeignKey('user.id'))
    user_to_id=Column(Integer,ForeignKey('user.id'))


class User(Base):
    __tablename__= 'user'
    id= Column(Integer,primary_key=True)
    username= Column(String(200),nullable=False)
    firstname= Column(String(200),nullable=False)
    lastname= Column(String(200),nullable=False)
    email= Column(String(200),nullable=False)
    user_id= relationship(Follower,backref='user')
  



class Post(Base):
    __tablename__= 'post'
    id= Column(Integer,primary_key=True)
    user_id= Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    

class Comment(Base):
    __tablename__= 'comment' 
    id= Column(Integer,primary_key=True)
    comment_text= Column(String(200),nullable=False)
    post_id=Column(Integer,ForeignKey('post.id'))
    post=relationship(Post)
    author_id= Column(Integer,ForeignKey('user.id'))
    user=relationship(User)
    

class Media(Base):
    __tablename__= 'media'
    id= Column(Integer,primary_key=True)
    type= Column(String,nullable=False)
    url=Column(String,nullable=False)
    post_id=Column (Integer,ForeignKey('post.id'))
    post=relationship(Post)
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
