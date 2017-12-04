from django.shortcuts import render
from main.models import Topic,Webpage,AccessRecord

def index(request):
	webpages_list = AccessRecord.objects.order_by('date')
	date_dict = {'access_records':webpages_list}
	return render(request, 'main/index.html',context=date_dict)