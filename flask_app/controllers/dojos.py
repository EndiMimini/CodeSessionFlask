from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.user import User
from flask_app.models.ninja import Ninja

@app.route('/create/dojo', methods = ['POST'])
def create_dojo():
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'user_id': session['user_id'],
        'name': request.form['name']
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojo/<int:id>')
def show_dojo(id):
    data={
        'id': id,
        'user_id': session['user_id'] 
    }
    
    user = User.get_by_id(data)
    myDojo=Dojo.get_one_with_ninjas(data)
    return render_template('dojo.html', user=user, dojo=myDojo)









