from django.urls import path
from teacher import views

app_name = 'teacher'

urlpatterns = [
    path(
        'teacher-week-table/<username>', views.TeacherWeekTable.as_view(), name='teacher-wt'
    ),
    path(
        '', views.Teacher.as_view(), name='teacher'
    )
]