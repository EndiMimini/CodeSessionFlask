from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models import dojo,ninja, user

@app.route('/ninjas')
def ninjas():
    return render_template('ninja.html', dojos= dojo.Dojo.get_all())

@app.route('/create/ninja', methods=['POST'])
def create_ninja():
    if 'user_id' not in session:
        return redirect('/logout')
    if not ninja.Ninja.validate_ninja(request.form):
        return redirect('/ninjas')
    ninja.Ninja.save(request.form)
    return redirect('/')

@app.route('/ninja/<int:id>/like', methods=['GET','PUT'])
def like_ninja(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data={
        'ninja_id': id,
        'user_id': session['user_id'],
        
    }
    myNinja= ninja.Ninja.getUsersWhoLiked(data)

    ninja.Ninja.addLike(data)
    ninja.Ninja.getUsersWhoLiked(data)

    return redirect(request.referrer)

@app.route('/ninja/<int:id>/unlike', methods=['GET','PUT'])
def unlike_ninja(id):
    if 'user_id' not in session:
            return redirect('/logout')
    data={
        'ninja_id': id,
        'user_id': session['user_id'],
    }
    user.User.unLike(data)
    return redirect(request.referrer)