from django.contrib import admin
from apps.course.models import Course, Description

admin.site.register(Course)
admin.site.register(Description)