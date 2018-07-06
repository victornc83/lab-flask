import sys
import json
import urllib
import urllib2
import config

def get_weather(query):
    api_url = config.EXTERNAL_API_URL['weather'] + '/weather?q={}&units=metric&appid=' + config.WEATHER_API_KEY
    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {
            "description": parsed["weather"][0]["description"], "temperature": parsed["main"]["temp"],
            "city": parsed["name"]
        }
    return weather