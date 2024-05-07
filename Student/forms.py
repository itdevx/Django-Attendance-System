from django import forms
from Student import models
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from bootstrap_datepicker_plus.widgets import DatePickerInput



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
        widgets = {
            'date': DatePickerInput()
        }


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

    

class ReshteForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(ReshteForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'رشته تحصیلی را وارد کنید'})

    class Meta:
        model = models.Reshte
        fields = '__all__'
