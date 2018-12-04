from django.contrib import admin
from .models import User_Study,User_Study_Assignment,Study,Assignment,Board,attendance,meeting
from django.contrib.auth.models import User


admin.site.register(User_Study)
admin.site.register(User_Study_Assignment)
admin.site.register(Study)
admin.site.register(Assignment)
admin.site.register(Board)
admin.site.register(attendance)
admin.site.register(meeting)

