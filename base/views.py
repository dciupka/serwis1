from django.shortcuts import render, redirect
from .models import Geoinfo, GeoPosition
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
        #pobranie i usuniecie listy o tej samej nazwie np. list_size = 2
        all_data=Geoinfo.objects.all()
        for a in all_data:
            if a.list_size == size:
                Geoinfo.objects.filter(id=a.id).delete()
                print(f'Usunięto listę o rozmiarze {size} ')

        for s in range(0, size):
            data = geo_geo.random_geo()
            display_name = data['display_name']
            name = display_name.split(sep=',')[0]
            country = data['address']['country']
            countryCode = data['address']['country_code']
            if check_In_Europe(countryCode):
                inEurope=True
            else:
                inEurope=False

            #odnalezienie iata_code po nazwie miasta
            try:
                iata_data=find_iata_by_city_name(name)
                if iata_data[0]['iata_code']:
                    iata_airport_code =True
            except:
                iata_airport_code=None
                print("brak skrótu IATA, lub koniec limitu na stroni api flightlab 100requestów/miesiac")


            geo_position = GeoPosition(latitude=data['lat'], longitude=data['lon'])
            geo_position.save()         #zapis do bazy wylosowanych pozycji

            item = Geoinfo(list_size=size,
                           _type=data['osm_type'],
                           _id=data['osm_id'],
                           key=None,
                           name=name,
                           iata_airport_code=iata_airport_code,
                           type='location',
                           country=data['address']['country'],
                           geo_position=geo_position,
                           location_id=data['place_id'],
                           inEurope=inEurope,
                           countryCode=countryCode,
                           coreCountry=random.getrandbits(1),
                           distance=None)
            item.save()
        return redirect('base:conf')
    context = {'form': form}
    return render(request, 'base/index.html', context)


def conf(request):
    return render(request, 'base/conf.html')

