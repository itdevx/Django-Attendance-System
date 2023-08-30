from django.db import models
from django.contrib.auth.models import User
from Student.models import Class, WEEK


class TeacherWeek(models.Model):
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='نام معلم')
    classes = models.ForeignKey(Class, on_delete=models.CASCADE, verbose_name='نام کلاس')
    day = models.CharField(max_length=10, choices=WEEK, verbose_name='روز های هفته')
    start_time = models.TimeField(verbose_name='شروع ساعت کلاس')
    end_time = models.TimeField(verbose_name='پایان ساعت کلاس')

    def __str__(self):
        return str(self.teacher)
        

    