# Kickstart Clone in Python's Flask Framework. 

DESIGNING YOUR DATABASE

What is a model? representation of a real world object or concept in app. Normally you'd find a MEMBER MODEL for registratin.

1. What model app needs
2. What attributes should it have
3. What are the relationships between models?


1) Member, Create Project, Create Pledge

2) What are the attributes?

Member 
id
First 
Last Name
Time Created
Time Updated

Project 
id
Name 
Short Description
Long Description
Goal Amount
Time Start
Time End
Time Created
Time Updated

Pledge
id 
amount 
Time Created
Time Updated


3) Relationships?

Member 
member can create many projects
member can pledge many times

Project 
A project has only one creator (member)
A project can have many pledges

Pledge 
A pledge is only made by one member
A pledge is for one project

Example mapped out: 

```

class Member(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	first_name = db.Column(db.String(100))
	last_name = db.Column(db.String(100))
	
	#######################################
	#   member can create many projects   #
	#######################################

	project = db.relationship('Project', backref="creator")
	
	####################################
	#   member can pledge many times   #
	####################################
	
	pledges = db.relationship('Pledge', backref="pledger", foreign_key="Pledge.member_id")
	

class Project(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	
	#############################################
	#  A project has only one creator (member)  #
	#############################################
	
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
	
	name = db.Column(db.String(100))
	short_description = db.Column(db.text)
	long_description = db.Column(db.text)
	goal_amount = db.Column(db.Integer)
	time_start = db.Column(db.DateTime)
	time_end = db.Column(db.DateTime)
	time_created= db.Column(db.DateTime)
	time_updated = db.Column(db.DateTime)
		
	#############################################
	#        A pledge is for one project        #
	#############################################
	
	pledges = db.relationship('Pledge', backref="project", foreign_key="Pledge.member_id")

class Pledge(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	
	#############################################
	#     A pledge is only made by one member   #
	#############################################
	
	member_id = db.Column(db.Integer, db.ForeignKey('member.id'), nullable=False)
	
	#############################################
	#           A pledge is for one project     #
	#############################################
	
	project_id = db.Column(db.Integer, db.ForeignKey('project.id'), nullable=False)
	
	amount = db.Column(db.Integer)
	time_created= db.Column(db.DateTime)
	time_updated = db.Column(db.DateTime)
```