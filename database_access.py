from sqlalchemy import create_engine, MetaData
from sqlalchemy import Table, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from database_setup import Prize, Player

Base = declarative_base()
engine = create_engine('postgresql://stack:c#2016@127.0.0.1:5432/guess_num')
Session = sessionmaker(bind=engine)

def query_prize(level):
	session = Session()
	return session.query(Prize).filter_by(level=level).first().prize


def reset_prize(level):
	print('in reset_prize')
	session = Session()
	q = session.query(Prize).filter_by(level=level).first()
	q.prize = 0
	session.commit()


def update_prize(level):
	session = Session()
	q = session.query(Prize).filter_by(level=level).first()
	if q.prize < level:
		q.prize += (level // 10)
		session.commit()


def update_prizes_table():
	for level in [10, 100, 1000, 10000]:
		update_prize(level)


def add_player(name, password):
	session = Session()
	session.add(Player(name = name, password = password))
	session.commit()


def update_player(name, level):
	print('in update_player')
	session = Session()
	q = session.query(Player).filter_by(name=name).first()
	q.Max_level = level
	session.commit()


def get_level(name):
	session = Session()
	return session.query(Player).filter_by(name=name).first().Max_level

def check_all_players():
	session = Session()
	q = session.query(Player).all()
	return [player.name for player in q]


def get_password(name):
	session = Session()
	return session.query(Player).filter_by(name=name).first().password


if __name__ == "__main__":
	update_prizes_table()
	print(query_prize(10))



