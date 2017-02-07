from django.shortcuts import render, redirect, reverse
from .models import User

# Create your views here.
def index(request):
	if request.method == 'POST':
		return createUser(request)
		
	users = User.objects.all().order_by('name')
	pages = len(users)

	context = {'users': User.objects.all().order_by('name'), 'pages': 0}
	return render(request, 'pagination_app/index.html', context)

def createUser(request):
	results = User.objects.createUser(request.POST)
	if results[1]:
		return redirect(reverse('pagination:index'))

	for error in results[0]:
		messages.error(request, error)
	return redirect(reverse('pagination:index'))

def filter(request):
	users = User.objects.getUsers(request.POST)

	context = {
		'users': users[0],
		'pages': users[1]
	}

	print context['pages']
	print users
	return render(request, 'pagination_app/index.html', context)

