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
                

class WalletView(generic.View):
    def get(self, request):

        return render(request, 'index.html')