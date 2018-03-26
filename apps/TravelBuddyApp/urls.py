from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$',views.user_registration),
    url(r'^login$', views.login),
    url(r'^travels$', views.travels), 
    url(r'^travels/destination$', views.destination), 
    url(r'^travels/add$', views.add_travel),
    url(r'^add$', views.add),
  ]