try:
    import requests
except ModuleNotFoundError:
    import subprocess
    subprocess.call('pip install requests')
    subprocess.call('pip install pygame')
    print('\n\nNecessary Modules installed. Restart Program')


class WeatherData:

    def __init__(self, city):
        self.ApiKey = 'f5314c6a881e48e8b70153604211104'
        self.CurrentWeatherEndpoint = '/current.json'
        self.CurrentEndpoint = f'http://api.weatherapi.com/v1{self.CurrentWeatherEndpoint}'

        self.params = {
            'key': f'{self.ApiKey}', 'q': f'{city}'
        }

        self.request = requests.get(url=self.CurrentEndpoint, params=self.params)
        self.request.raise_for_status()
        self.data = self.request.json()

        self.City = self.data['location']['name']
        self.Region = self.data['location']['region']
        self.Country = self.data['location']['country']

        self.TempC = int(round(self.data['current']['temp_c'], 0))
        self.TempF = int(round(self.data['current']['temp_f'], 0))
        self.IsDay = self.data['current']['is_day']
        if self.IsDay == 0:
            self.Current = 'Night'
        elif self.IsDay == 1:
            self.Current = 'Day'
        self.Condition = self.data['current']['condition']['text']
        self.Humidity = self.data['current']['humidity']
        self.FeelsLikeC = int(round(self.data['current']['feelslike_c'], 0))
        self.FeelsLikeF = int(round(self.data['current']['feelslike_f'], 0))
        self.Uv = self.data['current']['uv']
        self.Lat = self.data['location']['lat']
        self.Lon = self.data['location']['lon']
