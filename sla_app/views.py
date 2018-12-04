from django.shortcuts import render
from django.http import HttpResponse
import datetime
from sla_app.models import KeyPerformanceIndicator # czy jakos tak to sie nazywa
# Create your views here.

def index (request):
    return HttpResponse("<h1>WYKRES KPI!</h1>")

def get_all_kpi(request):
    data = KeyPerformanceIndicator.objects.all() # inne metody to np .filter(name = <wyciagniete_z_request_id>), albo mozesz tez .filter(id = kpi_id)
                                                # jak robisz .get, to musisz obslugiwac wyjatek DoesNotExists, a .filter() zwraca pusta liste jak nic nie ma
    return HttpResponse(data)
