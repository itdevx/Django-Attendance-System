from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.http import Http404
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Student import models
from Student import forms


class IndexView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    
    def get(self, request):
        class_room = models.Class.objects.all()
        return render(request, 'home.html', {'class_room': class_room})


class ClassRoomView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'

    def get(self, request, *args, **kwargs):
        number = kwargs.get('number')
        shift = kwargs.get('shift')
        students_in_class_room = models.Student.objects.filter(class_id__number=number, class_id__shift=shift).all()
        return render(request, 'class-room.html', {'student_class_room': students_in_class_room})


class CreateStudenView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'create-student.html'

    def get(self, request, *args, **kwargs):
        form = forms.StudentForm(request.POST)
        return render(request, self.template_name, {'form': form})
    
    def post(self, request, *args, **kwargs):
        if request.POST:
            form = forms.StudentForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student:create-student')
        else:
            form = forms.StudentForm()
        return render(request, self.template_name, {'form': form})



class StudentInfoView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'student.html'

    def get(self, request, *args, **kwargs):
        full_name = kwargs.get('full_name')
        id_code = kwargs.get('id_code')
        student = models.Student.objects.filter(full_name=full_name, id_code=id_code).first()
        attendance = models.Attendance.objects.filter(student=student).order_by('-id')

        context = {
            'student': student,
            'attendance': attendance
        }
        return render(request, self.template_name, context)


def student_edit(request, full_name, id_code):
    context = {}
    obj = get_object_or_404(models.Student, full_name=full_name, id_code=id_code)
    form = forms.StudentEditForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        level = form.cleaned_data.get('level')
        if form.cleaned_data.get('level_up'):
            level += 1
            form.save()

        # TODO redirec to class-room
        return redirect('student:index')
    context['form'] = form
    return render(request, 'edit-student.html', context)


class AttendanceView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'attendance.html'

    def get(self, request, *args, **kwargs):
        assign_class_id = kwargs.get('assign_class_id')
        # shift = kwargs.get('shift')
        assc = get_object_or_404(models.AttendanceClass, assign__class_id__number=assign_class_id)
        ass = assc.assign
        c = ass.class_id
        context = {
            'ass': ass,
            'c': c,
            'assc': assc
        }
        return render(request, self.template_name, context)


def confirm(request, assign_class_id):
    assc = get_object_or_404(models.AttendanceClass, assign__class_id__number=assign_class_id)
    ass = assc.assign
    cl = ass.class_id

    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.usn]
        if status == 'present':
            status = True
        else:
            status = False
        if assc.status == 1:
            try:
                a = models.Attendance.objects.create(student=s, date=assc.date, attendanceclass=assc)
                a.status = status
                a.save()
            except models.Attendance.DoesNotExist:
                a = models.Attendance(student=s, status=status, date=assc.date, attendanceclass=assc)
                a.save()
        else:
            a = models.Attendance(student=s, status=status, date=assc.date, attendanceclass=assc)            
            a.save()
            assc.status = 1
            assc.save()
    return HttpResponseRedirect(reverse('student:index'))



class WalletView(generic.View):
    def get(self, request):
        return render(request, 'index.html')


class SearchingView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'student_class_room'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query is not None:
            return models.Student.objects.get_searching(query)
        return models.Student.objects.all()

# =============================================================





