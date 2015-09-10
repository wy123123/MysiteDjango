from django.conf.urls import patterns, url
from rango import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^about/', views.about, name='about'),
    #url(r'^(?P<category>[a-zA-Z]+)/', views.cat, name='cat'),
    url(r'^category/(?P<category>[\w\s]+)/$', views.cat, name='category'),
    url(r'^add_category/$', views.add_category, name='add_category'),
    url(r'^add_page/$', views.add_page, name='add_page'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),

]
