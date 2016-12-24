from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Context, loader
from django.contrib.auth.decorators import login_required

from .models import Category

# Create your views here.
@login_required
def index(request):
	t = loader.get_template('core/index.html')
	c = Context()
	return HttpResponse(t.render(c))