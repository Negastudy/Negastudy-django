from django.db import models


class Category(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=200)


class Company(models.Model):
	id = models.IntegerField()
	name = models.CharField(max_length=200)

