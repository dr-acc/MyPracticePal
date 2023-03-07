"""Models for music practice logger app."""


from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    """A musician & app user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    routines = db.relationship("Routine", back_populates="user")
    practice_sessions = db.relationship("PracticeSession", back_populates="user")
    exercises = db.relationship("Exercise", back_populates="user")

    def __repr__(self):
        return f"<User user_id={self.user_id} email={self.email}>"


class Routine(db.Model): ###A menu (lunch vs dinner)
    """A user-created grouping of skills and exercises to practice regularly."""

    __tablename__ = "routines"

    routine_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    title = db.Column(db.String) ###this will come from form
    description = db.Column(db.Text) ### form text field data

    exercises = db.Column(db.String, nullable=True)
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    user = db.relationship("User", back_populates="routines")

    # practice_sessions = db.relationship("PracticeSession", back_populates="routine")

    def __repr__(self):
        return f"<Routine routine_id={self.routine_id} title={self.title}>"


class PracticeSession(db.Model):  ###A specific meal order
    """A single log entry representing a user's practice session."""

    __tablename__ = "practice_sessions"
    
    session_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    date = db.Column(db.DateTime(), default=datetime.now, nullable=False)
    total_session_min = db.Column(db.Integer)
    on_instrument_min = db.Column(db.Integer, nullable=True)
    off_instrument_min = db.Column(db.Integer, nullable=True)
    session_challenge_level = db.Column(db.String, nullable=True)
    session_enjoyment_level = db.Column(db.String, nullable=True)
    notes_next_practice = db.Column(db.String, nullable=True)
    questions_for_teacher = db.Column(db.String, nullable=True)
    exercises_this_session = db.relationship("Exercise", back_populates="practice_session")  
    # exercises_this_session = db.Column(db.String, nullable=True)

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    user = db.relationship("User", back_populates="practice_sessions")

    # routine_id = db.Column(db.Integer, db.ForeignKey("routines.routine_id"))
    # routine = db.relationship("Routine", back_populates="practice_sessions")

    def __repr__(self):
        return f"<PracticeSession {self.session_id} Date: {self.date} Exercises: {self.exercises_this_session}>"


class Exercise(db.Model): ###the menu items ordered -- "Attributes" problem = all the details about how they are ordered
    """A specific skill or assignment"""
    __tablename__ = "exercises"

    exercise_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    ex_title = db.Column(db.String)
    bpm = db.Column(db.Integer, nullable=True)
    key_variations = db.Column(db.String, nullable=True)
    mode_variations = db.Column(db.String, nullable=True)
    direction_variations = db.Column(db.String, nullable=True)
    my_variations = db.Column(db.String, nullable=True)

    p_session_id = db.Column(db.Integer, db.ForeignKey("practice_sessions.session_id"))
    practice_session = db.relationship("PracticeSession", back_populates="exercises_this_session")

    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    user = db.relationship("User", back_populates="exercises")

    def __repr__(self):
        return f"<Exercise {self.ex_title}>"



def connect_to_db(flask_app, db_uri="postgresql:///mpp", echo=False): 
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    ###can change "echo" to True if you want to see a much more verbose readout
    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets  annoying
    # this will tell SQLAlchemy not to print out every query it executes.

    connect_to_db(app)
