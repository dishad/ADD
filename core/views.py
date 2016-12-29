from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login

from .models import Category

# Create your views here.
@login_required
def index(request):
	t = loader.get_template('core/index.html')
	c = Context()
	return HttpResponse(t.render(c))

def login(request):

	# request is post, log in 
	if (request.method == 'POST'):

		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('core/index.html')
		else:
			return HttpResponse('Error: could not log in')

	else:
		# request is get, display page
		t = loader.get_template('core/login.html')
		c = Context()
		return HttpResponse(t.render(c))

def logout(request):
	logout(request)
	return redirect('%s?next=%s', (settings.LOGIN_URL, request.path))

def createacc(request):

	t = loader.get_template('core/createacc.html')
	c = Context()
	return HttpResponse(t.render(c))