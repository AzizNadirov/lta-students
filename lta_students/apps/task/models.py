from django.db import models


class Task(models.Model):
    question = models.TextField('tapşırıq')
    to_lesson = models.ManyToManyField('course.Lesson', related_name='tasks', blank=True)
    answer = models.TextField("cavab")

