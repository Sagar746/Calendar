from django.db import models

# Create your models here.

class Calendar(models.Model):
	name=models.CharField(max_length=200)
	description=models.TextField(max_length=200)

	def __str__(self):
		return self.name

class Event(models.Model):

	COLOR_CHOICE=(
		('red','Red'),
		('blue','Blue'),
		('teal','Teal'),
		('green','Green'),
		('orange','Orange')
	)

	title = models.CharField(max_length=200)
	start = models.DateTimeField()
	end = models.DateTimeField()
	color=models.CharField(max_length=10,choices=COLOR_CHOICE,default='red')
	description = models.TextField(max_length=200)
	calendar=models.ForeignKey(Calendar,on_delete=models.CASCADE,null=True,related_name='events')
	created_at = models.DateTimeField(auto_now_add=True)
	participants = models.TextField(null=True, default='')

	def __str__(self):
		return f'{self.title} started from {self.start_date} to {self.end_date}'





