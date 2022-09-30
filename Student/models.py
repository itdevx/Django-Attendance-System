from django.db import models
from django.urls import reverse
from django.db.models import Q


class Manager(models.Manager):
    def get_searching(self, query):
        ST = Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(id_code__icontains=query)
        return self.get_queryset().filter(ST).distinct()


class ClassRoom(models.Model):
    SHIFT = (
        ('M', 'صبح'),
        ('E', 'عصر'),
    )

    name = models.IntegerField(verbose_name='شماره کلاس')
    shift = models.CharField(choices=SHIFT, max_length=1, verbose_name='شیفت کلاسی')

    def get_absolut_url(self):
        return reverse('student:class_room', args=[self.shift, self.name])

    def __str__(self):
        return f'کلاس شماره {self.name} در شیفت {self.shift}'


class Student(models.Model):
    LEVEL = (
        ('10', 'دهم'),
        ('12', 'یازدهم'),
        ('11', 'دوازدهم'),
    )

    first_name = models.CharField(max_length=100, verbose_name='نام')
    last_name = models.CharField(max_length=100, verbose_name='نام خانوادگی')
    father_name = models.CharField(max_length=100, null=True, verbose_name='نام پدر')
    id_code = models.IntegerField(unique=True, verbose_name='کد ملی')
    class_room = models.ForeignKey(ClassRoom, on_delete=models.CASCADE)
    level = models.CharField(choices=LEVEL, max_length=2, verbose_name='پایه')
    level_up = models.BooleanField(default=False, verbose_name='قبول شده / قبول نشده')
    objects = Manager()

    def get_abolut_url(self):
        pass

    def __str__(self):
        return f'{self.first_name} {self.last_name} | {self.level} | {self.id_code}'

    
class Attendance(models.Model):
    ATTENDANCE = (
        ('1', 'حاضر'),
        ('2', 'تاخیر'),
        ('3', 'غیبت موجه'),
        ('4', 'غیبت غیر موجه'),
        ('5', 'مرخصی'),
    )

    ALARM = (
        ('1', 'زنگ اول'),
        ('2', 'زنگ دوم'),
        ('3', 'زنگ سوم'),
        ('4', 'زنگ چهارم'),
    )

    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name='دانش آموزش')
    alarm = models.CharField(choices=ALARM, max_length=1, null=True, blank=True, verbose_name='زنگ')
    attendance = models.CharField(choices=ATTENDANCE, max_length=1, default=1, verbose_name='حضور و غیاب')
    # change all name under line 55
    time_takhir = models.CharField(max_length=100, null=True, blank=True, verbose_name='زمان تاخیر')
    gheybat_movajah = models.TextField(null=True, blank=True, verbose_name='غیبت موجه')
    gheybat_gheyr_movajah = models.TextField(null=True, blank=True, verbose_name='غیبت غیر موجه')
    morkhasi = models.TextField(null=True, blank=True, verbose_name='مرخصی')
    date_attendance = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.student.first_name} {self.student.last_name} | {self.attendance} | {self.date_attendance.year}/{self.date_attendance.month}/{self.date_attendance.day}'
