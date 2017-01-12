from django import forms
from django.contrib.auth.models import User
from core.models import Post, Category

# forms will go here. create account has been added, new post form will probably go here

class CreateAccForm(forms.ModelForm):

	#form labels
	#first_name = forms.CharField(label="First Name:", max_length=30)
	#last_name = forms.CharField(label="Last Name:", max_length=30)
	#username = forms.CharField(label="Username:", max_length=30)
	#email = forms.CharField(label="Email:", max_length=30)
	#password = forms.CharField(label="Password:", max_length=30, widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'email', 'password')
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
			'password': forms.PasswordInput(attrs={'class': 'form-control'}),
		}

class ForgotPasswordForm(forms.ModelForm):

	secquestion = forms.CharField(label="What is your mother's maiden credit card number?", max_length=50)

	class Meta:
		model = User
		fields = ('username', 'email')
		widgets = {
			'username': forms.TextInput(attrs={'class': 'form-control'}),
			'email': forms.TextInput(attrs={'class': 'form-control'}),
		}

class PostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = ('title', 'price', 'description')
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'price': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control', 'rows': '10'}),
			#'category': forms.
		}


