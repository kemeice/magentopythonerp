from django.shortcuts import render
import requests
from requests_oauthlib import OAuth1
from requests_oauthlib import OAuth1Session
from django.shortcuts import redirect
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, UpdateView
from django.views.generic.base import TemplateView
#from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin
from .forms import ResetPasswordForm, NewProductForm, NewProductImageForm
from.models import *

# Create your views here.
class LoginRequired(LoginRequiredMixin):
    redirect_field_name = "login"
    template_name = "login.html"
    raise_exception = False


    @property
    def get_login_url(self):
        return self.render_to_response({})


@login_required
def home(request):
    new_orders = None
    return render(
        request,
        'dashboard.html',
        {'new_orders': new_orders}
    )


class UserProfileView(LoginRequired, TemplateView):
    template_name = "profile.html"

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        user = self.request.user

        #context['user_profile_form'] = UserProfileForm(instance=user)
        context['change_password_form'] = ResetPasswordForm()
        return context


class UserChangePasswordView(LoginRequired, FormView):
    form_class = ResetPasswordForm
    template_name = "profile.html"

    def get_success_url(self):
        return reverse('profile')

    def form_valid(self, form):
        '''
        Change user password if form is valid.
        '''

        current_user = self.request.user
        current_user.set_password(form.cleaned_data['password1'])
        current_user.save()
        return super(UserChangePasswordView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(UserChangePasswordView, self).get_context_data(**kwargs)

        context['change_password_form'] = context['form']

        user = self.request.user

        #context['user_profile_form'] = UserProfileForm(instance=user)
        return context


class UserChangeUserInfoView(LoginRequired, UpdateView):
    #form_class = UserProfileForm
    template_name = "profile.html"

    def get_object(self):
        return self.request.user

    def get_success_url(self):
        return reverse('profile')

    def get_context_data(self, **kwargs):
        context = super(UserChangeUserInfoView, self).get_context_data(**kwargs)

        context['user_profile_form'] = context['form']
        context['change_password_form'] = ResetPasswordForm()
        return context




@login_required
#   new_orders = Order.objects.all()
    #return render(request,
                  #'orders.html',
                 # {'orders': new_orders}
                  #)


class OrdersListView(LoginRequired, ListView):
    paginate_by = 10
    #model = Order
    template_name = "orders.html"


class ProductListView(LoginRequired, ListView):
    paginate_by = 10
    model = Product
    template_name = "products.html"


@login_required
def order_new(request):
    return render(request, 'order_new.html')


@login_required
def relationships(request):
    return render(request, 'relationships.html')


@login_required
def purchases(request):
    return render(request, 'purchase.html')


@login_required
def purchase_new(request):
    return render(request, 'purchase_new.html')


@login_required
def product_new(request):
    context = {}
    if request.method == 'POST':
        form = NewProductForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('dashboard', pk=product.id)
        else:
            context['form'] = form
    else:
        context['form'] = NewProductForm()
    return render(request, 'product_form.html', context=context)

@login_required
def product_image(request):
    context = {}
    if request.method == 'POST':
        form = NewProductImageForm(request.POST)
        if form.is_valid():
            product = form.save()
            return redirect('home')
        else:
            context['form'] = form
    else:
        context['form'] = NewProductImageForm()
    return render(request, 'product_image.html', context=context)


@login_required
def product_edit(request, pk):
    return render(request, 'product_edit.html')