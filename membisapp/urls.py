from django.conf.urls import patterns, url
from .views import *

urlpatterns = patterns(
     #url(r'^profile/$', views.UserProfileView.as_view(), name='profile'),
    #url(r'^profile/save/userinfo/$', views.UserChangeUserInfoView.as_view(), name='change_user_data'),
    #url(r'^profile/save/password/$', views.UserChangePasswordView.as_view(), name='change_user_password'),

    #url(r'^bestellingen/$', views.OrdersListView.as_view(), name='orders'),
    #url(r'^bestellingen/new/$', views.order_new, name='order_new'),
    #url(r'^relaties/$', views.relationships, name='relationships'),
    #url(r'^aankopen/$', views.purchases, name='purchases'),
    #url(r'^aankopen/new/$', views.purchase_new, name='purchase_new'),
    url(r'^products/$', ProductListView , name='products'),
    url(r'^products/image/*/', product_image, name='product_image'),
    url(r'^products/new/$', product_new, name='product_new'),
    url(r'^products/edit/(?P<pk>\d+)/$', product_edit, name='product_edit'),
    url(r'^dashboard', home, name='dashboard'),
    #url(r'^accounts/login/$', LoginRequired, name='login'),
    #url(r'^sync/$', sync_api, name='sync_api'),
    #url(r'^callback/$', views.sync_api_callback, name='callback'),
    url(r'^$', home, name='dashboard'),
)