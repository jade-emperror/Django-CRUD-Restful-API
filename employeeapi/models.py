from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    choices=[('intern','intern'),('hr','hr'),('manager','manager'),('developer','developer')]
    fullname = models.CharField(max_length=100)
    uname=models.ForeignKey(User,on_delete=models.CASCADE)
    emp_type = models.CharField(choices=choices,max_length=9)
    emp_code = models.CharField(max_length=3,primary_key=True)
    mobile = models.CharField(max_length=15)

class performance(models.Model):
    emp_code=models.ForeignKey(Employee,on_delete=models.CASCADE)
    rating = models.DecimalField(max_digits=2,decimal_places=2)

#performance
#api authentication