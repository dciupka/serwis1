from rest_framework import serializers
from  base.models import  Geoinfo

class GeoinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Geoinfo
        fields = '__all__'