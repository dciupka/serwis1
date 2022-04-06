from django.shortcuts import render, redirect
from .models import Geoinfo
from .forms import GeoinfoForm
import random
from .geo_geo import random_geo

# Create your views here.
def index(request):
    if request.method != 'POST':
        form = GeoinfoForm()
    else:
        form = GeoinfoForm(data=request.POST)
    if form.is_valid():
        size = form.cleaned_data['list_size']
        data={}
        for s in range(0, size):
            '''
            _type = data['osm_type']
            _id = data['osm_id']
            # key:null
            display_name = data['display_name']
            name = display_name.split()[0]
            iata_airport_code = None
            type = 'location',
            country = data['address']['country']
            # 'geo_position': {'latitude': lon, 'longitude': lat}, #ale można boundingboxowe
            location_id = data['place_id']
            #inEurope= True
            countryCode = data['address']['country_code']
            # 'coreCountry': True,
            # 'distance': None
            fullName = f'{name} {country}'
            '''
            data = random_geo()
            display_name = data['display_name']
            name = display_name.split()[0]
            item = Geoinfo(list_size=size, _type=data['osm_type'],
                           _id=random.randint(0, 65483214), key=None,
                           name=name, iata_airport_code=None, type='location',
                           country='POLSskA', latitude=random.randint(0, 180),
                           longitude=random.randint(0, 180), location_id=random.randint(0, 756423),
                           inEurope=True, countryCode=data['address']['country_code'], coreCountry=True, distance=None)
            item.save()
        return redirect('base:conf')
    context = {'form': form}
    return render(request, 'base/index.html', context)


def conf(request):
    return render(request, 'base/conf.html')


'''
       Geoinfo.objects.create()
            new = form.save(commit=False)
            new._type = 'Position'
            new._id = random.randint(0, 10000)
            new.key = None
            new.name = "STERKÓW"
            new.iata_airport_code = None
            new.type = "fifaFArafa"
            new.country = "Poland"
            new.latitude = 59.0
            new.longitude = 49.0
            new.location_id = random.randint(0, 10000)
            new.inEurope = True
            new.countryCode = "PL"
            new.coreCountry = False
            new.distance = None
            new.save()
            print(s)
'''
