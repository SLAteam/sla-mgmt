#from django.conf.urls import url
from . import views
#from django.contrib.auth import views as auth_views
from django.urls import path

urlpatterns = [
 #   url(r'^$', views.home),
 #   url(r'^loggedin$', views.loggedin),
 #   url(r'^login/$', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
	path('', views.index, name='index'), 
]