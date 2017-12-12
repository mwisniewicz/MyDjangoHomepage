from django.shortcuts import render
from blog.models import Article

def index(request):
	articles_list = Article.objects.order_by('-publication_date')
	articles_dict = {'articles':articles_list}
	return render(request, 'blog/index.html',context=articles_dict)