from django.forms import ModelForm
from django import forms
from predict.models import user_model
from predict.models import user_siup






class UserForm(forms.ModelForm):
	class Meta:
		model = user_model
		fields = '__all__'

class UserForm1(forms.ModelForm):
	class Meta:
		model = user_siup
		fields = '__all__'
