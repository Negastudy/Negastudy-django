from django.db import models
from django.conf import settings
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date

# CharField는 임시적으로 모두 200글자 제한으로 둠

class Study(models.Model):
	name = models.CharField(max_length=200)
	category = models.IntegerField(null=True)
	company = models.IntegerField(null=True)
	# limit = models.IntegerField(null=True)
	complete = models.BooleanField(default=False)
	startTime = models.DateField(blank=True, null=True)
	endTime = models.DateField(blank=True, null=True)
	id = models.AutoField(primary_key=True)
	members = models.ManyToManyField(
		settings.AUTH_USER_MODEL,
		through='User_Study',
		through_fields=('study', 'user'),
	)

	def save(self, *args, **kwargs):
		super(Study, self).save(*args, **kwargs)
		if self.endTime < date.today():
			self.complete = True
		super(Study, self).save()

	'''def __str__(self):
		return self.name'''


class Assignment(models.Model):
	deadline = models.DateTimeField(blank=True, null=True)
	study = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)


class Board(models.Model):
	study = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)
	author = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
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
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
	study = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)


class Meeting(models.Model):
	study = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)
	date = models.DateField(blank=True, null=True)
	time = models.TimeField(blank=True, null=True)
	location = models.CharField(max_length=200, null=True)
	content = models.TextField(null=True)


class Attendance(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
	meeting = models.ForeignKey(Meeting, on_delete=models.CASCADE, null=True)
	location = models.TextField(default=True)


class User_Study_Assignment(models.Model):
	user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True)
	study = models.ForeignKey(Study, on_delete=models.CASCADE, null=True)
	assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, null=True)