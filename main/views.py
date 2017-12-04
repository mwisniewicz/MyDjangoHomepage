from django.shortcuts import render

def index(request):
    my_dict = {'title': 'Welcome to my Django Page'}
    return render(request, 'main/index.html', context=my_dict)