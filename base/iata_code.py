import requests

def find_iata_by_city_name(city_name):
    '''city name must be in english, secred code for 100 request/permonth'''
    with open("C:/restproject/sc.txt") as file_object:
        lines = file_object.readlines()
    params = {
        'access_key': lines[1],
        'search':city_name,
    }
    api_result = requests.get('https://app.goflightlabs.com/cities?', params)
    api_response = api_result.json()
    print(api_response)
    return api_response

#Test for find_iata_by_city_name
'''
print(100*'--')
iata_data = {}
iata_data=find_iata_by_city_name('Warsaw')
iata_airport_code = iata_data[0]['iata_code']
print(iata_airport_code)
'''