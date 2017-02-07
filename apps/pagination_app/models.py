from __future__ import unicode_literals

from datetime import datetime
from django.utils import timezone
from django.db import models
from django.db.models import Q
import math
# Create your models here.
class ValidationManager(models.Manager):
	def createUser(self, form_info):
		errors = []

		if len(form_info['name']) < 2:
			errors.append('First name not valid.')
		if len(form_info['email']) < 2:
			errors.append('Email not valid.')

		if len(errors) > 0:
			return (errors, False)

		User.objects.create(name=form_info['name'], email=form_info['email'])
		return (errors, True)
	def getUsers(self, form_info):

		# if len(form_info['name']) > 0 and len(form_info['email']) > 0:
		# 	users = User.objects.filter(name__icontains=form_info['name'], email__icontains=form_info['email']).order_by('name')
		# elif len(form_info['name']) > 0 and len(form_info['email']) == 0:
		# 	users = User.objects.filter(name__icontains=form_info['name']).order_by('name')
		# elif len(form_info['name']) == 0 and len(form_info['email']) > 0:
		# 	users = User.objects.filter(email__icontains=form_info['email']).order_by('name')
		# else: 
		# 	users = User.objects.all().order_by('name')

		if form_info['start_date'] == '':
			start_date = datetime(1800, 01, 01)
		else:
			start_date = form_info['start_date']

		if form_info['end_date'] == '':
			end_date = datetime.now()
		else:
			end_date = form_info['end_date']

		users = User.objects.filter(name__icontains=form_info['name'], email__icontains=form_info['email']).filter(created_at__range=[start_date, end_date]).order_by('name')

		pages = math.ceil(len(users)/5)
		
		print pages
		return (users, pages)



class User(models.Model):
	name = models.CharField(max_length=55)
	email = models.CharField(max_length=55)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	objects = ValidationManager()