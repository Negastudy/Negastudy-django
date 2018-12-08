from Category_Manager.models import Category, Company
from Studycafe_Manager.models import Cafe
from main.models import User_Study,User_Study_Assignment,Study,Assignment,Board,Attendance,Meeting


def getCategory(n):
	cat = Category.objects.get(_id=n)
	return cat.name


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

