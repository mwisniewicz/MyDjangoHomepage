from django.db import models

class Article(models.Model):
	title = models.CharField(max_length=264,unique=True)
	publication_date = models.DateTimeField()
	text = models.TextField()
	thumbnail = models.ImageField(upload_to='blog/%Y/%m/%d')

	def __str__(self):
		return self.title