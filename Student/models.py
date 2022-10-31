from django.utils import timezone
from django.db import models
from django.urls import reverse
from django.db.models import Q
from django.core.exceptions import ValidationError
from extentions.utils import jalali_converter


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

ZANG = (
    ('اول', 'اول'),
    ('دوم', 'دوم'),
    ('دوم', 'دوم'),
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
    zang = models.BooleanField(choices=ZANG, null=True, blank=True)
    objects = Manager()

    def __str__(self):
        return f'{self.full_name}-{self.id_code}-{self.class_id}-{self.reshte}-{self.level}'

    def get_absolute_url(self):
        return reverse('student:student',args=[self.full_name, self.id_code])

    def jdate(self):
        return jalali_converter(self.date)

class Assign(models.Model):
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return f'کلاس : {self.class_id} اختصاص داده شد'

    def get_absolute_url(self):
        return reverse('student:class-room', args=[self.class_id.number, self.class_id.shift])


class AttendanceClass(models.Model):
    assign = models.ForeignKey(Assign, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    status = models.IntegerField(default=0)    

    def __str__(self):
        return f'کلاس : {self.assign.class_id.number} در شیف : {self.assign.class_id.shift}'

    def jdate(self):
        return jalali_converter(self.date)

class Zang(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    attendanceclass = models.ForeignKey(AttendanceClass, on_delete=models.CASCADE, default=1)
    date = models.DateField(auto_now_add=True)
    status = models.BooleanField(default=True)
    gheybat_text = models.CharField(max_length=500, null=True, blank=True)
    zang = models.ForeignKey(Zang, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.student.full_name} درتاریخ : {self.status} <- {self.date}'

    def jdate(self):
        return jalali_converter(self.date)
