from django import forms
from blog.models import Article

class FormArticle(forms.ModelForm):
	class Meta:
		model = Article
		fields = '__all__'