import psycopg2
from flask import Flask, request, render_template,session,logging,url_for,redirect
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

connect = psycopg2.connect(
		user = "postgres",
		password = "postgres",	
		host = "localhost",
		port = "5432",
		database = "img")

cursor = connect.cursor()	
	
app = Flask(__name__)

@app.route('/create')
def new_id():
	return render_template('register.html')

@app.route('/register', methods = ['GET','POST'])
def UploadImage():
    FileImage = request.files["file_image"].read()
    query = ''' INSERT INTO images(img) VALUES (%s)'''
    cursor.execute(query,(FileImage,))
    connect.commit()
    return "done"

    

def SaveToDatabase(id_item, FileImage):
    s = ""
    s += "INSERT INTO images"
    s += "("
    s += "id_item"
    s += ", img"
    s += ") VALUES ("
    s += "(%id_item)"
    s += ", '(%FileImage)'"
    s += ")"
    # We recommend adding TRY here to trap errors.
    cursor.execute(s, [id_item, FileImage])
    connect.commit()
    return "done"

if __name__ =="__main__":
	app.run(debug=True)

cursor.close()
connect.close()

