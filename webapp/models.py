from django.db import models

# Create your models here.
class onlineuser(models.Model):
	name=models.CharField(max_length=100);
	email=models.CharField(max_length=100);
	phone=models.CharField(max_length=100);
	pwd=models.CharField(max_length=100);
	gender=models.CharField(max_length=100);
	age=models.CharField(max_length=100);

class bookings(models.Model):
	service=models.CharField(max_length=100);
	date=models.CharField(max_length=100);
	user=models.CharField(max_length=100);
	