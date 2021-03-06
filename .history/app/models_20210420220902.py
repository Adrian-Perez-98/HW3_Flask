from app import db

class User(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)
    # author (string, unique, can't be null)
    author = db.Column(db.String, nullable=False, unique=True)
    # message (linkd to Messages table)
    message = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.author}>'

class Messages(db.Model):
    # have the following columns
    # id (int)
    id = db.Column(db.Integer, primary_key=True)
    # message (string, not unique, can't be null)
    # user_id link to id (int)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    # write __repr__ that outputs
    def __repr__(self):
        return '<Message {}>'.format(self.body)
    # <Message: MESSAGE_GOES_HERE>
    # replace MESSAGE_GOES_HERE with the message
