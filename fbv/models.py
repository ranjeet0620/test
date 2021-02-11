from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator,MinValueValidator,MaxValueValidator

# Create your models here.
#e1=Employee(name='Ranjeet',age=30,email='ranjeet@gmail.com')
class Employee(models.Model):
    name=models.CharField(max_length=30)
    age=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f'''{self.name}'''

    class Meta:
        db_table='EMP_INFO'

#a1=Address(city='Pune', pin=415712)
class Address(models.Model):
    city=models.CharField(max_length=30)
    pin=models.IntegerField(validators=[MinValueValidator(111111),MaxValueValidator(999999)])
    empref=models.OneToOneField(Employee,null=True,on_delete=models.CASCADE,related_name='adrref')

    def __str__(self):
        return f'''{self.city}'''
    class Meta:
        db_table='adr_info'


