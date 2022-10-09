from django import forms
from Student import models
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget


class StudentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام و نام خانوادگی را وارد کنید'})
        self.fields['father_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام پدر را وارد کنید'})
        self.fields['id_code'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'کدملی را وارد کنید'})
        self.fields['class_id'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['reshte'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['level'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['usn'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'usn را وارد کنید'})
        self.fields['date'].widget.attrs.update({'class': 'form-control date text-center mt-3'})
        
    class Meta:
        model = models.Student
        exclude = ['level_up']


class StudentEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(StudentEditForm, self).__init__(*args, **kwargs)
        self.fields['full_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام و نام خانوادگی را وارد کنید'})
        self.fields['father_name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام پدر را وارد کنید'})
        self.fields['id_code'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'کدملی را وارد کنید'})
        self.fields['class_id'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['reshte'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['level'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['usn'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'usn را وارد کنید'})
        self.fields['date'].widget.attrs.update({'class': 'form-control date text-center mt-3'})

    class Meta:
        model = models.Student
        fields = '__all__'

    def save(self, *args, **kwargs):
        return super(StudentEditForm, self).save(*args, **kwargs)

    
class ClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ClassForm, self).__init__(*args, **kwargs)
        self.fields['number'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['shift'].widget.attrs.update({'class': 'form-control text-center mt-3'})

    class Meta:
        model = models.Class
        fields = '__all__'

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if models.Class.objects.filter(number=number).exists():
            raise forms.ValidationError('این کلاس از قبل ثبت شده است')
        else:
            return number

class AssignForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AssignForm, self).__init__(*args, **kwargs)
        self.fields['class_id'].widget.attrs.update({'class': 'form-control text-center mt-3'})

    class Meta:
        model = models.Assign
        fields = '__all__'

    def clean_class_id(self):
        class_id = self.cleaned_data['class_id']
        if models.Assign.objects.filter(class_id=class_id).exists():
            raise forms.ValidationError('این کلاس قبلا اختصاص یافته است')
        else:
            return class_id


class AttendanceClassForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AttendanceClassForm, self).__init__(*args, **kwargs)
        self.fields['assign'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        # self.fields['status'].widget.attrs.update({'class': 'form-control text-center mt-3'})

    class Meta:
        model = models.AttendanceClass
        fields = ['assign']

    def clean_assign(self):
        assign = self.cleaned_data['assign']
        if models.AttendanceClass.objects.filter(assign=assign).exists():
            raise forms.ValidationError('این ساخته شده است')
        else:
            return assign
    

class ReshteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReshteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'رشته تحصیلی را وارد کنید'})

    class Meta:
        model = models.Reshte
        fields = '__all__'

    def clean_name(self):
        name = self.cleaned_data['name']
        if models.Reshte.objects.filter(name=name).exists():
            raise forms.ValidationError('این رشته تحصیلی از قبل ثبت شده است')
        else:
            return name
        
class EditReshteForm(forms.ModelForm):
    def __init__(self ,*args, **kwargs):
        super(ReshteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'رشته تحصیلی را وارد کنید'})

    class Meta:
        model = models.Reshte
        fields = '__all__'