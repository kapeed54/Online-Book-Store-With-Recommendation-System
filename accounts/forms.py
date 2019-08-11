from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms

class EditProfileForm(UserChangeForm):
	email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	first_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	address = forms.CharField (label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
	phone_number = forms.CharField (label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))
	password = forms.CharField(label='', widget=forms.TextInput(attrs={'type':'hidden'}))

	class Meta:
		model = User
		fields = ('username', 'first_name',
			'last_name', 'email','address','phone_number','password',)

	def __init__(self, *args, **kwargs):
		super(EditProfileForm, self).__init__(*args, **kwargs)
		
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<div class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></div>'




class SignUpForm(UserCreationForm):
	email = forms.EmailField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Email Address'}))
	first_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}))
	last_name = forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}))
	address= forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Address'}))
	phone_number= forms.CharField(label='',max_length=100, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}))

	class Meta:
		model = User
		fields = ('username', 'first_name','last_name', 'email','address','phone_number', 'password1','password2')

	def __init__(self, *args, **kwargs):
		super(SignUpForm, self).__init__(*args, **kwargs)
		
		self.fields['username'].widget.attrs['class'] = 'form-control'
		self.fields['username'].widget.attrs['placeholder'] = 'User Name'
		self.fields['username'].label = ''
		self.fields['username'].help_text = '<div class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></div>'
		
		self.fields['password1'].widget.attrs['class'] = 'form-control'
		self.fields['password1'].widget.attrs['placeholder'] = 'Password'
		self.fields['password1'].label = ''
		self.fields['password1'].help_text = '<small><ul class="form-text text-muted"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul></small>'
		
		self.fields['password2'].widget.attrs['class'] = 'form-control'
		self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
		self.fields['password2'].label = ''
		self.fields['password2'].help_text = '<div class="form-text text-muted"><small>Enter the same Password as before for verification</small></div>'


