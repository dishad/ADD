from django import forms
from django.contrib.auth.models import User

# forms will go here. create account has been added, new post form will probably go here

'''
class LoginForm(forms.ModelForm):

	class Meta:

		model = User
		fields = ('username', 'password')
'''

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

	username = forms.CharField(label="Username:", max_length=30)
	email = forms.CharField(label="Email:", max_length=30)
	secquestion = forms.CharField(label="What is your mother's maiden credit card number?", max_length=50)

	class Meta:
		model = User
		fields = ('username', 'email')


