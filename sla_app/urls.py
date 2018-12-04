from django.conf.urls import include, url
#from django.urls import patterns
from . import views

urlpatterns = [
   # url(r'^$',  views.index, name='index')]
    #url(r'^$',  views.all_kpi, name='all_kpi')]
   url(r'^$',  views.get_all_kpi, name='get_all_kpi')]
