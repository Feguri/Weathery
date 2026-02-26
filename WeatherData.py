import requests


class WeatherData:

    def __init__(self, city):
        self.ApiKey = '1e9e9de5ee2fe2c660df35054541f17c'

        self.CurrentEndpoint = "https://api.openweathermap.org/data/2.5/weather"

        self.params = {
            'q': city,
            'appid': self.ApiKey,
            'units': 'metric'
        }

        self.request = requests.get(self.CurrentEndpoint, params=self.params)
        self.request.raise_for_status()
        self.data = self.request.json()

        # Location
        self.City = self.data.get('name', '')
        # openweathermap doesn't expose a region field; attempt state if available
        self.Region = self.data.get('sys', {}).get('state', '')
        self.Country = self.data.get('sys', {}).get('country', '')

        # Temperature
        self.TempC = int(round(self.data['main']['temp']))
        self.FeelsLikeC = int(round(self.data['main']['feels_like']))

        # Convert to Fahrenheit manually
        self.TempF = int(round((self.TempC * 9/5) + 32))
        self.FeelsLikeF = int(round((self.FeelsLikeC * 9/5) + 32))

        # Weather
        # use 'main' field for broad conditions like Clear, Clouds, Rain, etc.
        self.Condition = self.data['weather'][0]['main']
        self.Humidity = self.data['main']['humidity']

        # Day / Night
        icon = self.data['weather'][0]['icon']
        self.Current = "Night" if icon.endswith('n') else "Day"
        # also provide integer flag for legacy code
        self.IsDay = 0 if icon.endswith('n') else 1

        # Coordinates
        self.Lat = self.data['coord']['lat']
        self.Lon = self.data['coord']['lon']

        # UV index - OpenWeather has a separate endpoint. may be restricted
        try:
            uv_resp = requests.get(
                'https://api.openweathermap.org/data/2.5/uvi',
                params={'lat': self.Lat, 'lon': self.Lon, 'appid': self.ApiKey}
            )
            uv_resp.raise_for_status()
            self.Uv = uv_resp.json().get('value', 0)
        except Exception:
            # if anything fails (401, network etc.), default to 0
            self.Uv = 0
