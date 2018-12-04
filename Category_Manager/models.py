from django.db import models


class Category(models.Model):
	_id = models.IntegerField()
	name = models.CharField(max_length=200)


class Company(models.Model):
	_id = models.IntegerField()
	name = models.CharField(max_length=200)

