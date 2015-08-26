from django.conf.urls import patterns, url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    #url(r'^(?P<category>[a-zA-Z]+)/', views.cat, name='cat'),
    url(r'^category/(?P<category>[\w\s]+)/$', views.cat, name='category'),
]
