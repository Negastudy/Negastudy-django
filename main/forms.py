from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.ModelForm): # 이거 사용 안함

    class Meta:
        model = User
        fields = ['username', 'password']