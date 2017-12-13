from django.shortcuts import render
from blog.models import Article
from . import forms

def index(request):
	articles_list = Article.objects.order_by('-publication_date')
	articles_dict = {'articles':articles_list}
	return render(request, 'blog/index.html',context=articles_dict)

def form_article_view(request):
	form = forms.FormArticle()
	if request.method == 'POST':

		form = forms.FormArticle()
		
		if form.is_valid():

			print("Form is VALID")
		else:
			print("not walid")

	return render(request,'blog/create-post.html', {'form':form})