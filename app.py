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
        person = {"first_name": firstname,"last_name": lastname,"email": email,"phone": phone,"age": age,"interest": interest,"message": message}
        db.child('People').push(person)
    return render_template('apply.html')

if __name__ == '__main__':
    app.run(debug=True)