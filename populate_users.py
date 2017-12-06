import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','public_python.settings')

import django

django.setup()

import random
from main.models import User
from faker import Faker

fakegen = Faker()

def populate(N=5):
	for entry in range(N):
		fake_email = fakegen.email()
		fake_lastname = fakegen.last_name()
		fake_firstname = fakegen.first_name()
		user = User.objects.get_or_create(firstname=fake_firstname,lastname=fake_lastname,email=fake_email)[0]

if __name__ == '__main__':
	print("populating scritps!")
	populate(20)
	print("populating complete")