from django.contrib import admin
from.models import User, Student, JobHistory, Projects
from django.contrib.auth.admin import UserAdmin

class CustomUserAdmin(UserAdmin):

    fieldsets = UserAdmin.fieldsets + ((None, {'fields': ('type',)}),)
    add_fieldsets = UserAdmin.add_fieldsets + ((None, {'fields': ('type',)}),)


admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Projects)
admin.site.register(JobHistory)