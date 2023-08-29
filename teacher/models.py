from django.db import models
from django.contrib.auth.models import User
from Student.models import Class, WEEK


class TeacherWeek(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)
    classes = models.ForeignKey(Class, on_delete=models.CASCADE)
    day = models.CharField(max_length=10, choices=WEEK)
    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return str(self.teacher)
        

    