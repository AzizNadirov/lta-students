from django.db import models

class Lesson(models.Model):
    name = models.CharField(max_length=1024)
    module = models.ForeignKey('Module', related_name = 'lessons', on_delete=models.CASCADE)

    def __str__(self):
        return f"<Lesson: {self.name}>"


class Module(models.Model):
    name = models.CharField(max_length=1024)
    course = models.ForeignKey('Course', related_name='modules', on_delete=models.CASCADE)
    
    def __str__(self):
        return f"<Module: {self.name}>"


class Course(models.Model):
    name = models.CharField('kurs', max_length=50)
    participants = models.ManyToManyField('student.Profile', related_name='courses', blank=True)

    def __str__(self):
        return f"<Course: {self.name}>"