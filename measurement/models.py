from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
        ordering = ['id', ]

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements')
    temperature = models.DecimalField(max_digits=3, decimal_places=1)
    image = models.ImageField(null=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Измерение'
        verbose_name_plural = 'Измерения'
        ordering = ['sensor', ]

    def __str__(self):
        return f'{self.sensor}: {self.temperature}, {self.created}'
