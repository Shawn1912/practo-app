import psycopg2
from flask import Flask, request, render_template,session,logging,url_for,redirect
import smtplib
from email.message import EmailMessage
import random
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

from other import user_email_id, user_pwd, nums

connect = psycopg2.connect(
		user = "postgres",
		password = "postgres",	
		host = "localhost",
		port = "5432",
		database = "practo_db")

cursor = connect.cursor()	
	
app = Flask(__name__)

@app.route('/login')
def login():
	return render_template('login.html')

@app.route('/validate-login', methods = ['POST'])
def loginValidatePost():
	error = None
	name = request.form['Email']
	pas = request.form['Password']
	query = '''SELECT * FROM users WHERE email = %s AND pass =%s '''
	cursor.execute(query,(name,pas))	
	user = cursor.fetchall()
	if len(user) == 0:
		error = "Invalid Details. Please try again"
		return render_template('login.html', error=error)
	else:
		return render_template('home.html')	

@app.route('/register')
def register():
	return render_template('register.html')

@app.route('/validate-register', methods = ['POST'])
def registerValidatePost():
	error = None
	new_name = request.form['Username']
	new_email = request.form['Email']
	new_phone = request.form['Number']
	new_city = request.form['City']
	new_gender = request.form['Gender']
	new_college = request.form['College']
	new_qualify = request.form['Qualify']
	new_exp = request.form['Experience']
	new_pass = request.form['Password']
	confirm = request.form['ConPassword']
	special = request.form['Specialty']
	FileImage = request.files["file_image"].read()

	if new_pass != confirm:
		error = "Password does not match. Please try again"
		return render_template('register.html', error=error)
	# if len(new_email) == 0 or len(new_pass) == 0 or len(new_name) == 0 or len(new_phone) == 0 or len(new_city) == 0 or len(new_college)==0 or len(special) == 0 or len(new_gender) == 0 or len(FileImage) == 0 or len(new_exp) == 0 or len(new_qualify) == 0:
	if len(new_email) == 0 or len(new_pass) == 0 or len(new_name) == 0 or len(new_phone) == 0 or len(new_city) == 0 or len(new_college)==0 or len(special) == 0 or len(new_gender) == 0 or len(new_exp) == 0 or len(new_qualify) == 0:
		error = "Invalid Details. Please try again"
		return render_template('register.html', error=error)	
	query = '''SELECT * FROM users WHERE email = %s '''	
	cursor.execute(query,(new_email,))

	isuser = cursor.fetchall()
	if len(isuser) == 0:	
		insert_query = ''' INSERT INTO users (email,pass,name,phone,gender,special,city,college,qualification,experience,img) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
		values = (new_email,new_pass,new_name,new_phone,new_gender,special,new_city,new_college,new_qualify,new_exp,FileImage)
		cursor.execute(insert_query,values)
		connect.commit()
		return render_template('home.html')
	else:
		error = "User Exists. Please try again"
		return render_template('register.html', error=error)	

@app.route('/forgot-password')
def forgotPassword():
	return render_template('forgot_password.html')		

@app.route('/send-email', methods = ['POST'])
def changePassword():
	ch_mail = request.form['Email']
	ch_num = request.form['Number']
	if len(ch_mail) == 0 or len(ch_num) == 0:
		error = "Invalid Details. Please try again"
		return render_template('forgot_password.html', error=error)
	forgot_query = ''' SELECT * FROM users WHERE email LIKE '{}' AND phone LIKE '{}' '''.format(ch_mail,ch_num)
	cursor.execute(forgot_query)
	user_pass = cursor.fetchall()
	if len(user_pass) != 0 :
		# error = "Your password is "+user_pass[0][1]
		# return render_template('forgot_password.html', error=error)

		#The mail addresses and password
		sender_address = user_email_id
		sender_pass = user_pwd
		receiver_address = 'shawnlouis2000@gmail.com'

		# generating email OTP
		# selects a random number from a list(nums) in other.py file
		# this method will be used only for testing purposes
		email_otp = random.choice(nums)
		content = ("Greetings from SequelString's copy of Practo App!!" + "\n" + "Use this OTP to sign in to your Practo account! Do not Share this code: " + str(email_otp))

		msg = EmailMessage()
		msg["Subject"] = "OTP Verification For SequelString's Doctor App Login."
		msg["From"] = sender_address
		msg["To"] = receiver_address
		msg.set_content(content)

		with smtplib.SMTP(
			"smtp.gmail.com", 587
		) as smtp:  # make sure to enable "less secure apps" on google before sending (not recievig) mail , link:https://myaccount.google.com/lesssecureapps
			smtp.ehlo()
			smtp.starttls()
			smtp.ehlo()

			smtp.login(sender_address, sender_pass)
			smtp.send_message(msg)
		print("Email OTP : ", email_otp)

		return redirect(url_for("otp"))
	else:
		error = "Username and phone number does not match. Please Try again."
		return render_template('forgot_password.html', error=error)	

@app.route('/otp', methods = ['POST'])
def otp():
	return render_template('password_otp.html')



if __name__ =="__main__":
	app.run(debug=True)

cursor.close()
connect.close()


