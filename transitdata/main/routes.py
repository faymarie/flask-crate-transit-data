from flask import render_template, request, Blueprint, redirect, url_for
from transitdata.models import Tile

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
        # posts = Post.query.all()
        # insert data
        # posts.save()
        # flash('The data has been inserted!', 'success')
        return redirect(url_for('home'))
    elif request.method == 'GET':
        # tiles = Tile.query.all()
        return render_template('home.html', tiles=tiles)