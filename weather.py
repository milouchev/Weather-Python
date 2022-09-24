#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 07:31:36 2022

@author: milouchev
"""

import requests
import datetime as dt
API_KEY = "2beb050ea9f28be440952a50995248e3"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

print("Current weather data provided by OpenWeather.")
city = input("Enter a city name: ")

# Using F string to directly embed variables and expressions (query parameters) in string below
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)


if response.status_code == 200:
    now = dt.datetime.now()
    data = response.json()
    weather = data['weather'][0]['description']
    temp_c = round(data["main"]["temp"] - 273.15, 2)
    temp_f = round(data["main"]["temp"] * (9/5) - 459.67, 2)
    feel_c = round(data["main"]["feels_like"] - 273.15, 2)
    feel_f = round(data["main"]["feels_like"] * (9/5) - 459.67, 2)

    print("\nWeather conditions:", weather)
    print("Current temperature: " + str(temp_c) + "°C", "/", str(temp_f) + "°F")
    print("Feels like: " + str(feel_c) + "°C", "/", str(feel_f) + "°F\n")
    print(now)
else:
    print("\nAn error occurred - weather data for selected city not found.")