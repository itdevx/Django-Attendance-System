from django import forms
from Student.models import Attendance, Student
from django.utils import timezone


class AttendanceForm(forms.ModelForm):
    def __init__(self, class_name, *args, **kwargs):
        super(AttendanceForm, self).__init__(*args, **kwargs)
        self.fields['student'].queryset = Student.objects.filter(class_room__name=class_name)
        self.fields['student'].widget.attrs.update({'class': 'form-control text-center'})     
        self.fields['alarm'].widget.attrs.update({'class': 'form-control text-center mt-3'})     
        self.fields['attendance'].widget.attrs.update({'class': 'form-control text-center mt-3', 'id': 'status', 'onchange': 'changeStatus()'})
        self.fields['time_takhir'].widget.attrs.update({'class': 'form-control text-center mt-3', 'id': 'tt', 'placeholder': 'زمان تاخیر را میتوانید به عدد و حروف وارد کنید'})     
        self.fields['gheybat_movajah'].widget.attrs.update({'class': 'form-control text-center mt-3 p-2', 'id': 'gm', 'placeholder': 'غیبت موجه'})     
        self.fields['gheybat_gheyr_movajah'].widget.attrs.update({'class': 'form-control text-center mt-3 p-2', 'id': 'gg', 'placeholder': 'غیبت غیر موجه'})
        self.fields['morkhasi'].widget.attrs.update({'class': 'form-control text-center mt-3', 'id': 'mor', 'placeholder': 'اطلاعات مربوط به مرخصی را وارد کنید'})

    class Meta:
        model = Attendance
        fields = '__all__'

    def clean_student(self):
        student = self.cleaned_data['student']
        filtering = Attendance.objects.filter(student=student)
        if not filtering:
            return student
        if filtering.exists() and timezone.now().month == filtering.last().date_attendance.month and timezone.now().day == filtering.last().date_attendance.day:
            raise forms.ValidationError('این دانش آموز یک بار در این روز ثبت شده است')
        return student
        

class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام را وارد کنید'})
        self.fields['last_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام خانوادگی را وارد کنید'})
        self.fields['father_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام پدر را وارد کنید'})
        self.fields['id_code'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'کدملی را وارد کنید'})
        self.fields['class_room'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['level'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        
    class Meta:
        model = Student
        exclude = ['level_up']
