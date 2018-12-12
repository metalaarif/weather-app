#!/usr/bin/python3
'''
Real time weather app, small project for myself.
Learning how awesome python3 can be!
Used api from https://openweathermap.org
'''
import requests
import bs4

def main():
    city = input("Enter City name with Country Code(optional) [london,uk]: ")
    html = get_data_from_openweather_api(city)
    data = get_weather_of_city(html)
    print("The temperature of {} is {}".format(data[0], data[1]))

def get_data_from_openweather_api(name):
    html_data = "http://api.openweathermap.org/data/2.5/weather?q={}&mode=html&appid=2de305846c0ca215654c20574174124d".format(name)
    html_response = requests.get(html_data)

    return html_response.text

def get_weather_of_city(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    location = soup.div.string
    temp = soup.find(title="Current Temperature").string

    return location, temp

if __name__ == "__main__":
    main()