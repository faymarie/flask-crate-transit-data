import time
from flask import (render_template, request, Blueprint, 
                    redirect, url_for, current_app, flash)
from transitdata import db
from transitdata.models import Agency
from transitdata.main.utils import insert_transitdata

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        try:
            insert_transitdata()
            flash('All data has been inserted.', 'success')
            time.sleep(10)
            
            return redirect(url_for('main.success'))
        except:
            flash('Error inserting data', 'error')

            return render_template('home.html')
    elif request.method == 'GET':  

        return render_template('home.html')

@main.route('/success')
def success():
    agencies = db.session.query(Agency).limit(10).all()
   
    return render_template('success.html', title='Success', agencies=agencies)
