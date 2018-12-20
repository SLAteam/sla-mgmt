from django.conf.urls import url
from django.urls import path
from sla_app import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('viewer/', views.get_kpi_by_user, name='get_kpi_by_user'),
    path('viewer/<str:oper_id>', views.get_kpi_by_oper, name='get_kpi_by_oper')
]

