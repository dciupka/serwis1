import urllib.request
import json
import ssl
import random
import argparse


serviceurl = 'https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&format=json'

#ignorj bledy certyikatem ssl
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE


lon = round(random.uniform(14.07, 24.09), 6)
lat = round(random.uniform(49, 54.50), 6)


url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&format=json&namedetails=1'

print('Pobieranie', url)
uh =urllib.request.urlopen(url,context=ctx)
data = uh.read().decode()
print(f'latitude: {lat}, lon {lon}')
print('Pobrano', len(data))

try:
    js = json.loads(data)
except:
    js= None
    print('Bład pobierania')

print(json.dumps(js, indent=4))


