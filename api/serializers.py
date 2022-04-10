from rest_framework import serializers
from  base.models import  Geoinfo, GeoPosition

class GeoPositonSerializer(serializers.ModelSerializer):
    class Meta:
        model =GeoPosition
        fields= ['latitude', 'longitude']

class GeoinfoSerializer(serializers.ModelSerializer):
    geo_position =GeoPositonSerializer(read_only=True)
    class Meta:
        model = Geoinfo
        fullName = Geoinfo.fullName
        fields = ['_type',
                  '_id',
                  'key',
                  'name',
                  'fullName',
                  'iata_airport_code',
                  'type',
                  'country',
                  'geo_position',
                  'location_id',
                  'inEurope',
                  'countryCode',
                  'coreCountry',
                  'distance',
                  'geo_position'
                  ]




