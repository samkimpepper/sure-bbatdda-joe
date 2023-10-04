
from rest_framework import serializers
from .models import Alarm

class AlarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alarm 
        fields = ["id", "content", "link"]