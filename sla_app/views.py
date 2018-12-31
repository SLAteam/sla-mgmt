from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from sla_app.models import KeyPerformanceIndicator, Operator, AggregationType
from django.http import HttpResponse

def get_kpi_by_name(kpi_name):
    return KeyPerformanceIndicator.objects.get(name=kpi_name)


def get_kpi_by_id(self,kpi_id):
    return KeyPerformanceIndicator.objects.get(id=kpi_id)

#poniższa funkcja generowała wykres na potrzeby sprintu 3
def get_kpi_by_country(self,kpi_country):
	data = KeyPerformanceIndicator.objects.filter(country=kpi_country)
	kpi_list = []
	kpi_list = data
	country = data[0].country
	context = { 'country' : country, 'kpi_list' : kpi_list }

	return render_to_response('viewer.html', context)

def get_kpi_by_oper(request, oper_id):
	if request.user.is_authenticated:
		data = KeyPerformanceIndicator.objects.filter(operator=oper_id)
	name_list = data.values('name').distinct
	kpi_list = []
	kpi_list = data
	context = { 'country' : data[0].country, 'operator' : data[0].operator, 'kpi_list' : kpi_list, 'name_list' : name_list }

	return render_to_response('viewer.html', context)

def get_kpi_by_user(request):
	oper = get_operator_for_user_id(request.user.id)
	data = KeyPerformanceIndicator.objects.filter(operator=oper.id)
	kpi_list = []
	context = { 'country' : data[0].country, 'operator' : oper.id, 'kpi_list' : data, 'name_list' : data.values('name').distinct }

	return render_to_response('viewer.html', context)

def get_operator_for_user_id(user_id):
    u = User.objects.get(id = user_id)

    return Operator.objects.get(user = u)


def get_all_kpis_for_user(user_id):
    oper = get_operator_for_user_id(user_id)

    return KeyPerformanceIndicator.objects.filter(operator = oper)


def get_aggr_type_by_type(aggr_type):
    return AggregationType.objects.get(kpi_type=aggr_type)


def get_aggr_type_by_id(aggr_type_id):
    return AggregationType.objects.get(id=aggr_type_id)


def get_operator_by_name(oper_name):
    return Operator.objects.get(name = oper_name)


def get_operator_by_id(oper_id):
    return Operator.objects.get(id = oper_id)


#def index(request):
#    return render_to_response('index.html', context)
def index(request):
    return render_to_response('index.html')

def kpi(request):
    kpi_list = []
    if request.user.is_authenticated:
        kpi_list = get_all_kpis_for_user(request.user.id)

    context = { 'kpi_list' : kpi_list }

    return render_to_response('kpi.html', context)
