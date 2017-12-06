from django.shortcuts import render
from main.models import Topic,Webpage,AccessRecord,User

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	users_list = User.objects.all()
	date_dict = {'access_records':webpages_list,'users':users_list}
	return render(request, 'main/index.html',context=date_dict)