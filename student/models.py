from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class StudentRecord(models.Model):
    """
    student Details models.
    """
    student_name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100,null=True,blank=True)
    date_of_birth = models.DateField()
    address = models.TextField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=20)
    pin = models.CharField(max_length=6)
    phone_number = models.CharField(max_length=10,unique=True,null=True,blank=True)
    email = models.EmailField(unique=True,null=True,blank=True)
    class_opted = models.IntegerField(
                          validators=[MinValueValidator(5),
                                      MaxValueValidator(10)])
    marks = models.IntegerField(validators=[MinValueValidator(1),
                                      MaxValueValidator(100)])
    date_enrolled = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'student_record'


    def __str__(self):
        return self.student_name 
    
