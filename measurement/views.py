
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework.response import Response

from measurement.models import Sensor, Measurement
from measurement.serializers import SensorSerializer, MeasurementsSerializer, SimpleSensorSerializer


class SensorsListCreate(ListCreateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SimpleSensorSerializer


class SensorsRetrieveUpdate(RetrieveUpdateAPIView):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer


class MeasurementCreate(CreateAPIView):
    queryset = Measurement.objects.all()
    serializer_class = MeasurementsSerializer

    def perform_create(self, serializer):
        serializer.save()
