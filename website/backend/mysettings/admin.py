from django.contrib import admin
from solo.admin import SingletonModelAdmin
from .models import MySetting

@admin.register(MySetting)
class MySettingsAdmin(SingletonModelAdmin):
    pass
