from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.core.exceptions import ValidationError


class Manager(models.Manager):
    def get_searching(self, query):
        ST = Q(full_name__icontains=query) | Q(id_code__icontains=query)
        return self.get_queryset().filter(ST).distinct()


SHIFT = (
    ('صبح', 'صبح'),
    ('عصر', 'عصر'),
)

LEVEL = (
    ('دهم', 'دهم'),
    ('یازدهم', 'یازدهم'),
    ('دوازدهم', 'دوازدهم'),
)

class Reshte(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Class(models.Model):
    number = models.IntegerField()
    shift = models.CharField(choices=SHIFT, max_length=3)

    def __str__(self):
        return f'{self.number}-{self.shift}'

    def get_absolute_url(self):
        return reverse('student:class-room', args=[self.number, self.shift])
    
    # def get_attendance_url(self):
        # return reverse('student:attendance', args=[self.id])


class Student(models.Model):
    full_name = models.CharField(max_length=200)
    father_name = models.CharField(max_length=100)
    id_code = models.IntegerField(unique=True)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    reshte = models.ForeignKey(Reshte, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVEL, max_length=8)
    level_up = models.BooleanField(default=False)
    date = models.DateField()
    usn = models.CharField(primary_key=True, max_length=200)
    objects = Manager()

    def __str__(self):
        return f'{self.full_name}-{self.id_code}-{self.class_id}-{self.reshte}-{self.level}'

    def get_absolute_url(self):
        return reverse('student:student',args=[self.full_name, self.id_code])


class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    
    # def __str__(self):
    #     return str(self.class_id)


class AttendanceClass(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendanceclass = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    gheybat_text = models.CharField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f'{self.student.full_name} درتاریخ : {self.status} <- {self.date}'


