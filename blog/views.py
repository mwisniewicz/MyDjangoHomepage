from django.shortcuts import render
from blog.models import Article
from . import forms
from blog.forms import FormArticle

def index(request):
	articles_list = Article.objects.order_by('-publication_date')
	articles_dict = {'articles':articles_list}
	return render(request, 'blog/index.html',context=articles_dict)

def form_article_view(request):
	form = FormArticle(None)
	if request.method == 'POST':
		form = FormArticle(request.POST)
		if form.is_valid():
			form.save(commit=True)
			print("Form is VALID")
			return index(request)

		else:
			print("not walid")

	return render(request,'blog/create-post.html', {'form':form})