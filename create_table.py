import psycopg2

connection = psycopg2.connect(
	user = "postgres",
	password = "postgres",    #enter postgres password here
	host = "localhost",
	port = "5432",
	database = "practo_db")

cursor = connection.cursor()

table_query = ''' CREATE TABLE users 
	(email TEXT PRIMARY KEY NOT NULL,
	pass TEXT NOT NULL,
	name TEXT NOT NULL,
	phone TEXT NOT NULL,
	gender TEXT NOT NULL,
	special TEXT NOT NULL,
	city TEXT NOT NULL,
	qualification TEXT NOT NULL,
	college TEXT NOT NULL,
	experience TEXT NOT NULL,
	img BYTEA NOT NULL);'''
cursor.execute(table_query)
connection.commit()
print("created")	
cursor.close()
connection.close()	