from django.db import models
from user.models import User


def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+6)]


class Registrar(models.Model):
    registorar = models.ForeignKey(User, on_delete = models.DO_NOTHING)
    is_active = models.BooleanField(default=True)
    start = models.DateField(auto_now_add=False)
    end = models.DateField()

    def __str__(self):
        return self.registorar


class Course(models.Model):
    course_id = models.IntegerField(primary_key=True)
    course_name = models.CharField(max_length=512)
    start = models.DateField(null=True, blank=true)
    end = models.DateField(null=True, blank=true)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return '%s %s' %(self.course_id, self.course_name)


class Rivison(models.Model):
    rigistrar = models.ForeignKey(Rigistrar, on_delete=models.DO_NOTHING)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    rivison = models.IntegerField(choicess=year_choices)


    
    

