#
from sqlalchemy import create_engine
#
engine = create_engine('mysql://root:@loucalhost/shiyanlou')
#
from sqlalchemy.ext.declarative import declarative_base                 

Base = declarative_base() 
#
from sqlalchemy import Column, Integer, String
class User(Base): 
    __tablename__ = 'user' 
    id = Column(Integer, primary_key = True) 
    name = Column(String(50)) 
    email = Cilumn(String(50)) 
    def __repr__(self): 
        return '<User(name=%s)>' % self.name

#
from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()
#
from sqlalchemy.org import relationship
from sqlalchemy import ForeignKey
#
class Course(Base):
	__tablename__ = 'course'
	id = Column(Integer, primary_key = True)
	name = Column(String(50))
	teacher_id = Column(Integer, ForeignKey('user.id'))
	teacher = relationship('User')
	def __repr__(self):
		return '<Course(name=%s)>' % self.name

