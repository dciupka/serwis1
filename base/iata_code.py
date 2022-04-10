import requests

def find_iata_by_city_name(city_name):
    '''city name must be in english, secred code for 100 request/permonth'''
    params = {
        'access_key': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI0IiwianRpIjoiMDJkNjMxNjFiMWI4NDMyNmNjYjJjZDIxNGRlY2Q5NTBiOTcxMGNjN2I0YzA5MzgzZTI2NWU4ZDZhYzcxYjAzMGFjY2UyODFlOTg0OGMxZGUiLCJpYXQiOjE2NDk0NDQwODAsIm5iZiI6MTY0OTQ0NDA4MCwiZXhwIjoxNjgwOTgwMDgwLCJzdWIiOiIyMzc0Iiwic2NvcGVzIjpbXX0.Ji0KJDC0CiQY4CEb6lN_bRkiqrf2cT-VtQdaMGhAgHio8L5sR3XdGRYrLGMTE65CAhvsvGWtnB_zcK9WkDI9kg',
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