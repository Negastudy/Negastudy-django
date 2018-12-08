from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('mypage', views.mypage, name='mypage'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('send_email', views.send_email, name='send_email'),
    url(r'^study_group/(?P<pk>\d+)/$', views.Study_detail, name='study_group'),
    path('check_code', views.check_code, name='check_code'),
    url(r'^studyinfo/(?P<pk>\d+)/$', views.studyinfo, name='studyinfo'),
    path('create', views.create, name='createStudy'),
]