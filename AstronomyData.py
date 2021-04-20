import requests


class AstronomyData:
    def __init__(self, city):
        self.ApiKey = 'f5314c6a881e48e8b70153604211104'
        self.AstronomyEnd = '/astronomy.json'
        self.AstronomyEndpoint = f'http://api.weatherapi.com/v1{self.AstronomyEnd}'

        self.params = {
            'key': f'{self.ApiKey}',
            'q': f'{city}'
        }

        self.request = requests.get(url=self.AstronomyEndpoint, params=self.params)
        self.request.raise_for_status()
        self.data = self.request.json()

        self.sunrise = self.data['astronomy']['astro']['sunrise']
        self.sunset = self.data['astronomy']['astro']['sunset']


data = AstronomyData(city='montreal')
