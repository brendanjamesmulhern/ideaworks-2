from . import Lesson
from django.db import models

class Section(models.Model):
    title = models.CharField(max_length=1000)
    articles = models.ManyToManyField(Lesson.Lesson, related_name='sections', null=True, blank=True);

    def __str__(self):
        return self.title