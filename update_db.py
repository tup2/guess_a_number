import time

from database_access import update_prizes_table

for i in range(100):
	time.sleep(86400)
	update_prizes_table()

