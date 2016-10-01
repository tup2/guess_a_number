from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()



class User(Base):
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String)

	def __repr__(self):
		return "<User(name={0}>".format(self.name)

if __name__ == '__main__':
	engine = create_engine('postgresql://stack:c#2016@127.0.0.1:5432/guess_num')
	Base.metadata.create_all(engine)