import requests

def get_weather(request):
    weather_data = requests.get(
        'https://api.weatherapi.com/v1/current.json?q=Fergana&key=3eead9e64e5248bcbf8112613241811'
    ).json()
    return {
        'weather':weather_data,
    }