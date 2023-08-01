from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase


config = {
  "apiKey": "AIzaSyA_sYbPLjQre0ev6vRt1JORu3XKW17LWBY",
  "authDomain": "tech2peace-e783d.firebaseapp.com",
  "databaseURL": "https://tech2peace-e783d-default-rtdb.europe-west1.firebasedatabase.app",
  "projectId": "tech2peace-e783d",
  "storageBucket": "tech2peace-e783d.appspot.com",
  "messagingSenderId": "392709059440",
  "appId": "1:392709059440:web:928f231b1e63be219c55b5",
  "measurementId": "G-BL7GJ7GH6Y"
}
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apply', methods=['GET', 'POST'])
def apply():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        age = request.form['age']
        interest = request.form['interest']
        message = request.form['message']
        card = request.form['card']
        person = {"first_name": firstname,"last_name": lastname,"email": email,"phone": phone,"age": age,"interest": interest,"message": message,"card":card,"admin":False}
        db.child('People').push(person)
    return render_template('apply.html')

@app.route('/donate', methods=['GET', 'POST'])
def donate():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        message = request.form['message']
        card = request.form['card']
        amount=request.form['amount']
        bank=request.form['bank']
        donator = {"first_name": firstname,"last_name": lastname,"email": email,"phone": phone,"message": message,"card":card,"amount":amount,"bank":bank}
        db.child('Donations').push(donator)
    return render_template('donate.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        phone = request.form['phone']
        card = request.form['card']       
        if "ayoub"==firstname and "ayoub"==lastname and "1904ayoub@gmail.com"==email and "+9725491904574"==phone and "fpdmvpo1224"==card :
            person1=db.child("People").get().val()
            try:
                donator1=db.child("Donations").get().val()
                return render_template('info.html', person1=person1,donator1=donator1, is_donate = True)
            except:
                return render_template('info.html', person1=person1, is_donate = False)

    return render_template("admin.html")
if __name__ == '__main__':
    app.run(debug=True)