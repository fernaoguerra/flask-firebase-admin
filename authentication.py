from flask import Flask, session, render_template, request, redirect
import pyrebase

config = {
  "apiKey":"add your firebase info here",
  "authDomain": "add your firebase info here",
  "projectId": "add your firebase info here",
  "storageBucket": "add your firebase info here",
  "messagingSenderId": "add your firebase info here",
  "appId": "add your firebase info here",
  "measurementId": "add your firebase info here",
  "databaseURL": ""
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

email='youremail@gmail.com'
password = '123456'

# Use this to create a user with email 
user = auth.create_user_with_email_and_password(email, password) 
print(user)

