from . import Course
from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=5000)
    email = models.EmailField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bought_courses = models.ManyToManyField(Course.Course, related_name='bought_courses', null=True, blank=True)
    made_courses = models.ManyToManyField(Course.Course, related_name='made_courses', null=True, blank=True)

    def __str__(self):
        return self.username