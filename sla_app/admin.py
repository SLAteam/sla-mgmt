from django.contrib import admin
from .models import *

class OperatorAdmin(admin.ModelAdmin):
    search_fields = ['id','name']
    list_display = ['id','name']


class AggregationTypeAdmin(admin.ModelAdmin):
    search_fields = ['id','kpi_type']
    list_display = ['id','kpi_type']


class KeyPerformanceIndicatorAdmin(admin.ModelAdmin):
    search_fields = ['id','name','aggregation_type','operator','country']
    list_display = ['id','name','aggregation_type','operator','created_at']
    list_filter = ['aggregation_type','operator']

    def get_queryset(self, request):
        if request.user.is_superuser:
            return KeyPerformanceIndicator.objects.all()
        return KeyPerformanceIndicator.objects.filter(operator__user=request.user)

# Register your models here.
admin.site.register(Operator, OperatorAdmin)
admin.site.register(AggregationType, AggregationTypeAdmin)
admin.site.register(KeyPerformanceIndicator, KeyPerformanceIndicatorAdmin)
