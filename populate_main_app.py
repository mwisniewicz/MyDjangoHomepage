import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','public_python.settings')

import django

django.setup()

import random
from main.models import Topic,Webpage,AccessRecord
from faker import Faker

fakegen = Faker()

topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):
	for entry in range(N):
		top = add_topic()
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()

		#CREATE NEW WEBPAGE ENTRY

		webpg = Webpage.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]

		#CREATE FAKE ACCESS RECORD

		acc_rec = AccessRecord.objects.get_or_create(name=webpg,date=fake_date)[0]

if __name__ == '__main__':
	print("populating scritps!")
	populate(20)
	print("populating complete")