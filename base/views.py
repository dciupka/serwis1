from django.shortcuts import render, redirect
from .models import Geoinfo
from .forms import GeoinfoForm
import random


# Create your views here.
def index(request):
    if request.method != 'POST':
        form = GeoinfoForm()
    else:
        form = GeoinfoForm(data=request.POST)
    if form.is_valid():
        size = form.cleaned_data['list_size']
        for s in range(0, size):
            item = Geoinfo(list_size=size, _type='Position',
                           _id=random.randint(0, 65483214), key=None,
                           name="KUPA", iata_airport_code=None, type='location',
                           country='POLSskA', latitude=random.randint(0, 180),
                           longitude=random.randint(0, 180), location_id=random.randint(0, 756423),
                           inEurope=True, countryCode='PL', coreCountry=True, distance=None)
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
