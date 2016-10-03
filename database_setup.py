from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base = declarative_base()
Session = sessionmaker()

class Player(Base):
	__tablename__ = 'players'

	indx = Column(Integer, primary_key=True, autoincrement=True)
	name = Column(String)
	password = Column(String)
	Max_level = Column(Integer, ForeignKey('prizes.level'))

	def __repr__(self):
		return "<Player(name={0}, max_level={1})>".format(self.name, self.Max_level)

class Prize(Base):
	__tablename__ = 'prizes'

	level = Column(Integer, primary_key=True)
	prize = Column(Integer)

	def __repr__(self):
		return "<Prize(level={0}, prize={1})>".format(self.level, self.prize)

def setup_prize(engine):
	Session.configure(bind=engine)
	session = Session()
	session.add_all([
		Prize(level=10, prize=1),
		Prize(level=100, prize=10),
		Prize(level=1000, prize=100),
		Prize(level=10000, prize=1000)
		])
	session.commit()

if __name__ == '__main__':
	engine = create_engine('postgresql://user1:user1@127.0.0.1:5432/guess_num')
	Base.metadata.create_all(engine)
	setup_prize(engine)