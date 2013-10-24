from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/example/')
def example():
	return render_template('example.html')

@app.route('/facebook/')
def facebook():
	return render_template('facebook.html')

@app.route('/profile/')
def profile():
	return render_template('profile.html')

@app.route('/city_forum/')
def city_forum():
	return render_template('city_forum.html')

@app.route('/city_list/')
def city_list():
	return render_template('city_list.html')

@app.route('/settings/')
def settings():
	return render_template('settings.html')

@app.route('/friend_list/')
def friend_list():
	return render_template('friend_list.html')
