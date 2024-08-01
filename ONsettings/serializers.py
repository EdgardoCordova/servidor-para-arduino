from rest_framework import serializers
from .models import crc_ON

class crcONSerializer(serializers.ModelSerializer):
    class Meta:
        model = crc_ON
        fields = ('circuit_id', 'hour', 'minute', 'status1', 'status2', 'status3', 'status4', 'status5', 'status6' )


