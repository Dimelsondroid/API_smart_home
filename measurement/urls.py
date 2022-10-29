from django.urls import path

from measurement.views import SensorsListCreate, SensorsRetrieveUpdate, MeasurementCreate

urlpatterns = [
    path('sensors/', SensorsListCreate.as_view()),
    path('measurements/', MeasurementCreate.as_view()),
    path('sensors/<pk>/', SensorsRetrieveUpdate.as_view())
]
