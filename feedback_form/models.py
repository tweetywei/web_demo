from django.db import models

# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=30)
    degree = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Feedback(models.Model):
    student_name = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.FloatField()
    ranking_level = models.IntegerField()

    def __str__(self):
        return self.student_name