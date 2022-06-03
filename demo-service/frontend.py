import code
import random
from flask import Flask, request, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os
import sys
import json
import uuid
import boto3
import names
import logging

app = Flask(__name__)

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

aws_region = os.getenv("AWS_DEFAULT_REGION", default='eu-west-1')

# -------------------------    Secrets Retrieval       ------------------------
sm_client = boto3.client('secretsmanager')

secret_arn = os.getenv("DEMO_DB_SECRET_ARN")
response = sm_client.get_secret_value(SecretId=secret_arn)
secret = json.loads(response['SecretString'])

# ------------------    Aurora (PostgreSQL Database)     -------------------------
DB_URL = f"postgresql://{secret['username']}:{secret['password']}@{secret['host']}/{secret['dbname']}"
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL

db = SQLAlchemy(app)

class UserModel(db.Model):
    __tablename__ = 'users'
    email = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String())

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __repr__(self):
        return f"<User {self.email}>"
    
# ----------------------         Main Page         ----------------------------
@app.route('/', methods=["GET", "POST"])
def create_user():

     # When "Send" button is clicked
    if request.method == 'POST':
        
        # Get data from form
        new_customer = UserModel(
            name=request.form['user'],
            email=request.form['email']
        )
        
        db.session.add(new_customer)
        db.session.commit()
    
        return users() #redirect(url_for('create_user'))

    
    # Generate a random name and amount to prepopulate the text box
    first_name = names.get_first_name()
    last_name = names.get_last_name()
    name = f'{first_name} {last_name}'
    email = f'{first_name.lower()}_{last_name.lower()}@mydomain.com'
       
    return render_template('index.html', user=name, email=email)

# -------------------      Request Redirection Page      ------------------------
@app.route('/users')
def users():
    users = UserModel.query.all()
    return render_template('users.html', users=users)

if __name__ == '__main__':
    db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=False)
    