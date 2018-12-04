from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# CharField는 임시적으로 모두 200글자 제한으로 둠


class Study(models.Model):
	category = models.IntegerField(null=True)
	name = models.CharField(max_length=200)
	company = models.IntegerField(null=True)
	id = models.AutoField(primary_key=True)


class Assignment(models.Model):
	deadline = models.DateTimeField(blank=True, null=True)
	study = models.ForeignKey(Study, on_delete=models.CASCADE)


class Board(models.Model):
	study = models.ForeignKey(Study, on_delete=models.CASCADE)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
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
	uid = models.ForeignKey(User, on_delete=models.CASCADE)
	study = models.ForeignKey(Study, on_delete=models.CASCADE)


class Meeting(models.Model):
	# ForeignKey (User_Study) 추가필요
	date = models.DateTimeField(blank=True, null=True)
	location = models.TextField()


class Attendance(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE)


class User_Study_Assignment(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	study = models.ForeignKey(Study, on_delete=models.CASCADE)
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)