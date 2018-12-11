from django.shortcuts import render, get_object_or_404
from models import KeyPerformanceIndicator, Operator, AggregationType


def get_kpi_by_name(kpi_name):
    return KeyPerformanceIndicator.objects.get(name=kpi_name)


def get_kpi_by_id(kpi_id):
    return KeyPerformanceIndicator.objects.get(id=kpi_id)


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
