from punchstarter import db

#create members class and inhert from db.model class

class Member(db.Model):
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	

class Project(db.Model):
	name = db.Column(db.String(100))
	short_description = db.Column(db.text)
	long_description = db.Column(db.text)
	goal_amount = db.Column(db.Integer)
	time_start = db.Column(db.DateTime)
	time_end = db.Column(db.DateTime)
	time_created= db.Column(db.DateTime)
	time_updated = db.Column(db.DateTime)

class Pledge(db.Model):
	pass
	