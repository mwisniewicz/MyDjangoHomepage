import re
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=264,unique=True)
	publication_date = models.DateField()
	text = models.CharField(max_length=1000)
	thumbnail = models.ImageField(upload_to='blog/%Y/%m/%d')

	@classmethod
	def getTeaser(self):
		temp = re.findall(r'\w+',self.text)
		count = len(temp)
		return count
		

	def __str__(self):
		return self.title