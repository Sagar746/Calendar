from django.db import models

# Create your models here.

class Calendar(models.Model):
	calendar_name=models.CharField(max_length=200)
	description=models.TextField(max_length=200)

	def __str__(self):
		return self.calendar_name

class Participant(models.Model):
	email=models.EmailField(unique=True)

	def __str__(self):
		return self.email

COLOR_CHOICE=(
	('red','Red'),
	('blue','Blue'),
	('yellow','Yellow'),
	('green','Green'),
	('orange','Orange')
)

class Event(models.Model):
	title = models.CharField(max_length=200)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	color=models.CharField(max_length=10,choices=COLOR_CHOICE,default='red')
	participants=models.ForeignKey(Participant,on_delete=models.CASCADE,null=True,related_name='events')
	description = models.TextField(max_length=200)
	calendar=models.ForeignKey(Calendar,on_delete=models.CASCADE,null=True,related_name='events')
	created_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.title} started from {self.start_date} to {self.end_date}'