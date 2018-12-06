from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
from django.contrib import messages
from .models import *
import random

# Create your views here.


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
    email = ''
    if request.method == "POST":
        id = request.POST['signup-id']
        pwd = request.POST['signup-pwd']
        pwd2 = request.POST['signup-pwd-check']
        email = request.POST['signup-email']
        emailcheck = request.POST['signup-email-check']

        if pwd != pwd2:
            messages.error(request, '비밀번호와 비밀번호 확인이 일치하지 않습니다.')
            return redirect('sign_up')

        if email != '':
            verifynum = random.randint(1, 10000) + 10000;
            send_mail('Negastudy Email Verification Code', 'The verification code is ' + str(verifynum),
                      'negastudyverify@gmail.com', [email], fail_silently=False)

            if emailcheck != verifynum:
                messages.error(request, '이메일 인증 코드가 유효하지 않습니다.')

            else:
                User.objects.create_user(username=id, email=email, password=pwd2)
        User.objects.create_user(username=id, email=email, password=pwd2)
    return render(request, 'main/Sign_Up.html')


def send_email(request):
    send_mail('Negastudy Email Verification Code', 'The verification code is ', 'negastudyverify@gmail.com', ['starlight3714@gmail.com'], fail_silently=False)
    return HttpResponse('Mail Success')