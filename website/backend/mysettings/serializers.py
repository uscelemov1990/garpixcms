from rest_framework import serializers
from .models import MySetting


class MySettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = MySetting
        fields = '__all__'
