from django.contrib import admin
from main.models import Topic,Webpage,AccessRecord,User

admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic)
admin.site.register(User)