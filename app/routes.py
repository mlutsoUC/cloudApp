from flask import Flask, url_for, request, render_template, redirect, g, flash
from markupsafe import escape, Markup
from app import app
from app.forms import LoginForm
from app.modbd import readWeights, readParams
import time
import os
import sys
import random


@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/logo324.png')
def logoapp():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'logo32.png', type='image/png')

@app.route('/test')
def test():
    return render_template('test.html')


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Utilcell'}
    posts = [
        {
            'author': {'username': 'Michal'},
            'body': 'Hello from Flask !'
        },
        {
            'author': {'username': 'Nikola'},
            'body': 'Hello from MQTT!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/uwt6008')
def uwt():
    return render_template('uwt6008.html', weights=readWeights(), units=readParams())

@app.route('/callback')
def callback():
    print('called uwt6008')
    ... # before rendering callback
    return render_template('uwt6008.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html',  title='Sign In', form=form)

if __name__ == '__main__':
    app.run()
