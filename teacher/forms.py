from django import forms
from teacher import models
from django.contrib.auth.models import User
from bootstrap_datepicker_plus.widgets import TimePickerInput


valid_time_formats = ['%P', '%H:%M%A', '%H:%M %A', '%H:%M%a', '%H:%M %a']


class UserFullName(User):
    class Meta:
        proxy = True

    def __str__(self):
        return self.get_full_name()


class TeacherWeekForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TeacherWeekForm, self).__init__(*args, **kwargs)
        self.fields['teacher'] = forms.ModelChoiceField(queryset=UserFullName.objects.all())
        self.fields['teacher'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام کاربری را وارد کنید'})
        self.fields['classes'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام کوچک را وارد کنید'})
        self.fields['day'].widget.attrs.update({'class': 'form-control text-center mt-3', 'placeholder': 'نام خانوادگی را وارد کنید'})
        self.fields['start_time'].widget.attrs.update({'class': 'form-control text-center mt-3'})
        self.fields['end_time'].widget.attrs.update({'class': 'form-control text-center mt-3'})

    class Meta:
        model = models.TeacherWeek
        fields = '__all__'
        widgets = {
            'start_time' : TimePickerInput(),
            'end_time' : TimePickerInput(),
        }

    def clean_end_time(self):
        data = super(TeacherWeekForm, self).clean()
        start_time = self.cleaned_data.get('start_time')
        end_time = self.cleaned_data.get('end_time')
        if start_time.hour >= end_time.hour:
            raise forms.ValidationError('ساعت شروع از ساعت پایان بیشتر میباشد')
        return

