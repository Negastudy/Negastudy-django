from django.db import models


class Category(models.Model):
	_id = models.IntegerField()
	name = models.CharField(max_length=200)

	def __int__(self):
		return self._id


class Company(models.Model):
	_id = models.IntegerField()
	name = models.CharField(max_length=200)

	def __int__(self):
		return self._id


class School(models.Model):
	_id = models.IntegerField()
	name = models.CharField(max_length=200)
