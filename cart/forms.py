from django.shortcuts import render, redirect,get_object_or_404
from django import forms
from django.db import models
from shop.models import Product


PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1,30)]

class CartAddProductForm(forms.Form):
	quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
	update = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)



