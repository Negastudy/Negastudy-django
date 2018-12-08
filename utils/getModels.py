from Category_Manager.models import Category, Company, School
from Studycafe_Manager.models import Cafe
from main.models import User_Study,User_Study_Assignment,Study,Assignment,Board,Attendance,Meeting
from django.contrib.auth.models import User


def getCategory(n):
	cat = Category.objects.get(_id=n)
	return cat.name


def getCategoryNames():
	category_list = Category.objects.all()
	category_namelist = []
	category_numlist = []
	for cat in category_list:
		category_namelist.append(cat.name)
		category_numlist.append(cat._id)

	return category_namelist, category_numlist


def getNotice(pk):
	try:
		# boards = Board.objects.get(study=pk)
		title = Board.objects.filter(study=pk).latest('title')
	except Board.DoesNotExist:
		title = None

	return title


def getPeoplenames(pk):
	try:
		user_study = User_Study.objects.filter(study=pk)
		people = []
		for element in user_study:
			people.append(element.user)
		return  people
	except User_Study.DoesNotExist:
		return None


def getSchoolNames():
	school_list = School.objects.all()
	school_namelist = []
	school_numlist = []
	for s in school_list:
		school_namelist.append(s.name)
		school_numlist.append(s._id)

	return school_namelist, school_numlist


def getCompanyNames():
	Company_list = Company.objects.all()
	Company_namelist = []
	Company_numlist = []
	for com in Company_list:
		Company_namelist.append(com.name)
		Company_numlist.append(com._id)

	return Company_namelist, Company_numlist


def getMeetings(pk):
	study_names = []
	meeting_date = []
	meeting_contents = []

	try:
		user = User.objects.get(id=pk)
		user_studies = User_Study.objects.filter(user=user)

		for s in user_studies:
			study = s.study
			study_names.append(study.name)
			meetings = Meeting.objects.filter(study=study)
			for m in meetings:
				meeting_date.append(m.date)
				meeting_contents.append(m.content)
	except:
		print("No attributes")

	return study_names, meeting_date, meeting_contents

