
from flask import render_template, request, Blueprint, redirect, url_for, current_app, flash
from transitdata.main.utils import insert_transitdata

# from flask import (render_template, request, url_for, 
#                   redirect, g as app_globals, 
#                   make_response, jsonify, flash)


main = Blueprint('main', __name__)


tiles = [
    {
        'author': 'Marie Klaus',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'December 25, 2019'
    },
    {
        'author': 'Klausmausi',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'May 01, 2018'
    },
]

@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            insert_transitdata()
            flash('All data has been inserted.', 'success')
        except:
            flash('Error inserting data', 'error')
        return render_template('home.html')
    elif request.method == 'GET':  
        return render_template('home.html')

@main.route('/success')
def success():
        return render_template('success.html', title='Success', tiles=tiles)