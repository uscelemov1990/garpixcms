from django.db import models
from garpix_utils.file import get_file_path
from solo.models import SingletonModel

class MySetting(SingletonModel):
    logo = models.ImageField(upload_to=get_file_path, verbose_name='Изображение')
    document = models.FileField()

    class Meta:
        verbose_name = 'Основная информация'


