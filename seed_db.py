import os
from model import connect_to_db, db, User, Exercise, Routine, PracticeSession
from server import app


os.system("dropdb mpp")
os.system("createdb mpp")

connect_to_db(app)
app.app_context().push()

db.create_all()

user = User(email="pwrchords2@yahoo.com", password="p")
db.session.add(user)
db.session.commit()

db.session.refresh(user)

routine1 = Routine(title="Patterns", description="A Routine to learn my fretboard", user=user, exercises="Major Scale Practice|Minor Scale Practice")
routine2 = Routine(title="Finger Exercises", description="Drills to play at 120bpm some day", user=user, exercises="Broken thirds|Broken sixths|Subtraction")
routine3 = Routine(title="Harmonium Jams", description="Songs to play with Ann & friends", user=user, exercises = "Hear This|AM Jam")

db.session.add_all([routine1, routine2, routine3])
db.session.commit()



practice_session1 = PracticeSession(date="01-01-2023", total_session_min=60, user=user)
practice_session2 = PracticeSession(date="01-02-2023", total_session_min=30, user=user)
practice_session3 = PracticeSession(date="01-03-2023", total_session_min=20, user=user)

db.session.add_all([practice_session1, practice_session2, practice_session3])
db.session.commit()
db.session.refresh(practice_session1)
db.session.refresh(practice_session2)
db.session.refresh(practice_session3)

exercise1 = Exercise(ex_title="Charting Open Area", bpm=100, user_id=1)
exercise2 = Exercise(ex_title="Workbook", user_id=1)
exercise3 = Exercise(ex_title="Play Along", bpm=106, user_id=1)
exercise4 = Exercise(ex_title="Broken Thirds", bpm=60, user_id=1)
exercise5 = Exercise(ex_title="Broken Sixths", bpm=89, user_id=1)
exercise6 = Exercise(ex_title="Subtraction", user_id=1)
exercise7 = Exercise(ex_title="Major Scales All Strings", user_id=1)
exercise8 = Exercise(ex_title="Six Variations", user_id=1) 
exercise9 = Exercise(ex_title="Shh", user_id=1)
exercise10 = Exercise(ex_title="Broken Sixths", bpm=100, user_id=1)


db.session.add_all([exercise1, exercise2, exercise3, exercise4, exercise5, exercise6, exercise7, exercise8, exercise9, exercise10])
db.session.commit()