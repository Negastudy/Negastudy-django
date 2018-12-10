from . import views
from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf.urls import url

urlpatterns = [
    path('home', views.home, name='home'),
    path('sign_in', views.sign_in, name='sign_in'),
    path('mypage', views.mypage, name='mypage'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('send_email', views.send_email, name='send_email'),
    url(r'^study_group/(?P<pk>\d+)/$', views.Study_detail, name='study_group'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('check_code', views.check_code, name='check_code'),
    path('create', views.create, name='createStudy'),
    path('search', views.search, name='search'),
    url(r'^apply/(?P<pk>\d+)/$', views.apply, name='apply'),
    url(r'^school_search/(?P<pk>\d+)/$', views.categoty_school, name='cate'),
    url(r'^category_search/(?P<pk>\d+)/$', views.categoty, name='cate2'),
]