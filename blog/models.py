import re
from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=264,unique=True)
	publication_date = models.DateField()
	text = models.TextField()
	
	def __str__(self):
		return self.title