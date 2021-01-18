from . import app
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy(app)

# create user 'mysql'@'localhost' identified by 'pass';
# create database lifehack;
# grant all on lifehack.* to mysql@localhost;
# from backend.models import init
# init()

def init():
    db.create_all()


class Test(db.Model):
    __tablename__ = 'tests'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(1000))
    number = db.Column(db.Integer)

    def to_dict(self):
        return dict(
            id=self.id,
            text=self.text,
            number=self.number
        )

    def __repr__(self):
        return '<Test %r, %r, %r>' % self.id, self.text, self.number

class Users(db.Model):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100))
    user_name = db.Column(db.String(100))
    password = db.Column(db.String(100))

    def to_dict(self):
        return dict(
            id=self.id,
            email=self.email,
            user_name=self.user_name,
            password=self.password
        )

    def __repr__(self):
        return '<Test %r>' % self.id

class Clothes(db.Model):
    __tablename__ = 'clothes'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer,
                    db.ForeignKey(
                            'users.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
                        )
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)
    category = db.Column(db.String(100))
    image_name = db.Column(db.String(100))
    repeat = db.Column(db.String(100))

    def to_dict(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            name=self.name,
            price=self.price,
            category=self.category,
            image_name=self.image_name,
            repeat=self.repeat
        )

    def __repr__(self):
        return '<Test %r>' % self.id



class Tag(db.Model):
    __tablename__ = 'tags'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    tag_name = db.Column(db.String(100))
    clothes_id = db.Column(db.Integer,
                        db.ForeignKey(
                            'clothes.id',
                            onupdate='CASCADE',
                            ondelete='CASCADE')
                        )

    def to_dict(self):
        return dict(
            id=self.id,
            tag_name=self.tag_name,
            clothes_id=self.clothes_id
        )

    def __repr__(self):
        return '<Tag %r>' % self.tag_name


class Like(db.Model):
    __tablename__ = 'likes'
    __table_args__ = {'extend_existing': True}
    liker_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'users.id',
            onupdate='CASCADE',
            ondelete='CASCADE'
        ),
        primary_key=True
    )
    clothes_id = db.Column(
        db.Integer,
        db.ForeignKey(
            'clothes.id',
            onupdate='CASCADE',
            ondelete='CASCADE'
        ),
        primary_key=True
    )

    def to_dict(self):
        return dict(
            liker_id=self.liker_id,
            clothes_id=self.clothes_id
        )

    def __repr__(self):
        return '<Like %r, %r>' % self.liker_id



class Follow(db.Model):
    __tablename__ = 'follow'
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    followee_id = db.Column(db.Integer,
                            db.ForeignKey(
                                'users.id',
                                onupdate='CASCADE',
                                ondelete='CASCADE')
                            )
    follower_id = db.Column(db.Integer,
                            db.ForeignKey(
                                'users.id',
                                onupdate='CASCADE',
                                ondelete='CASCADE')
                            )

    def to_dict(self):
        return dict(
            id=self.id,
            followee_id=self.followee_id,
            follower=self.follower_id
        )

    def __repr__(self):
        return '<Follow %r %r>' % self.follower_id, self.followee_id
