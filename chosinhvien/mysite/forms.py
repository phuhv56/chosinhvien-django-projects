# __author__ = 'Der Kaiser'

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from mysite.models import Category, Product, Anonymous


class ProductForm(ModelForm):
    class Meta:
        model = Product
        exclude = ('slug', 'time_post', 'status', 'id', 'user', )

class AnonymousForm(ModelForm):
    class Meta:
        model = Anonymous
        exclude = ('product', )


