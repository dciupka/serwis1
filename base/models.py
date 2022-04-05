from django.db import models

class Geoinfo(models.Model):
    list_size = models.IntegerField()
    _type= models.CharField(max_length=200)
    _id = models.IntegerField()
    key= models.BooleanField(null=True)
    name= models.CharField(max_length=200)
    iata_airport_code=models.BooleanField(null=True)
    type= models.CharField(max_length=200)
    country= models.CharField(max_length=200)
    latitude = models.FloatField()
    longitude= models.FloatField()
    location_id=models.IntegerField(null=True)
    inEurope= models.BooleanField()
    countryCode=models.CharField(max_length=10)
    coreCountry=models.BooleanField()
    distance=models.BooleanField(null=True)

    def __str__(self):
        return self.name


