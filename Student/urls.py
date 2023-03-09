from unicodedata import name
from django.urls import path
from Student import views


app_name = 'student'

urlpatterns = [
    path(
        '', views.IndexView.as_view(), name='index'
    ),
    path(
        'creative-settings', views.WalletView.as_view(), name='created-list'
    ),
    path(
        'class-room/<number>/<shift>', views.ClassRoomView.as_view(), name='class-room'
    ),
    path(
        'create-student', views.CreateStudenView.as_view(), name='create-student'
    ),
    path(
        'student/<id_code>', views.StudentInfoView.as_view(), name='student'
    ),
    path(
        'attendance/<int:assign_class_id>/', views.AttendanceView.as_view(), name='attendance'
    ),
    path(
        'attendance/<int:assign_class_id>/confirm', views.confirm, name='confirm'
    ),
    path(
        'student-edit/<full_name>/<id_code>', views.student_edit, name='student-edit'
    ),
    path(
        'search/', views.SearchingView.as_view(), name='search'
    ),
    path(
        'created/create-class/', views.CreateClassView.as_view(), name='create-class'
    ),
    path(
        'edited/delete-class/<int:pk>', views.ClassDelete.as_view(), name='delete-class'
    ),
    path(
        'edited/edit-class/<number>/<shift>', views.class_edit, name='edit-class'
    ),
    path(
        'created/create-reshte/', views.CreateReshteView.as_view(), name='create-reshte'
    ),
    path(
        'edited/delete-reshte/<int:pk>', views.ReshteDelete.as_view(), name='delete-reshte'
    ),
    path(
        'edited/edit-reshte/<int:pk>', views.reshte_edit, name='edit-reshte'
    ),
    path(
        'attendance-list/<class_id_number>/', views.AttendanceList.as_view(), name='attendance-list'
    ),
    path(
        'attendance-edit/<class_id_number>/<date>/<zang>/', views.AttendanceEdit.as_view(), name='attendance-edit'
    ),
    path(
        'student/export-csv/<id_code>/', views.export_csv, name='export-csv' 
    ),
    path(
        'student/export-pdf/<id_code>/', views.export_pdf, name='export-pdf' 
    ),

]
