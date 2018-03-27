from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^registration$',views.user_registration),
    url(r'^login$', views.login),
    url(r'^travels$', views.travels), 
    url(r'^travels/destination/(?P<id>\d+)$', views.destination), 
    url(r'^travels/add$', views.add_travel),
    url(r'^add$', views.add),
    url(r'^logout$', views.logout),
    url(r'^join/(?P<id>\d+)$', views.join),
  ]