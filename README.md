# guess_a_number

# guess a number and win the prize!

# There are 4 levels: 10, 100, 1000 or 10000

# At level 10, a random number n is generated, 0 <= n <= 10, you get 5 chances to guess the number.
# Guess correct, the prize is yours!
# The prize for level 10 is $1, and increased $1 every 24 hours if nobody won the game, until $10.
# If somebody else guess right and take the prize, you have to wait 24 hours for the prize to increase to $1

# At level 100, guess a number n, 0 <= n <= 100, the prize started at $10 and increased $10 every 24 hours until $100
# At level 1000, guess a number n, 0 <= n <= 1000, the prize started at $100 and increased $100 every 24 hours until $1000
# At level 10000, guess a number n, 0 <= n <= 10000, the prize started at $1000 and increased $1000 every 24 hours until $10000

# Go to a higher level after you conquered the lower one and make your best guess

# ########################## #
# Backend database PostgreSQL
# Code is written in Python3 and requires library sqlAlchemy

# ########################## #
# How to Play
# 1. postgresql, python3 and sqlalchemy are pre-required
# 2. create database guess_num, and assign it to user1 with password: user1 in your database
# 3. run database_setup.py to create the database schema and initialize the prizes table
# 4. run update_db.py at background(recommend) to update the prize tables every 24 hours
# 5. start playing by running game.py
		you will be prompted to register with a user name and password
		you could login later with the user name/password to continue to a higher level
