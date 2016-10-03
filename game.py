from database_access import query_prize, reset_prize, check_all_players, add_player, \
	update_player, get_password, get_level

def register_user(name = ''):
	names = check_all_players()
	while True:
		if name and name not in names:
			break
		if name in names:
			message = 'Username already taken, try another one: '
		elif not name:
			message = 'Enter a valid username: '
		try:
			name = input(message)
		except ValueError:
			message = 'Enter a valid username: '
			print('Invalid, try again')
	try:
		password = input('Enter your password: ')
	except VaueError:
		print('Invalid password, try again')
	password_again = ''
	c = 0
	while c < 5 and (not password_again or password_again != password):
		password_again = input('Enter your password again: ')
		c += 1
	if password_again == password:
		add_player(name, password)
		guess(name)
	else:
		yorn = input('start over?[y or n] ')
		if yorn.lower() in {'y', 'yes'}:
			register_user()


def log_on():
	is_new = input('New user? [y or n]: ')
	if is_new.lower() in {'y', 'yes'}:
		register_user()
	else:
		names = check_all_players()
		name = ''
		while not name:
			name = input('Enter your user name: ')
		if name not in names:
			yorn = input('Not in our database, do you want to register[y or n]: ')
			if yorn.lower() in {'y', 'yes'}:
				register_user(name)
			else:
				log_on()
		else:
			password = get_password(name)
			password_again = ''
			c = 0
			while c < 5 and (not password_again or password_again != password):
				password_again = input('Enter your password: ')
				c += 1
			if password_again == password:
				level = get_level(name) or 1
				if level == 10000:
					print('Final Prize Winner Already, relax')
				else:
					guess(name, level*10)
			else:
				print('Seems like you are having trouble retrieving your password, you could either register a new name or try again later.')
				yorn = input('Register a new name? [y/n]: ')
				if yorn.lower() in {'y', 'yes'}:
					register_user()


def guess(name, level=10):
	import random
	is_winner = False

	target = random.randint(0, level)
	count = 0
	prize = query_prize(level)
	while count < 5 and prize != 0:
		try:
			num = int(input('Guess a numer between 0 and {0}, inclusive: '.format(level)))
			count += 1
			if num == target:
				print('You Win $', prize)
				reset_prize(level)
				update_player(name, level)
				is_winner = True
				break
			prize = query_prize(level)
		except ValueError:
			print('invalid input, try again')
			count += 1
			prize = query_prize(level)
	if not is_winner and prize == 0:
		print('Other has won this prize')
	if not is_winner:
		print('Game Over ~~')



if __name__ == '__main__':
	log_on()