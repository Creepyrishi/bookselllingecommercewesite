from flask import request, jsonify, redirect, url_for, render_template, Flask
import os
import db
import random
import authtication

app = Flask(__name__)

@app.route("/")
def home():
    data_list = db.newBooks()
    return render_template('index.html', data_list=data_list)

#auth routes
@app.route("/auth")
def authantication():
    return render_template('auth.html')


@app.route('/signup', methods=['POST'])
def signup():

    firstname = request.form.get('form-first-name')
    lastname = request.form.get('form-last-name')
    email = request.form.get('form-email')

    try:
        
        
        return render_template('notice.html', notice='Goto mail and verify your account')
    except Exception as e:
        return render_template('notice.html', notice="Something went wrong")

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

##

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
    record = db.getid(id)
    print(record)
    return render_template('detail.html', data = record)


app.run(debug=True)