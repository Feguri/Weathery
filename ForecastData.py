import requests


class ForecastData:
    def __init__(self, lat, lon):
        self.ApiKey = '1e9e9de5ee2fe2c660df35054541f17c'
        self.City = 'Montreal'
        self.cnt = 7

        self.request = requests.get(url=f'https://api.openweathermap.org/data/2.5/onecall'
                                        f'?lat={lat}&'
                                        f'lon={lon}&'
                                        f'appid={self.ApiKey}')
        self.request.raise_for_status()
        self.data = self.request.json()

        self.index = 0
        self.MaxTempListK = []
        self.MinTempListK = []
        for self.Day in self.data['daily']:
            self.MaxTempListK.append(self.data['daily'][self.index]['temp']['max'])
            self.MinTempListK.append(self.data['daily'][self.index]['temp']['min'])
            self.index += 1

        self.MaxTempListC = []
        for self.MaxItemK in self.MaxTempListK:
            self.ConvertedTemp = int(round(self.MaxItemK - 273.15, 0))
            self.MaxTempListC.append(self.ConvertedTemp)

        self.MinTempListC = []
        for self.MinItemK in self.MinTempListK:
            self.ConvertedTemp = int(round(self.MinItemK - 273.15, 0))
            self.MinTempListC.append(self.ConvertedTemp)

# ------------------------------------------ ALL THE TEMPS FOR THE WEEK -------------------------------------- #
        self.MaxZeroC = self.MaxTempListC[0]
        self.MaxOneC = self.MaxTempListC[1]
        self.MaxTwoC = self.MaxTempListC[2]
        self.MaxThreeC = self.MaxTempListC[3]
        self.MaxFourC = self.MaxTempListC[4]
        self.MaxFiveC = self.MaxTempListC[5]
        self.MaxSixC = self.MaxTempListC[6]
        self.MaxSevenC = self.MaxTempListC[7]

        self.MinZeroC = self.MinTempListC[0]
        self.MinOneC = self.MinTempListC[1]
        self.MinTwoC = self.MinTempListC[2]
        self.MinThreeC = self.MinTempListC[3]
        self.MinFourC = self.MinTempListC[4]
        self.MinFiveC = self.MinTempListC[5]
        self.MinSixC = self.MinTempListC[6]
        self.MinSevenC = self.MinTempListC[7]

        self.MaxZeroF = int(round((self.MaxTempListC[0] * (9 / 5)) + 32, 0))
        self.MaxOneF = int(round((self.MaxTempListC[1] * (9/5)) + 32, 0))
        self.MaxTwoF = int(round((self.MaxTempListC[2] * (9/5)) + 32, 0))
        self.MaxThreeF = int(round((self.MaxTempListC[3] * (9/5)) + 32, 0))
        self.MaxFourF = int(round((self.MaxTempListC[4] * (9/5)) + 32, 0))
        self.MaxFiveF = int(round((self.MaxTempListC[5] * (9/5)) + 32, 0))
        self.MaxSixF = int(round((self.MaxTempListC[6] * (9/5)) + 32, 0))
        self.MaxSevenF = int(round((self.MaxTempListC[7] * (9/5)) + 32, 0))

        self.MinZeroF = int(round((self.MinTempListC[0] * (9 / 5)) + 32, 0))
        self.MinOneF = int(round((self.MinTempListC[1] * (9/5)) + 32, 0))
        self.MinTwoF = int(round((self.MinTempListC[2] * (9/5)) + 32, 0))
        self.MinThreeF = int(round((self.MinTempListC[3] * (9/5)) + 32, 0))
        self.MinFourF = int(round((self.MinTempListC[4] * (9/5)) + 32, 0))
        self.MinFiveF = int(round((self.MinTempListC[5] * (9/5)) + 32, 0))
        self.MinSixF = int(round((self.MinTempListC[6] * (9/5)) + 32, 0))
        self.MinSevenF = int(round((self.MinTempListC[7] * (9/5)) + 32, 0))

        # A list of the weather conditions for the next 7 days
        self.ConditionsList = []

        self.Index = 0

        for self.Condition in self.data['daily']:
            self.CurrentCondition = self.data['daily'][self.Index]['weather'][0]['main']
            self.ConditionsList.append(self.CurrentCondition)

            self.Index += 1

# ------------------------------------------ CONDITIONS FOR THE WEEK -------------------------------------- #
        self.ConditionOne = self.ConditionsList[1]
        self.ConditionTwo = self.ConditionsList[2]
        self.ConditionThree = self.ConditionsList[3]
        self.ConditionFour = self.ConditionsList[4]
        self.ConditionFive = self.ConditionsList[5]
        self.ConditionSix = self.ConditionsList[6]
        self.ConditionSeven = self.ConditionsList[7]
