from rest_framework import serializers
from .models import ApiModel

class CoreSerializers(serializers.ModelSerializer):
    class Meta():
        model = ApiModel
        fields = ['nomer']
