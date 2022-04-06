import argparse
import json
from typing import Dict
import requests
import random
from pprint import pprint


NOMINATIM_API_URL = "https://nominatim.openstreetmap.org"
NOMINATIM_REVERSE_ENDPOINT = f"{NOMINATIM_API_URL}/reverse"

query_params = {
    "addressdetails":1,

}


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("command", type=str, choices=["reverse"])
    return parser.parse_args()


def fetch_osm_reverse(lat: float, lon: float, zoom: int, params: Dict[str, int]) -> dict:
    params_query = "&".join(f"{param_name}={param_value}" for param_name, param_value in params.items())
    request_url = f"{NOMINATIM_REVERSE_ENDPOINT}?lat={lat}&lon={lon}&zoom={zoom}&{params_query}&format=json"
    print(request_url)

    response = requests.get(request_url)
    response.raise_for_status()
    return response.json()


def random_geo():
    """random data from geojson"""
    lon = round(random.uniform(14.07, 24.09), 6)
    lat = round(random.uniform(49, 54.50), 6)
    data = fetch_osm_reverse(lat=lat, lon=lon, zoom=10, params=query_params)
    #pprint(data)
    #print('+++++++++++++++++++++++++++++++++++++++++++++++++++++++')
    return data
