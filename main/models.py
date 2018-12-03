from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# CharField는 임시적으로 모두 200글자 제한으로 둠
'''
class User(models.Model):
	sex = models.IntegerField()
	name = models.CharField(max_length=200)
	password = models.TextField()
	email = models.TextField()
'''


class Study(models.Model):
	category = models.IntegerField()
	name = models.CharField(max_length=200)
	company = models.IntegerField()
	id = models.AutoField(primary_key=True)


class Assignment(models.Model):
	deadline = models.DateTimeField(blank=True, null=True)
	study = models.ForeignKey(Study, related_name='assignment', on_delete=models.CASCADE)  # 수정 필요


class Board(models.Model):
	study = models.ForeignKey(Study, on_delete=models.CASCADE)
	auth = models.CharField(max_length=200)  # 수정필요 (https://tutorial.djangogirls.org/ko/django_models/ 예시 모델 참고)
	title = models.CharField(max_length=200)
	date = models.DateTimeField(blank=True, null=True)
	content = models.TextField()

	def publish(self):
		''' 글 게시 시간 자동 생성 및 모델 저장'''
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title


class User_Study(models.Model):
	pass
	# ForeignKey (User) 추가필요
	# ForeignKey (Study) 추가필요


class attendance(models.Model):
	pass
	# ForeignKey (User) 추가필요
	# ForeignKey (meeting) 추가필요


class meeting(models.Model):
	# ForeignKey (User_Study) 추가필요
	date = models.DateTimeField(blank=True, null=True)
	location = models.TextField()


class User_Study_Assignment(models.Model):
	pass
	# ForeignKey (User) 추가필요
	# ForeignKey (Study) 추가필요
	# ForeignKey (Assignment) 추가필요