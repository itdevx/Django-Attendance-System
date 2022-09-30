from http.client import RemoteDisconnected
from urllib.request import HTTPRedirectHandler
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Student import models
from Student import forms


class IndexView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    
    def get(self, request):
        class_room = models.ClassRoom.objects.all()
        context = {
            'class_room': class_room
        }

        return render(request, 'home.html', context)

    
class ClassRoomView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'

    def get(self, request, *args, **kwargs):
        shift = kwargs.get('shift')
        class_name = kwargs.get('class_name')
        students_by_class_room = models.Student.objects.filter(class_room__shift=shift, class_room__name=class_name).all()

        context = {
            'student_class_room': students_by_class_room,
            'cn': class_name
        }

        return render(request, 'class-room.html', context)


class AttendanceView(generic.View):
    def get(self, request, *args, **kwargs):
        class_name = kwargs.get('class_name')
        form = forms.AttendanceForm(class_name, request.POST)
        context = {
            'form': form,
            'cn': class_name
        }

        return render(request, 'attendance.html', context)

    def post(self, request, *args, **kwargs):
        class_name = kwargs.get('class_name')
        if request.POST:
            form = forms.AttendanceForm(class_name, request.POST)
            if form.is_valid():
                form.save()
                return redirect(f'/attendance/{class_name}')

        c = {   
            'form': form
        }

        return render(request, 'attendance.html', c)


class CreateStudentView(generic.View):
    template_name = 'create-student.html'
    def get(self, request, *args, **kwargs):
        form = forms.StudentForm(request.POST)
        context = {
            'form': form
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        message = ''
        if request.POST:
            form = forms.StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student:create-student')
        else:
            form = forms.StudentForm()

        return render(request, self.template_name, {'form': form, 'message': message})
                

class SearchingView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'student_class_room'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query is not None:
            return models.Student.objects.get_searching(query)
        return models.Student.objects.all()


class StudentInfo(generic.View):
    template_name = 'student.html'

    def get(self, request, *args, **kwargs):
        last_name = kwargs.get('last_name')
        id_code = kwargs.get('id_code')

        student = models.Student.objects.filter(last_name=last_name, id_code=id_code).first()
        attendance = models.Attendance.objects.filter(student=student).all().order_by('-id')[:1]

        context = {
            'student': student,
            'attendance': attendance
        }

        return render(request, self.template_name, context)


class WalletView(generic.View):
    def get(self, request):

        return render(request, 'index.html')