from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.http import Http404, HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from Student import models
from Student import forms
from django.core.exceptions import ValidationError


class IndexView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    
    def get(self, request):
        class_room = models.Class.objects.all()
        class_room_m = models.Class.objects.filter(shift='صبح').all()
        class_room_e = models.Class.objects.filter(shift='عصر').all()
        student_e = models.Student.objects.filter(class_id__shift='عصر').count()
        student_m = models.Student.objects.filter(class_id__shift='صبح').count()

        c = {
            'class_room': class_room,
            'class_room_m': class_room_m,
            'class_room_e': class_room_e,
            'student_m': student_m,
            'student_e': student_e
        }
        return render(request, 'home.html', c)


class ClassRoomView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'

    def get(self, request, *args, **kwargs):
        number = kwargs.get('number')
        shift = kwargs.get('shift')
        students_in_class_room = models.Student.objects.filter(class_id__number=number, class_id__shift=shift).all()
        return render(request, 'class-room.html', {'student_class_room': students_in_class_room})


class CreateClassView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'create-class.html'

    def get(self, request, *args, **kwargs):
        form = forms.ClassForm(request.POST)
        class_ = models.Class.objects.all()
        return render(request, self.template_name, {'form': form, 'class': class_})
    
    def post(self, request, *args, **kwargs):
        if request.POST:
            form = forms.ClassForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student:created-list')
        else:
            form = forms.ClassForm()
        return render(request, self.template_name, {'form': form})


# TODO : have a problem for modal
class ClassDelete(LoginRequiredMixin, generic.DeleteView):
    login_url = 'account:login'
    model = models.Class
    success_url = reverse_lazy('student:create-class')


def class_edit(request, number, shift):
    context = {}
    obj = get_object_or_404(models.Class, number=number, shift=shift)
    form = forms.ClassForm(request.POST or None, instance=obj)
    class_ = models.Class.objects.all()
    if form.is_valid():
        form.save()
        return redirect('student:index')
    context['form'] = form
    context['class'] = class_
    return render(request, 'create-class.html', context)


class CreateAssignView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'create-assign.html'

    def get(self, request, *args, **kwargs):
        form = forms.AssignForm(request.POST)
        assign = models.Assign.objects.all()
        class_ = models.Class.objects.all()
        return render(request, self.template_name, {'form': form, 'assign': assign, 'class': class_})
    
    def post(self, request, *args, **kwargs):
        if request.POST:
            form = forms.AssignForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student:created-list')
        else:
            form = forms.AssignForm()
        return render(request, self.template_name, {'form': form})


class CreateAttendanceClassView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'create-attendance-class.html'

    def get(self, request, *args, **kwargs):
        form = forms.AttendanceClassForm(request.POST)
        attendance = models.AttendanceClass.objects.all()
        return render(request, self.template_name, {'form': form, 'attendance': attendance})
    
    def post(self, request, *args, **kwargs):
        if request.POST:
            form = forms.AttendanceClassForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student:created-list')
        else:
            form = forms.AttendanceClassForm()
        return render(request, self.template_name, {'form': form})


class CreateReshteView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'create-reshte.html'

    def get(self, request, *args, **kwargs):
        form = forms.ReshteForm(request.POST)
        reshte = models.Reshte.objects.all()
        return render(request, self.template_name, {'form': form, 'reshte': reshte})
    
    def post(self, request, *args, **kwargs):
        if request.POST:
            form = forms.ReshteForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('student:created-list')
        else:
            form = forms.ReshteForm()
        return render(request, self.template_name, {'form': form})


# def reshte_edit(request, pk):
#     context = {}
#     objec = get_object_or_404(models.Reshte, id=pk)
#     form = forms.EditReshteForm(request.POST or None, instance=objec)
#     reshte = models.Reshte.objects.all()
#     if form.is_valid():
#         form.save()
#         return redirect('student:create-reshte')
#     context['form'] = form
#     context['reshte'] = reshte
#     return render(request, 'create-reshte.html', context)


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
        attendance = models.Attendance.objects.filter(student=student).order_by('-id').distinct()

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

        attendance = models.Attendance.objects.filter(student__class_id__number=assign_class_id, date=assc.date)
        context = {
            'ass': ass,
            'c': c,
            'assc': assc,
            'attendance': attendance
        }
        return render(request, self.template_name, context)


def confirm(request, assign_class_id):
    assc = get_object_or_404(models.AttendanceClass, assign__class_id__number=assign_class_id)
    ass = assc.assign
    cl = ass.class_id

    for i, s in enumerate(cl.student_set.all()):
        status = request.POST.get(s.usn, False)
        if status == 'present':
            status = True
        else:
            status = False
        if assc.status == 1:
            from django.utils import timezone
            if models.Attendance.objects.filter(student=s, date=timezone.now().date()).exists():
                return HttpResponse('این وجود دارد')
            else:
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


class SearchingView(generic.ListView):
    template_name = 'search.html'
    context_object_name = 'student_class_room'

    def get_queryset(self):
        query = self.request.GET.get('query')
        if query is not None:
            return models.Student.objects.get_searching(query)
        return models.Student.objects.all()


class WalletView(generic.View):
    def get(self, request):
        return render(request, 'index.html')



