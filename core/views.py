from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User

from core.models import Category
from core.forms import CreateAccForm

# Create your views here.
@login_required
def index(request):
	t = loader.get_template('core/index.html')
	c = Context()
	return HttpResponse(t.render(c))

def login(request):

	# request is post, log in 
	if request.method == 'POST':

		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)

			return HttpResponseRedirect('core/index.html')


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


# create account view
def createacc(request):

	if request.method == "POST":

		form = CreateAccForm(request.POST)
		if form.is_valid():

			print("about to create new user")
			new_user = User.objects.create_user(**form.cleaned_data)
			login(new_user)

			print("new user created: " + new_user.get_username() + " " + new_user.get_full_name())

			return HttpResponseRedirect('core/index.html');

		else:

			print("invalid form")
			form = CreateAccForm()

			return render(request, 'core/createacc.html', {'form': form})

	else:
		form = CreateAccForm()

		#t = loader.get_template('core/createacc.html')
		#c = Context({form: "form"})
		#return HttpResponse(t.render(c))
		return render(request, 'core/createacc.html', {'form': form})