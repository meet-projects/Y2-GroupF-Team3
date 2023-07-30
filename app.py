from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    # Handle form submission here
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)