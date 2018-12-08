from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm, StudyForm, SearchForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
from Category_Manager.models import Category, Company, School
import random
from django.shortcuts import render, get_object_or_404
from utils.getModels import getCategory, getNotice, getPeoplenames, getCategoryNames, getSchoolNames, getCompanyNames, getMeetings
import json
from django.contrib.auth.decorators import login_required
from main.models import User_Study,User_Study_Assignment,Study,Assignment,Board,Attendance,Meeting
from random import *
from django.db.models import Q


verifynum = 0

def sign_in(request):
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			login(request, user)
			return HttpResponse('Success!')
		else:
			return redirect('sign_in')
	else:
		form = LoginForm()
		return render(request, 'main/Log_In.html', {'form': form})


def mypage(request):
	data = {'username': request.user, 'email': request.user.email}
	return render(request, 'main/mypage.html', {'data': data})


def studyinfo(request, pk):
	study = Study.objects.get(pk=pk)
	meeting = Meeting.objects.filter(study=study)

	return render(request, 'main/Study_Group.html', {'study': study, 'meeting_list': meeting })


def sign_up(request): # 미완성
	if request.method == "POST":
		emailcheck = request.POST.get('code', '')

	#if pwd != pwd2:
	#    messages.error(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
	#    return redirect('sign_up')

	# if emailcheck != '':
	#    if int(emailcheck) != verifynum:
	#      print(int(emailcheck), verifynum, "NOTVALID")
	#      messages.error(request, '이메일 인증 코드가 유효하지 않습니다.')

	#else:
	#id = request.POST['signup-id']
	#pwd = request.POST['signup-pwd']
	#pwd2 = request.POST['signup-pwd-check']
	#User.objects.create_user(username=id, email=email, password=pwd2)
	#  User.objects.create_user(username=id, email=email, password=pwd2)
	return render(request, 'main/Sign_Up.html')


def send_email(request):
	if request.method == "POST":
		email = request.POST.get('email', '')

		global verifynum
		verifynum = random.randint(1, 10000) + 10000
		request.session
		send_mail('Negastudy Email Verification Code', 'The verification code is '+str(verifynum), 'negastudyverify@gmail.com', [email], fail_silently=False)
	return HttpResponse('success')


def check_code(request):
	if request.method == "POST":
		code = request.POST.get('code','')
		global verifynum

		if int(code) != verifynum:
			print(int(code), verifynum, "NOTVALID")
			messages.error(request, '이메일 인증 코드가 유효하지 않습니다.')


def Study_detail(request, pk):
	study_group = get_object_or_404(Study, pk=pk)

	category =getCategory(study_group.category)
	title = study_group.name
	StartTime = study_group.startTime
	EndTime = study_group.endTime
	notice = getNotice(pk)
	meeting_list = []
	try:
		meeting_list = Meeting.objects.filter(study=pk).order_by('-date')
		meeting_list = meeting_list[0:4]

	except Meeting.DoesNotExist:
		meeting_list = []

	people = getPeoplenames(pk)
	complete = study_group.complete
	if len(meeting_list) == 0:
		meeting_list = None

	return render(request, 'main/Study_Group.html', locals())


def create(request):
	form = StudyForm(request.POST)
	if request.method =='POST':
		try:
			category_namelist, category_numlist = getCategoryNames()
			school_namelist, school_numlist = getSchoolNames()
			Company_namelist, Company_numlist = getCompanyNames()
			return HttpResponse(json.dumps({'category_namelist': category_namelist,
			                                'category_numlist': category_numlist,
			                                'school_namelist': school_namelist,
			                                'school_numlist': school_numlist,
			                                'Company_namelist': Company_namelist,
			                                'Company_numlist': Company_numlist,}), 'application/json')
		except:
			if form.is_valid():
				pass
	return render(request, 'main/Study_Create.html', locals())


# @login_required (login_url = '/sign_in/')
def home(request):
	user_id=5
	user = User.objects.get(id=user_id)
	study_names, meeting_date, meeting_contents = getMeetings(user_id)
	alarm_num = len(study_names)
	alarm = []
	for i in range(alarm_num):
		year, month, day = str(meeting_date[i]).split('-')
		alarm.append("[{}] : {} ({}/{})".format(study_names[i], meeting_contents[i], month, day))

	school_num = user.last_name
	school = School.objects.get(_id = int(school_num))
	school_name = school.name # 유저 학교 명
	school_study_num = Study.objects.filter(school = school.id).count() # 학교 스터디 개수
	school_studying_num = Study.objects.filter(school = school.id, complete=False).count() # 진행중인 학교 스터디 개수

	category_num1 = randint(1, 10)
	category1 = Category.objects.get(_id = int(category_num1))
	category_name1 = category1.name #랜덤 카테고리 명
	category_study_num1 = Study.objects.filter(category=category1.id).count()
	category_studying_num1 = Study.objects.filter(category=category1.id, complete=False).count()

	category_num2 = 10
	while category_num2 == category_num1:
		category_num2 = randint(1, 10)
	category2 = Category.objects.get(_id=int(category_num2))
	category_name2 = category2.name  # 랜덤 카테고리 명
	category_study_num2 = Study.objects.filter(category=category2.id).count()
	category_studying_num2 = Study.objects.filter(category=category2.id, complete=False).count()

	url1 = "../../static/images/"
	if category_num1 == 1:
		url1 += "Foreign_Language.jpg"
	elif category_num1 == 2:
		url1 += "interview.jpeg"
	elif category_num1 == 3:
		url1 += "exam.jpg"
	elif category_num1 == 4:
		url1 += "NCS.jpg"
	elif category_num1 == 5:
		url1 += "job.jpg"
	elif category_num1 == 6:
		url1 += "intern.jpg"
	elif category_num1 == 7:
		url1 += "talk.jpg"
	elif category_num1 == 8:
		url1 += "coding.jpg"
	elif category_num1 == 9:
		url1 += "sanhak.jpg"
	else:
		url1 += "main_omr.jpg"

	url2 = "../../static/images/"
	if category_num2 == 1:
		url2 += "Foreign_Language.jpg"
	elif category_num2 == 2:
		url2 += "interview.jpeg"
	elif category_num2 == 3:
		url2 += "exam.jpg"
	elif category_num2 == 4:
		url2 += "NCS.jpg"
	elif category_num2 == 5:
		url2 += "job.jpg"
	elif category_num2 == 6:
		url2 += "intern.jpg"
	elif category_num2 == 7:
		url2 += "talk.jpg"
	elif category_num2 == 8:
		url2 += "coding.jpg"
	elif category_num2 == 9:
		url2 += "sanhak.jpg"
	else:
		url2 += "main_omr.jpg"


	return render(request, 'main/home.html', locals())


def search(request):
	qs = Study.objects.all()
	q = request.GET.get('q', '')
	if q:
		list = qs.filter(Q(name__contains=q) | Q(desc__contains=q))

	return render(request, 'main/study_list.html', locals())





