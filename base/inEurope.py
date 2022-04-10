import json

def check_In_Europe(country_code):
    filename='./base/countryInEurope.json' # django need ./base/countryInEurpoe.json path
    #filename ='countryInEurope.json' #for testing
    with open(filename,mode='r') as f:
        in_europe_data = json.load(f)
        for k in in_europe_data:
            if country_code.upper() == k['code']:
                return True

#Test
'''
print(check_In_Europe('PL')) #true
print(check_In_Europe('POMSA')) #none
print(check_In_Europe('')) #none
'''
