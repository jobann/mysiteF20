from django.db import models
import datetime
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    length = models.IntegerField(blank=False, null=False, default=12)

    def __str__(self):
        return self.name


class Course(models.Model):
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Student(User):
    LVL_CHOICES = [
        ('HS', 'High School'),
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('ND', 'No Degree'),
    ]

    level = models.CharField(choices=LVL_CHOICES, max_length=2, default='HS')
    address = models.CharField(max_length=300, blank=True, null=True)
    province = models.CharField(max_length=2, default='ON')
    registered_courses = models.ManyToManyField(Course, blank=True)
    interested_in = models.ManyToManyField(Topic)


class Order(models.Model):
    ODR_CHOICES = [
        (0, 'Cancelled'),
        (1, 'Confirmed'),
        (2, 'On Hold')
    ]
    courses = models.ManyToManyField(Course)
    student = models.ForeignKey(Student,  on_delete=models.CASCADE, null=True)
    order_status = models.IntegerField(choices=ODR_CHOICES, default=1)
    order_date = models.DateField(default=timezone.now)

    def total_cost(self):
        total_cost = 0
        for c in self.courses.all():
            total_cost = total_cost + c.price
        return total_cost

