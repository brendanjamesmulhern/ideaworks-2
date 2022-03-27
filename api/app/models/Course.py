from . import User
from . import Section
from django.db import models

print(User)

class Course(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sections = models.ManyToManyField(Section.Section, related_name="courses", null=True, blank=True)

    def __str__(self):
        return self.title
