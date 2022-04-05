import urllib.request
import json
import ssl

serviceurl = 'https://nominatim.openstreetmap.org/reverse?lat=<value>&lon=<value>&<params>'

#ignorj bledy certyikatem ssl
ctx = ssl.create_default_context()
ctx.check_hostname=False
ctx.verify_mode = ssl.CERT_NONE

params = dict(format='geojson')
lon = 56.0
lat = 56.0


url = f'https://nominatim.openstreetmap.org/reverse?lat={lat}&lon={lon}&{params}'

print('Pobieranie', url)
uh =urllib.request.urlopen(url,context=ctx)
data = uh.read().decode()
print('Pobrano', len(data))