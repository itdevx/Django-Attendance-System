from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from teacher.models import TeacherWeek
from django.contrib.auth.models import User


class TeacherWeekTable(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'teacher-week-table.html'

    def get(self, request, username):
        teacher = User.objects.get(username=username)
        teacher_week = TeacherWeek.objects.filter(teacher=teacher).order_by('-day', 'start_time', 'classes')
        for i in teacher_week:
            print(int(i.start_time.hour))

        context = {
            'teacher_wt' : teacher_week,
            'teacher' : teacher
        }

        return render(request, self.template_name, context)

