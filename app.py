from flask import Flask, session, render_template, request, redirect,flash,url_for
import pyrebase
import traceback

app = Flask(__name__)

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

app.secret_key = 'secret'

@app.route('/', methods=['GET', 'POST'])
def index():
  if ('user' in session):
    print (session["user"])
    
    return f"""Hi, {session['user']}
    <br>
    <a href="/logout">Logout!</a>
    """

  if request.method == "POST":
    print("eeeee")
    email = request.form.get('email')
    password = request.form.get('password')
    print(email)
    print(password)
    try:
      user = auth.sign_in_with_email_and_password(email, password)
      session['user'] = email
      return redirect(url_for('index'))
    except Exception as e:
      print(e)
      print(type(traceback.format_exc()))
      flash('You were not successfully logged in')
      return redirect(url_for('index'))
  return render_template('home.html')
  
@app.route('/logout', methods=['GET', 'POST'])
def logout():
  session.pop('user')
  return redirect('/')
  # return render_template('home.html')

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)