from rest_framework import serializers

from measurement.models import Sensor, Measurement


class MeasurementsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Measurement
        fields = ['id', 'sensor', 'temperature', 'image']
        ordering = ['id', ]


class SensorSerializer(serializers.ModelSerializer):
    measurements = MeasurementsSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']
        ordering = ['id', ]


class SimpleSensorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']
        ordering = ['id', ]
