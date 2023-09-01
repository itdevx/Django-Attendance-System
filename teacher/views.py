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
        context = {
            'teacher_wt' : teacher_week,
            'teacher' : teacher
        }

        return render(request, self.template_name, context)


class Teacher(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'teacher.html'

    def get(self, request):
        if not request.user.is_superuser:
            teacher = User.objects.filter(username=request.user.username)
            teacher_week = TeacherWeek.objects.filter(teacher=teacher).order_by('-day', 'start_time', 'classes')
            print(teacher_week)
            context = {
                'teacher': teacher,
                'teacher_wt': teacher_week
            }
            return render(request, self.template_name, context)

