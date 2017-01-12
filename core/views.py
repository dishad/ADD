from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate
from django.contrib.auth import login as login_user
from django.contrib.auth import logout as logout_user
from django.contrib.auth.models import User

from core.models import Category, Post
from core.forms import CreateAccForm, ForgotPasswordForm, PostForm

@login_required
def index(request):

	newpostform = PostForm()

	return render(request, 'core/index.html',
		{
			'categories': get_categories(),
			'form': newpostform
		})

def login(request):

	# request is post, log in 
	if request.method == 'POST':

		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username, password=password)
		if user is not None:
			login_user(request, user)

			return HttpResponseRedirect('/')


		else:
			return HttpResponse('Error: could not log in')

	else:
		# request is get, display page
		t = loader.get_template('core/login.html')
		c = Context()
		return HttpResponse(t.render(c))

def logout(request):
	logout_user(request)
	return redirect('%s?next=%s', (settings.LOGIN_URL, request.path))


# create account view
def createacc(request):

	form = CreateAccForm()

	if request.method == "POST":

		form = CreateAccForm(request.POST)
		if form.is_valid():

			print("about to create new user")
			first_name = form.cleaned_data.get('first_name')
			last_name = form.cleaned_data.get('last_name')
			username = form.cleaned_data.get('username')
			email = form.cleaned_data.get('email')
			password = form.cleaned_data.get('password')
			new_user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
			new_user = authenticate(username=username, password=password)

			if new_user:
				login_user(request, new_user)
				print("new user created: " + new_user.get_username() + " " + new_user.get_full_name())
				return HttpResponseRedirect('/');
			else:
				print('failed to authenticate user')

		else:

			print("invalid form")

			return render(request, 'core/createacc.html', {'form': form})

	else:

		return render(request, 'core/createacc.html', {'form': form})

# forgot password
def forgotpassword(request):

	#if request.method == 'POST'

		#TODO: forgot password functionality

	#else

	return render(request, 'core/forgotpassword.html', {'form': form})

def newpost(request):

	form = PostForm(request.POST)

	if form.is_valid():

		cur_user = request.user


		title = form.cleaned_data.get('title')
		price = form.cleaned_data.get('price')
		description = form.cleaned_data.get('description')
		poster = cur_user.id
		category = form.cleaned_data.get('category')
		subcategory = form.cleaned_data.get('subcategory')

		Post.objects.create(title=title, price=price, description=description, poster=poster, category=category)

		HttpResponseRedirect('/newpostsuccess')

	else:
		print('form not valid')

		HttpResponseRedirect('/')
def newpostsuccess(request):
	return render(request, 'core/newpostsuccess.html')


def get_categories():
	return Category.objects.all()

