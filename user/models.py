from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db.models.signals import post_save
from django.dispatch import receiver
import datetime
from django.utils.timezone import now


class User(AbstractUser):
    gender = models.SmallIntegerField(choices=((0,'None'), (1,'Mmale'), (2,'Female'), (3,'Trans')), default=0) 
    adhar = models.IntegerField(blank=True, null=True, unique=True)
    dob = models.DateField(blank=True, null=True, )
    father_name = models.CharField(max_length=256, blank=True,null=True )
    mother_name = models.CharField(max_length=256, blank=True, null=True)
    type = models.IntegerField(choices=((0,'None'), (1,'Student'), (2,'Staff'), (3,'lower_staf')), default=0)
  


class Student(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, limit_choices_to={'type':1}, )
    contact_number = models.IntegerField(null=True,blank=True)
    addr = models.TextField(blank=True, default='Home')
    email = models.CharField(max_length=256,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.user)


EMPLOYEMENT = [(0,'None'),(1,'PRINCIPLE'),(2,'HOD'),(2,'PROFESSOR'),(3,'ASST-PROFESSOR'),(4,'ASSOCIAT-PROFESSOR'),(5,'LAB-INCHARGE'),(6,'LAB-ASSISTANT'),]
PROJECT_STATUS = [(0,'None'),(1,'DEV'),(2,'PROD'),(3,'LIVE'),(4,'CLOSED')]


class Projects(models.Model):
    pr_id = models.CharField(max_length=256, unique=True)
    pr_name = models.CharField(max_length=256)
    client = models.CharField(max_length=256)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(null=True,blank=True)
    status = models.SmallIntegerField(choices=PROJECT_STATUS, default=0)

    def __str__(self):
        return self.pr_id


class JobHistory(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'type':2}, )
    designation = models.SmallIntegerField(choices=EMPLOYEMENT, default=0)
    start = models.DateField(auto_now_add=True)
    end = models.DateField(null=True,blank=True)

    def __str__(self):
        return str(self.project)





    
            







# class YearInSchool(models.Model):
#     pass

# @receiver(post_save, sender=User)
# def create_student(sender, instance, created, **kwargs):
#     if created:
#         Student.objects.create(user=instance)
    

# @receiver(post_save, sender=User)
# def save_student(sender, instance, **kwargs):
#     instance.student.save()