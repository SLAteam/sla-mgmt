from django.conf.urls import url
from sla_app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url('kpi/', views.kpi, name='kpi')
]

