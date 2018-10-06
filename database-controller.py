import sqlite3
import csv

# Connect to the database
connection = sqlite3.connect('csclub.db')

# Create cursor, it is used to interact with the database
cursor = connection.cursor()

# Create the table 
# cursor.execute('CREATE TABLE community (id INTEGER PRIMARY KEY, name TEXT, school_id INTEGER, email TEXT);')

# Add a person to the database
def addMember(name, school_id, email):
	cursor.execute('SELECT id FROM community WHERE email=?', (email.lower(), ))
	member = cursor.fetchone()
	if member == None:
		cursor.execute('INSERT INTO community (name, school_id, email) VALUES(?,?,?)',(name, school_id, email.lower()))
	else:
		print("{member['email']} is already in the database. Name: {member['name']")

# Load data from csv file
def load_data(filename):
	file = open(filename, mode = 'r')
	csv_data = csv.DictReader(file)
	return csv_data

data = load_data('data.csv')
for person in data:
	addMember(person['name'], person['id'], person['email'])

# Commit changes to database
connection.commit()