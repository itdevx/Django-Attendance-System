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
        'student/<full_name>/<id_code>', views.StudentInfoView.as_view(), name='student'
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
        'created/create-assign/', views.CreateAssignView.as_view(), name='create-assign'
    ),
    path(
        'created/create-attendance-class/', views.CreateAttendanceClassView.as_view(), name='create-attendance-class'
    ),
    path(
        'created/create-reshte/', views.CreateReshteView.as_view(), name='create-reshte'
    ),
]






# urlpatterns = [
#     path(
#         '', views.IndexView.as_view(), name='index',
#     ),
#     path(
#         'class-room/<shift>/<class_name>', views.ClassRoomView.as_view(), name='class_room'
#     ),
#     path(   
#         'attendance/<class_name>', views.AttendanceView.as_view(), name='attendance'
#     ),
#     path(
#         'create-student', views.CreateStudentView.as_view(), name='create-student'
#     ),
#     path(
#         'student-info/<last_name>/<id_code>', views.StudentInfo.as_view(), name='student-info'
#     ),
#     # path(
#     #     'student-edit/<int:id_code>', views.StudentEdit.as_view(), name='student-edit'
#     # ),
#     path(
#         'student-edit/<id_code>', views.student_edit, name='student-edit'
#     ),
#     path(
#         'attendance-test/<class_name>', views.AttendanceViewTest.as_view(), name='a-test'
#     ),
#     path(
#         'wallet', views.WalletView.as_view(), name='wallet'
#     )
# ]