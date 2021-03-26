from django.db import models
from user.models import User
import datetime
from django.utils.translation import ugettext_lazy as _

def year_choices():
    return [(r,r) for r in range(1984, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

STATUS = [(0,'None'),(1,'DEV'),(2,'PROD'),(3,'LIVE'),(4,'CLOSED')]
EMPLOYEMENT = [(0,'None'),(1,'PRINCIPLE'),(2,'HOD'),(2,'PROFESSOR'),(3,'ASST-PROFESSOR'),(4,'ASSOCIAT-PROFESSOR'),(5,'LAB-INCHARGE'),(6,'LAB-ASSISTANT'),]



class Department(models.Model):
    depart_id = models.IntegerField(unique=True, )
    depart_name = models.TextField(unique=True, max_length=512)
    start = models.DateField(auto_now_add=True)
    status = models.SmallIntegerField(choices=STATUS)

    def __str__(self):
        return self.depart_name
    
class Classes(models.Model):

    def class_year(self):
        return datetime.date.today().year
    depart = models.ForeignKey(Department, on_delete=models.CASCADE, limit_choices_to={'status':1,'status':3}  , null=True)
    class_id = models.CharField(max_length=256, unique=True)
    class_name = models.CharField(max_length=256)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'type':2}, null=True )
    assis_professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'type':2}, null=True, related_name='assis' )

    start = models.DateField(auto_now_add=True)
    end = models.DateField(null=True,blank=True)
    status = models.SmallIntegerField(choices=STATUS, default=0)
    class_year = models.DateField(null=True)

    def __str__(self):
        return self.class_id


class ClassHistory(models.Model):
    classes = models.ForeignKey(Classes, on_delete=models.CASCADE)
    professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'type':2}, null=True)
    assis_professor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'type':2}, null=True, related_name='ass')
    start = models.DateField(auto_now_add=True)
    end = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.classes)





    
