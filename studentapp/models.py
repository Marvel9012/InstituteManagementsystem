from django.db import models

# Create your models here.

class City(models.Model):
    City_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.City_name}'


class Course(models.Model):
    Course_name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.Course_name}'


class Student(models.Model):
    Student_name=models.CharField(max_length=50)
    Student_age=models.IntegerField()
    Student_Phno=models.BigIntegerField()
    Student_City=models.ForeignKey(City,on_delete=models.CASCADE)
    Student_Course=models.ForeignKey(Course,on_delete=models.CASCADE)

