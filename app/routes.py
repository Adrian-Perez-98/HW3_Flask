from flask import render_template, redirect

from app import db
from app import app
from app.forms import MessageForm
from app.models import User, Messages


# add route '/' and also add the two methods to handle request: 'GET' and 'POST'
@app.route("/", methods=['GET', 'POST'])
def home():
    form = MessageForm()
    if form.validate_on_submit():
        # create row in Message table with user (created/found) add to ta database
        user = User.query.filter_by(username=form.author.data).first()    # check if user exits in database
        if user is None:  # if not create user and add to database
            u = User(author=form.author.data)  # create new user with form info
            db.session.add(u)
            db.session.commit()

        message = Messages(message=form.message, user_id=user)

    posts = [
        {
            'author': 'Carlos',
            'message': 'Yo where you at!'
        },
        {
            'author': 'Jerry',
            'message': 'Home. You?'
        }
    ]
    # output all messages
    # create a list of dictionaries with the following structure
    # [{'author':'carlos', 'message':'Yo! Where you at?!'},
    #  {'author':'Jerry', 'message':'Home. You?'}]

    return render_template('home.html', posts=posts, form=form)
