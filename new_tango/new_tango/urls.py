"""new_tango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from registration.backends.simple.views import RegistrationView
from django.contrib.auth.views import password_change_done
class MyRegistrationView(RegistrationView):
    def get_success_url(self,request, user):
        return '/rango/'

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
	url(r'^rango/', include('rango.urls')),
    url(r'^accounts/register/$', MyRegistrationView.as_view(), name='registration_register'),
    #url(r'^accounts/password/change/done/$', password_change_done, {'template_name': 'registration/password_change_done.html'}),
    #url(r'^accounts/password/change/done/$', auth_password_change_done, {'template_name': 'registration/logout.html'}),
    url(r'^accounts/', include('registration.backends.default.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
