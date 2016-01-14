from punchstarter import db

#create members class and inhert from db.model class

'''
Relationships?

Member 
member can create many projects  - relationship 
member can pledge many times     - relationship - foreign_keys

Project 
A project has only one creator (member) - Foreigh Key 
A project can have many pledges - relationship - Foreign Key 

Pledge 
A pledge is only made by one member - Foreign Key - member.id
A pledge is for one project - Foreign Key - project.id
'''

class Member(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(64), nullable=False)
	last_name = db.Column(db.String(64), nullable=False)
	project = db.relationship('Project', backref='creator')
	pledges = db.relationship('Pledge', backref='pledgor', foreign_keys='Pledge.member_id')
	

class Project(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
	name = db.Column(db.String(64), nullable=False)
	short_description = db.Column(db.Text, nullable=False)
	long_description = db.Column(db.Text, nullable=False)
	goal_amount = db.Column(db.Integer, nullable=False)
	image_filename = db.Column(db.String(128), nullable=False)
	time_created = db.Column(db.DateTime(timezone=False), nullable=False)
	time_start = db.Column(db.DateTime(timezone=False), nullable=False)
	time_end = db.Column(db.DateTime(timezone=False), nullable=False)
	pledges = db.relationship('Pledge', backref='project', foreign_keys='Pledge.project_id')
	
	#properties when you need to create new attributes dependent on existing fields in database


	# def num_days_left(self):
	# 	now = datetime.datetime.now()
	# 	num_days_left = (self.time_end - now).days

	# 	return num_days_left
	

class Pledge(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
	amount = db.Column(db.Integer, nullable=False)
	time_created = db.Column(db.DateTime(timezone=False), nullable=False)