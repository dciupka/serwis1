from django.shortcuts import render, redirect
from .models import Geoinfo
from .forms import GeoinfoForm
import random
from . import geo_geo
from .iata_code import find_iata_by_city_name
from .inEurope import check_In_Europe


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
            # 'geo_position': {'latitude': lon, 'longitude': lat}, #ale można boundingboxowe
     
            '''
            data = geo_geo.random_geo()
            print('wylosowano -dobre dane')
            display_name = data['display_name']
            name = display_name.split(sep=',')[0]
            country = data['address']['country']
            fullName = f'{name} {country}'
            countryCode = data['address']['country_code']
            if check_In_Europe(countryCode):
                inEurope=True
            else:
                inEurope=False

            try:
                iata_data=find_iata_by_city_name(name)
                if iata_data[0]['iata_code']:
                    iata_airport_code =True
            except:
                iata_airport_code=None
                print("brak skrótu IATA, lub koniec limitu na stroni api flightlab 100requestów/miesiac")
            item = Geoinfo(list_size=size, _type=data['osm_type'],
                           _id=data['osm_id'], key=None,
                           name=name, iata_airport_code=iata_airport_code, type='location',
                           country=data['address']['country'], latitude=data['lat'],
                           longitude=data['lon'], location_id=data['place_id'],
                           inEurope=inEurope, countryCode=countryCode, coreCountry=True, distance=None)
            print(data)
            item.save()
        return redirect('base:conf')
    context = {'form': form}
    return render(request, 'base/index.html', context)


def conf(request):
    return render(request, 'base/conf.html')

'''
dict_file = {'_type': 'Position',
             '_id': 65483214,
             'key': None,
             'name': 'Oksywska',
             'fullName': 'Oksywska, Poland',
             'iata_airport_code': None,
             'type': 'location',
             'country': 'Poland',
             'geo_position': {'latitude': 51.0855422, 'longitude': 16.9987442},
             'location_id': 756423,
             'inEurope': True,
             'countryCode': 'PL',
             'coreCountry': True,
             'distance': None}

'''