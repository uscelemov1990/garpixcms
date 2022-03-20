from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=60, verbose_name='Тег')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
