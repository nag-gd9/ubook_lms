from django.db import models
from django.contrib.auth.models import AbstractUser


# YEAR_IN_SCHOOL_CHOICES = [('1', '1 class'),('2', '2 class'),('3', '3 class'),('4', '4 class'),('5', '5 class'),('6', '6 class'),('7', '7 class'),('8', '8 class'),('9', '9 class'),('10', '10th class'),]

class User(AbstractUser):
    type = models.CharField(max_length=256, choices=(('1','Student'), ('2','Professor'), ('3','lower_staf')), default='1')  


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True )
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, blank=True, null=True)
    birth = models.DateField(blank=True)
    gender = models.BooleanField(choices=(('Male','Male'), ('Female','Female'), ('Trans','Trans')), default='Male') 
    adhar = models.IntegerField(blank=True, null=True)
    father_name = models.CharField(max_length=256, blank=True,null=True )
    mother_name = models.CharField(max_length=256, blank=True, null=True)
    student_class = models.CharField(max_length=256)
    student_section = models.CharField(max_length=50,blank=True, null=True)
    fav_language = models.CharField(max_length=50,blank=True, null=True)
    contact_number = models.IntegerField(null=True,blank=True)
    addr = models.TextField(blank=True, default='Home')
    email = models.CharField(max_length=256,blank=True, null=True)

    def __str__(self):
        return '{}'.format(self.user)
    