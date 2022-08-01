from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
  return 'welcome'

@app.route('/welcome/home')
def welcome_home():
  return welcome() + ' home'

@app.route('/welcome/back')
def welcome_back():
  return welcome() + ' back'