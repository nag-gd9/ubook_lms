from django.contrib import admin
from.models import User, Student
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('type',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('type',)}),)

class Student_admin(admin.ModelAdmin):
    pass

admin.site.register(User, CustomUserAdmin)
admin.site.register(Student, Student_admin)