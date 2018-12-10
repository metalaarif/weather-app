#!/usr/bin/python3
'''
Real time weather app, small project for myself.
Learning how awesome python3 can be!
'''
import requests

def main():
    city = input("type the city or country name to get weather: ")
    get_data_from_website(city)
    get_info_about_city()

def get_data_from_website(name):
    html_data = "https://www.weatherbug.com/weather-forecast/now/{}".format(name)
    html_response = requests.get(html_data).text
#    print(html_response)
    return html_response

def get_info_about_city():
    pass

if __name__ == "__main__":
    main()
