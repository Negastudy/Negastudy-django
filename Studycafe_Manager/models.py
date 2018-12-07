from django.db import models


class Cafe(models.Model):
	name = models.CharField(max_length=200)
	location = models.TextField(default=True)
	# 추가 정보 필요

