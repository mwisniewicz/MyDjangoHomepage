from django.contrib import admin
from main.models import Topic,Webpage,AccessRecord

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)