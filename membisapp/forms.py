from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext, ugettext_lazy as _
from django.conf import settings
from .models import *




class membisUserChangeForm(UserChangeForm):
    def __init__(self, *args, **kargs):
        super(membisUserChangeForm, self).__init__(*args, **kargs)
        del self.fields['username']

    class Meta:
       fields = '__all__'


class ResetPasswordForm(forms.Form):
    password1 = forms.CharField(label="Nieuw Paswoord", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Nieuw Paswoord Opnieuw", widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super(ResetPasswordForm, self).clean()
        pwd1 = cleaned_data.get("password1")
        pwd2 = cleaned_data.get("password2")

        if pwd1 != pwd2:
            raise forms.ValidationError("Passwords do not match!")


class NewProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('type_product', 'category','weight','stock','delivery', 'supplier','supplier_sku','order_per_X',        'supplier_delivery_time','advantage_1',  'advantage_2', 'advantage_3', 'name','groups', 'price', 'shortdescription', 'description', 'sale_price','membis_be_Nederlands','membis_be_France','membis_nl_Nederlads','Horeca','Color','width','lenght', 'size')

class NewProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        fields = ('product','image', 'thumbnail')