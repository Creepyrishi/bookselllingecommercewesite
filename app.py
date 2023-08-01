from flask import request, jsonify, redirect, url_for, render_template, Flask
import os
import firebase_admin
from firebase_admin import credentials, auth  # Import the 'auth' module
import db
import random
# Initialize Firebase Admin SDK with your service account key
firebase_cred_path = os.path.join(os.getcwd(), 'serviceAccountKey.json')
cred = credentials.Certificate(firebase_cred_path)
firebase_admin.initialize_app(cred)
app = Flask(__name__)

@app.route("/")
def home():
    data_list = db.newBooks()
    return render_template('index.html', data_list=data_list)

@app.route("/auth")
def authantication():

    return render_template('auth.html')


@app.route('/signup', methods=['POST'])
def signup():
    firstname = request.form.get('form-first-name')
    lastname = request.form.get('form-last-name')
    email = request.form.get('form-email')
    password = random.random().__str__()

    try:
        user = auth.create_user(
            email=email,
            password=password
        )
        auth.generate_reset_password_link(email)
        
        return render_template('notice.html', notice='Goto mail and verify your account')
    except Exception as e:
        return render_template('notice.html', notice="Something went wrong")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        user = auth.get_user_by_email(email)
        # User exists, proceed with login
        auth_user = auth.get_user(user.uid)
        return jsonify({'message': 'Logged in successfully!', 'user': auth_user.to_dict()}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 401

@app.route("/search", methods=['GET'])
def search():
    name = request.args.get('search')

    data_list = {'name':name,
                 'list':db.search(name)
                 }
    return render_template('search.html', data_list=data_list)

@app.route("/store")
def store():

    data_list = {'hot':db.hotBooks(),
                     'new':db.newBooks()
                     }

    return render_template('store.html', data_list=data_list)

@app.route("/view", methods=['GET'])
def view():
    id = request.args.get('id')
    return render_template('detail.html')
app.run(debug=True)