from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.core.mail import send_mail
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


def sign_up(request): # 미완성
    if request.method == "POST":
        name = request.POST['signup-fname']
        phone = request.POST['signup-phone']
        birth = request.POST['signup-birth']

        # User.objects.create_user(username=name, )

    return render(request, 'main/Sign_Up.html')


def send_email(request):
    verifynum = random.randint(1, 10000) + 10000;
    send_mail('Negastudy Email Verification Code', 'The verification code is '+str(verifynum), 'negastudyverify@gmail.com', ['starlight3714@gmail.com'], fail_silently=False)
    return HttpResponse('Mail Success')