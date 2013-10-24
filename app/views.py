from app import app
from flask import render_template

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/city_forum/')
def city_forum():
	return render_template('city_forum.html')

@app.route('/city_forum_discussion/')
def city_forum_discussion():
	return render_template('city_forum_discussion.html')

@app.route('/city_list/')
def city_list():
	return render_template('city_list.html')

@app.route('/example/')
def example():
	return render_template('example.html')

@app.route('/facebook/')
def facebook():
	return render_template('facebook.html')

@app.route('/friend_list/')
def friend_list():
	return render_template('friend_list.html')

@app.route('/friend_profile/')
def friend_profile():
	return render_template('friend_profile.html')

@app.route('/friend_profile/')
def friend_profile():
	return render_template('friend_profile.html')

@app.route('/log_in/')
def log_in():
	return render_template('log_in.html')

@app.route('/nearby_traveler/')
def nearby_traveler():
	return render_template('nearby_traveler.html')

@app.route('/non_friend_profile/')
def non_friend_profile():
	return render_template('non_friend_profile.html')

@app.route('/private_message/')
def private_message():
	return render_template('private_message.html')

@app.route('/profile/')
def profile():
	return render_template('profile.html')

@app.route('/profile_edit/')
def profile_edit():
	return render_template('profile_edit.html')

@app.route('/settings/')
def settings():
	return render_template('settings.html')