from . import views
from django.urls import path

urlpatterns = [
    path('sign_in', views.sign_in, name='sign_in'),
    path('mypage', views.mypage, name='mypage'),
    path('sign_up', views.sign_up, name='sign_up'),
    path('send_email', views.send_email, name='send_email'),
    # path('home', views.)
]