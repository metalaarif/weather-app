#!/usr/bin/python3
'''
Real time weather app, small project for myself.
Learning how awesome python3 can be!
Used api from https://openweathermap.org
'''
import requests
import bs4
i = 0
while i == 0:
    city = input("Enter the City Name [london,uk] e[x]it: ")
    city = city.lower().strip()
    if city != "x":
        html = "http://api.openweathermap.org/data/2.5/weather?q={}&mode=html&appid=2de305846c0ca215654c20574174124d".format(
            city)
        response = requests.get(html)
        data = response.text

        soup = bs4.BeautifulSoup(data, "html.parser")

        location = soup.div.string
        temp = soup.find(title="Current Temperature").string

        print("The temperature of {} is {}".format(location, temp))
    elif city == "x":
        print("Thanks ba-bye")
        break