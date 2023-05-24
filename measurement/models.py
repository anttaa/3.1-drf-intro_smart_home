from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')

    class Meta:
        verbose_name = 'Сенсор'
        verbose_name_plural = 'Сенсоры'

    def __str__(self):
        return self.name


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', verbose_name='Учителя')
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время')

    class Meta:
        verbose_name = 'Показание'
        verbose_name_plural = 'Показания'
