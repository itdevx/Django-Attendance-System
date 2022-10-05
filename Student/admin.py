from django.contrib import admin
from Student.models import Assign, Attendance, AttendanceClass, Class, Reshte, Student

admin.site.register(Assign)
admin.site.register(Attendance)
admin.site.register(AttendanceClass)
admin.site.register(Class)
admin.site.register(Reshte)
admin.site.register(Student)






# from Student.models import ClassRoom, Student, Attendance
# @admin.register(Student)
# class StudentAdmin(admin.ModelAdmin):

#     def shift(self, obj):
#         return obj.class_room
#     shift.short_description = 'shift'

#     list_display = ['first_name', 'last_name', 'father_name', 'id_code', 'level', 'shift']
#     list_filter = ['first_name', 'last_name', 'id_code']
    

# @admin.register(ClassRoom)
# class ClassRoomAdmin(admin.ModelAdmin):
    
#     def shift(self, obj):
#         return obj.class_room
#     shift.short_description = 'shift'

#     list_display = ['name', 'shift']


# @admin.register(Attendance)
# class AttendanceAdmin(admin.ModelAdmin):
#     def student(self, obj):
#         return obj.student
    
#     student.short_description = 'student'

#     list_display = ['student', 'attendance', 'date_attendance']
    