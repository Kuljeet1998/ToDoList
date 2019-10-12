from django.db import models

# Create your models here.
class User(models.Model):
	f_name=models.CharField(max_length=10)
	l_name=models.CharField(max_length=10)
	
	def __str__(self):
		return self.f_name


class Todo(models.Model):
	types=(('created','Created'),('in progress','In Progress'),('completed','Completed'))
	#user=models.ForeignKey(User,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	desc=models.TextField(max_length=500)
	status=models.CharField(max_length=100,choices=types)
	created_time=models.DateTimeField(auto_now_add=True)
	
	def __str__(self):
		return self.title