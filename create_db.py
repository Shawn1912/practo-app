import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

connect = psycopg2.connect(
	user = "postgres",
	password = "postgres", #enter your postgres password
	host = "localhost",
	port = "5432",
	database = "postgres"
	)
connect.autocommit = True

cursor = connect.cursor()
create = '''CREATE database practo_db2 '''
cursor.execute(create)
print("created")
cursor.close()
connect.close()