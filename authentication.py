from flask import Flask, session, render_template, request, redirect
import pyrebase

config = {
  "apiKey":"AIzaSyDXjvxMN5YUtXnr5z_RnVG8m0x_fWziLLQ",
  "authDomain": "farialimajobsadmin.firebaseapp.com",
  "projectId": "farialimajobsadmin",
  "storageBucket": "farialimajobsadmin.appspot.com",
  "messagingSenderId": "26442600891",
  "appId": "1:26442600891:web:787a9f63fa8012be28349e",
  "measurementId": "G-3RFQV2Z2V7",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email='fernaoguerra@gmail.com'
password = '123456'

user = auth.create_user_with_email_and_password(email, password) 
print(user)

# user = auth.sign_in_with_email_and_password(email, password)