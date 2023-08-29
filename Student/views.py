from typing import Any, Dict, Optional
from django.db import models
from django.shortcuts import redirect, render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.urls import reverse
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from Student import models
from Student import forms
from teacher import forms as tf
from django.contrib.auth.decorators import login_required
from extentions.utils import jalali_converter
from django.utils import timezone
import csv
from io import BytesIO
from django.template.loader import get_template, render_to_string
from xhtml2pdf import pisa
import pandas as pd
from io import StringIO


class IndexView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'home.html'
    
    def get(self, request):
        student_m = models.Student.objects.filter(class_id__shift='صبح').count()
        student_e = models.Student.objects.filter(class_id__shift='عصر').count()
        c = {
            'student_m': student_m,
            'student_e': student_e
        }
        assign_m = models.Assign.objects.filter(class_id__shift='صبح')
        assign_e = models.Assign.objects.filter(class_id__shift='عصر')

        if assign_m.exists():
            c['class_room_m'] = assign_m

        if assign_e.exists():
            c['class_room_e'] = assign_e

        return render(request, self.template_name, c)


class ClassRoomView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'class-room.html'
    
    def get(self, request, *args, **kwargs):
        number = kwargs.get('number')
        shift = kwargs.get('shift')
        students_in_class_room = models.Student.objects.filter(class_id__number=number, class_id__shift=shift).all()
        return render(request, self.template_name, {'student_class_room': students_in_class_room, 'class': number})


class AttendanceList(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'attendance-list.html'

    def get(self, request, *args, **kwargs):
        class_id_number = kwargs.get('class_id_number')
        att = models.Attendance.objects.filter(attendanceclass__assign__class_id__number=class_id_number)

        date = []
        for i in att:
            date.append(i.date)

        att_list_date = []
        zang_list = []
        for a in att:
            att_list_date.append(a.date)
            zang_list.append(a.zang)

        c = {
            'dates': set(date),
            'class_id_number': class_id_number,
            'att': att,
            'att_date': set(att_list_date),
            'zang_list': set(zang_list)
        }
        return render(request, self.template_name, c)


# add new view for filter zang
class AttendanceEdit(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'attendance-edit.html'

    def get(self, request, *args, **kwargs):
        class_id_number = kwargs.get('class_id_number')
        date = kwargs.get('date')
        zang = kwargs.get('zang')
        att = models.Attendance.objects.filter(attendanceclass__assign__class_id__number=class_id_number, date=date,zang__name=zang)

        c = {
            'att_list': att,
            'class_id_number': class_id_number,
            'date': date,
            'zang': zang
        }
        return render(request, self.template_name, c)
    
    def post(self, request, *args, **kwargs):
        class_id_number = kwargs.get('class_id_number')
        date = kwargs.get('date')
        zang = kwargs.get('zang')
        att = models.Attendance.objects.filter(attendanceclass__assign__class_id__number=class_id_number, date=date,zang__name=zang)
        if request.POST:
            att.update()
            pass
            # return redirect('student:index')
        c={'att_list': att, 'class_id_number': class_id_number}
        return render(self, self.template_name, c)


class AttendanceStudent(generic.View):
    template_name = 'view-attendance-student.html'
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)


class CreateClassView(LoginRequiredMixin, generic.View):
    login_url = 'account:login'
    template_name = 'create-class.html'

    def get(self, request, *args, **kwargs):
        form = forms.ClassForm(request.POST)
        class_ = models.Class.objects.all()
        return render(request, self.template_name, {'form': form, 'class': class_})
    
    def post(self, request, *args, **kwargs):
        class_ = models.Class.objects.all()
        if request.POST:
            form = forms.ClassForm(request.POST)
            if form.is_valid():
                if models.Class.objects.filter(number=request.POST['number'], shift=request.POST['shift']):
                    form.add_error('number', 'این کلاس از قبل ثبت شده است')
                else:
                    form.save()
                    c = models.Class.objects.last()
                    a = models.Assign(class_id=c)
                    a.save()
                    at = models.AttendanceClass(assign=a)
                    at.save()
                    return redirect('student:create-class')
        else:
            form = forms.ClassForm()
        return render(request, self.template_name, {'form': form, 'class': class_})


class ClassDelete(LoginRequiredMixin, generic.DeleteView):
    login_url = 'account:login'
    model = models.Class
    success_url = reverse_lazy('student:create-class')
    

class EditClassView(LoginRequiredMixin, generic.UpdateView):
    login_url = 'account:login'
    template_name = 'create-class.html'
    context_object_name = 'form'
    form_class = forms.ClassForm
    model = models.Class
    success_url = reverse_lazy('student:create-class')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['class'] = models.Class.objects.all()
        return context
        
    def get_object(self, queryset=None):
        return self.model.objects.get(number=self.kwargs['number'], shift=self.kwargs['shift'])


class CreateReshteView(LoginRequiredMixin, generic.CreateView):
    model = models.Reshte
    login_url = 'account:login'
    template_name = 'create-reshte.html'
    success_url = reverse_lazy('student:created-list')
    context_object_name = 'form'
    form_class = forms.ReshteForm
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reshte'] = models.Reshte.objects.all()
        return context


class ReshteDelete(LoginRequiredMixin, generic.DeleteView):
    login_url = 'account:login'
    model = models.Reshte
    success_url = reverse_lazy('student:create-reshte')


@login_required(login_url='account:login')
def reshte_edit(request, pk):
    obj = get_object_or_404(models.Reshte, id=pk)
    form = forms.ReshteForm(request.POST or None, instance=obj)
    reshte = models.Reshte.objects.all()
    if form.is_valid():
        form.save()
        return redirect('student:create-reshte')
    context = {
        'form' : form,
        'reshte' : reshte
    }
    return render(request, 'create-reshte.html', context)
    

class CreateTeacher(LoginRequiredMixin, generic.CreateView):
    login_url = 'account:login'
    template_name = 'create-teacher.html'
    model = User
    form_class = tf.TeacherWeekForm
    success_url = reverse_lazy('student:create-teacher')
    context_object_name = 'form'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['teachers'] = User.objects.all()
        return context


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
        id_code = kwargs.get('id_code')
        student = models.Student.objects.filter(id_code=id_code).first()
        attendance = models.Attendance.objects.filter(student=student).order_by('-date', '-zang').distinct()

        context = {
            'student': student,
            'attendance': attendance
        }
        return render(request, self.template_name, context)


@login_required(login_url='account:login')
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
        assc = get_object_or_404(models.AttendanceClass, assign__class_id__number=assign_class_id)
        ass = assc.assign
        c = ass.class_id
        attendance = models.Attendance.objects.filter(student__class_id__number=assign_class_id, date=assc.date)
        d = timezone.now().date()
        jalali = jalali_converter(d)
        zang = models.Zang.objects.all()
        
        context = {
            'ass': ass,
            'c': c,
            'assc': assc,
            'attendance': attendance,
            'jalali': jalali,
            'zang': zang
        }
        return render(request, self.template_name, context)


def confirm(request, assign_class_id):
    assc = get_object_or_404(models.AttendanceClass, assign__class_id__number=assign_class_id)
    ass = assc.assign
    cl = ass.class_id
    zang = request.POST.get('zang')
    z = models.Zang.objects.get(name=zang)
    
    for i, s in enumerate(cl.student_set.all()):
        status = request.POST.get(s.usn, False)
        if status == 'present':
            status = True
        else:
            status = False
        if assc.status == 1:
            from django.utils import timezone
            if models.Attendance.objects.filter(student=s, date=timezone.now().date(), zang=z).exists():
                pass
            else:
                try:
                    a = models.Attendance.objects.create(student=s, date=assc.date, attendanceclass=assc)
                    a.status = status
                    a.zang = z
                    a.save()
                except models.Attendance.DoesNotExist:
                    a = models.Attendance(student=s, status=status, date=assc.date, attendanceclass=assc)
                    a.zang = z
                    a.save()
        else:
            a = models.Attendance(student=s, status=status, date=assc.date, attendanceclass=assc)
            a.zang = z
            a.save()
            assc.status = 1
            assc.save()
    return redirect('student:attendance',assign_class_id)


def confirm_update(request, assign_class_id, date, zang):
    assc = get_object_or_404(models.AttendanceClass, assign__class_id__number=assign_class_id, zang__name=zang)
    ass = assc.assign
    cl = ass.class_id
    
    for i, s in enumerate(cl.student_set.all()):
        status = request.POST.get(s.usn, False)
        if status == 'present':
            status = True
        else:
            status = False
        if assc.status == 1:
            student_attendnace = models.Attendance.objects.filter(student=s, date=date, zang=zang)
            print(student_attendnace)
    
    return redirect('student:attendance',assign_class_id)


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


def export_csv(request, id_code):
    student = models.Student.objects.filter(id_code=id_code)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attenchment; filename={id_code}.csv'
    write = csv.writer(response)
    write.writerow(['نام و نام خانوادگی', 'نام پدر', 'شماره ملی', 'شماره کلاس', 'شیفت', 'پایه تحصیلی', 'رشته تحصیلی'])
    for s in student:
        write.writerow([s.full_name, s.father_name, s.id_code, s.class_id.number, s.reshte, s.class_id.shift, s.level, s.reshte])
    return response


def render_to_pdf(template_src, context={}):
    template = get_template(template_src)
    html = template.render(context)
    result = BytesIO()
    # pdf = pisa.pisaDocument(BytesIO(html.encode('UTF-8')), result)
    pdf = pisa.CreatePDF(BytesIO(html.encode('utf-8')), dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def export_pdf(request, id_code):
    # template = get_template('pdf-output.html')
    student = models.Student.objects.filter(id_code=id_code).values()
    df = pd.DataFrame(student)
    print(df)
    context = {
        'student': student
    }
    # html = template.render(context)
    pdf = render_to_pdf('pdf-output.html', context)
    if pdf:
        return HttpResponse(pdf, content_type='application/pdf')
    return HttpResponse('Not Found!')