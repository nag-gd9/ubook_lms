from django.contrib import admin
from .models import Department, Classes, ClassHistory

# Register your models here.
admin.site.register(Department, admin.ModelAdmin)
admin.site.register(Classes)
admin.site.register(ClassHistory)
