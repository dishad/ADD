from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

from .models import Category

@login_required
def index(request):
	return render(request, 'core/index.html',
		{
			'categories': get_categories()
		})

def login(request):

	# request is post, log in 
	#if (request.method == 'POST'):

	#else:
	# request is get, display page
	t = loader.get_template('core/login.html')
	c = Context()
	return HttpResponse(t.render(c))

def createacc(request):

	t = loader.get_template('core/createacc.html')
	c = Context()
	return HttpResponse(t.render(c))

def get_categories():
	return Category.objects.all()