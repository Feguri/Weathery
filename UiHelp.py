from WeatherData import WeatherData
from ForecastData import ForecastData

with open(file='City.csv', mode='r') as city_file:
    City = city_file.read()


f = open('City.csv', "w+")
f.close()

data = WeatherData(city=f'{City}')
forecast_data = ForecastData(lat=data.Lat, lon=data.Lon)


class Ui:
    def __init__(self):
        self.SunnyList = ['Sunny', 'Clear']
        self.CloudsList = ['Partly cloudy', 'Clouds']
        self.OvercastList = ['Cloudy', 'Overcast', 'Mist', 'Freezing fog', 'Fog']
        self.LightRainList = ['Light rain shower', 'Patchy rain possible', 'Patchy sleet possible',
                              'Patchy freezing drizzle possible',
                              'Patchy light drizzle', 'Light drizzle', 'Freezing drizzle', 'Heavy freezing drizzle',
                              'Patchy light rain', 'Light rain', 'Light freezing rain', 'Light sleet',
                              'Light rain shower', 'Light sleet showers']
        self.RainList = ['Rain', 'Moderate rain at times', 'Moderate rain', 'Heavy rain at times', 'Heavy rain',
                         'Moderate or heavy freezing rain', 'Moderate or heavy sleet', 'Torrential rain shower',
                         'Moderate or heavy sleet showers']
        self.SnowList = ['Snow', 'Patchy light snow', 'Light snow', 'Patchy moderate snow', 'Moderate snow',
                         'Patchy heavy snow',
                         'Heavy snow', 'Ice pellets', 'Light snow showers', 'Moderate or heavy snow showers',
                         'Light showers of ice pellets', 'Moderate or heavy showers of ice pellets', 'Blowing snow']
        self.ThunderList = ['Thunder', 'Thunder Storm', 'Thunderstorm', 'Storm', 'Patchy light rain with thunder',
                            'Moderate or heavy rain with thunder',
                            'Patchy light snow with thunder', 'Moderate or heavy snow with thunder',
                            'Thundery outbreaks possible']
        self.Sunny = '#80BFFF'
        self.SunnyNight = '#090d2b'
        self.Overcast = '#637d96'
        self.Clouds = '#7290b5'

        self.fg = 'black'
        self.background = self.Sunny

    def main_icon_number(self):
        if data.Condition in self.SunnyList:
            self.background = self.Sunny
            return 0
        elif data.Condition in self.CloudsList:
            self.background = self.Clouds
            return 1
        elif data.Condition in self.OvercastList:
            self.background = self.Overcast
            return 2
        elif data.Condition in self.LightRainList:
            self.background = self.Clouds
            return 10
        elif data.Condition in self.RainList:
            self.background = self.Overcast
            return 7
        elif data.Condition in self.SnowList:
            self.background = self.Clouds
            return 6
        elif data.Condition in self.ThunderList:
            self.background = self.Overcast
            return -1
        else:
            return 0

    def day_one_icon(self):
        if forecast_data.ConditionOne in self.SunnyList:
            return 1

        elif forecast_data.ConditionOne in self.CloudsList:
            return 2

        elif forecast_data.ConditionOne in self.OvercastList:
            return 7

        elif forecast_data.ConditionOne in self.LightRainList:
            return 8

        elif forecast_data.ConditionOne in self.RainList:
            return 10

        elif forecast_data.ConditionOne in self.SnowList:
            return 9

        elif forecast_data.ConditionOne in self.ThunderList:
            return 3

        else:
            return 1

    def day_two_icon(self):
        if forecast_data.ConditionTwo in self.SunnyList:
            return 1

        elif forecast_data.ConditionTwo in self.CloudsList:
            return 2

        elif forecast_data.ConditionTwo in self.OvercastList:
            return 7

        elif forecast_data.ConditionTwo in self.LightRainList:
            return 8

        elif forecast_data.ConditionTwo in self.RainList:
            return 10

        elif forecast_data.ConditionTwo in self.SnowList:
            return 9

        elif forecast_data.ConditionTwo in self.ThunderList:
            return 3

        else:
            return 1

    def day_three_icon(self):
        if forecast_data.ConditionThree in self.SunnyList:
            return 1

        elif forecast_data.ConditionThree in self.CloudsList:
            return 2

        elif forecast_data.ConditionThree in self.OvercastList:
            return 7

        elif forecast_data.ConditionThree in self.LightRainList:
            return 8

        elif forecast_data.ConditionThree in self.RainList:
            return 10

        elif forecast_data.ConditionThree in self.SnowList:
            return 9

        elif forecast_data.ConditionThree in self.ThunderList:
            return 3

        else:
            return 1

    def day_four_icon(self):
        if forecast_data.ConditionFour in self.SunnyList:
            return 1

        elif forecast_data.ConditionFour in self.CloudsList:
            return 2

        elif forecast_data.ConditionFour in self.OvercastList:
            return 7

        elif forecast_data.ConditionFour in self.LightRainList:
            return 8

        elif forecast_data.ConditionFour in self.RainList:
            return 10

        elif forecast_data.ConditionFour in self.SnowList:
            return 9

        elif forecast_data.ConditionFour in self.ThunderList:
            return 3

        else:
            return 1

    def day_five_icon(self):
        if forecast_data.ConditionFive in self.SunnyList:
            return 1

        elif forecast_data.ConditionFive in self.CloudsList:
            return 2

        elif forecast_data.ConditionFive in self.OvercastList:
            return 7

        elif forecast_data.ConditionFive in self.LightRainList:
            return 8

        elif forecast_data.ConditionFive in self.RainList:
            return 10

        elif forecast_data.ConditionFive in self.SnowList:
            return 9

        elif forecast_data.ConditionFive in self.ThunderList:
            return 3

        else:
            return 1

    def day_six_icon(self):
        if forecast_data.ConditionSix in self.SunnyList:
            return 1

        elif forecast_data.ConditionSix in self.CloudsList:
            return 2

        elif forecast_data.ConditionSix in self.OvercastList:
            return 7

        elif forecast_data.ConditionSix in self.LightRainList:
            return 8

        elif forecast_data.ConditionSix in self.RainList:
            return 10

        elif forecast_data.ConditionSix in self.SnowList:
            return 9

        elif forecast_data.ConditionSix in self.ThunderList:
            return 3

        else:
            return 1

    def day_seven_icon(self):
        if forecast_data.ConditionSeven in self.SunnyList:
            return 1

        elif forecast_data.ConditionSeven in self.CloudsList:
            return 2

        elif forecast_data.ConditionSeven in self.OvercastList:
            return 7

        elif forecast_data.ConditionSeven in self.LightRainList:
            return 8

        elif forecast_data.ConditionSeven in self.RainList:
            return 10

        elif forecast_data.ConditionSeven in self.SnowList:
            return 9

        elif forecast_data.ConditionSeven in self.ThunderList:
            return 3

        else:
            return 1

    def there_is_thunder(self):
        if data.Condition in self.ThunderList:
            return True
        else:
            return False


