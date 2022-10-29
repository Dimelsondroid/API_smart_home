from django.contrib import admin

from measurement.models import Measurement, Sensor


class MeasurmentInline(admin.TabularInline):
    model = Measurement
    extra = 1


@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description']
    inlines = [MeasurmentInline, ]


@admin.register(Measurement)
class MeasurementAdmin(admin.ModelAdmin):
    list_display = ['id', 'sensor', 'temperature', 'created', 'modified', 'image']
