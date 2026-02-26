import os
import platform
from tkinter import *
from WeatherData import WeatherData
from ForecastData import ForecastData
from AstronomyData import AstronomyData
import datetime as dt
from tkinter import simpledialog

# Determine operating system
IS_WINDOWS = platform.system().lower().startswith('win')
IS_MACOS = platform.system().lower() == 'darwin'
# (other platforms can be detected similarly)

# helper for building paths (os.path.join already handles separators correctly)
def make_path(*parts):
    return os.path.join(*parts)

print(f"Running on {platform.system()} (Windows? {IS_WINDOWS}, macOS? {IS_MACOS})")

import random


date = dt.datetime
today = date.now()
TodayWeekday = today.weekday()

WeekDays = ['', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

Tomorrow1 = 'Tomorrow'
Tomorrow2 = WeekDays[TodayWeekday + 3]
Tomorrow3 = WeekDays[TodayWeekday + 4]
Tomorrow4 = WeekDays[TodayWeekday + 5]
Tomorrow5 = WeekDays[TodayWeekday + 6]
Tomorrow6 = WeekDays[TodayWeekday + 7]
Tomorrow7 = WeekDays[TodayWeekday + 8]

SunnyNight = '#090d2b'

window = Tk()
window.geometry('1200x700')
window.title('Weathery 🌲')

City = simpledialog.askstring(title='Search a City', prompt='Enter Your City Name')

city_file_path = make_path('City.csv')
with open(file=city_file_path, mode='a') as city_file:
    city_file.write(f'{City}')

data = WeatherData(city=f'{City}')
astronomy_data = AstronomyData(city=f'{City}')
forecast_data = ForecastData(lat=data.Lat, lon=data.Lon)

from UiHelp import Ui
Ui = Ui()
Icon = PhotoImage(file=os.path.join('new_icons', f"output-onlinepngtools ({Ui.main_icon_number()}).png"))
Background = Ui.background

#  ---------------------------------------- Day 1 ----------------------------------------- #

ConditionOneIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_one_icon()}).png"))

#  ---------------------------------------- Day 2 ----------------------------------------- #

ConditionTwoIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_two_icon()}).png"))

#  ---------------------------------------- Day 3 ----------------------------------------- #

ConditionThreeIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_three_icon()}).png"))

#  ---------------------------------------- Day 4 ----------------------------------------- #

ConditionFourIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_four_icon()}).png"))

#  ---------------------------------------- Day 5 ----------------------------------------- #

ConditionFiveIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_five_icon()}).png"))

#  ---------------------------------------- Day 6 ----------------------------------------- #

ConditionSixIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_six_icon()}).png"))

#  ---------------------------------------- Day 7 ----------------------------------------- #
ConditionSevenIcon = PhotoImage(file=os.path.join('Small Icons', f"output-onlinepngtools ({Ui.day_seven_icon()}).png"))

Gota = PhotoImage(file=os.path.join('Small Icons', 'output-onlinepngtools (11).png'))

if data.IsDay == 0:
    Background = Ui.SunnyNight
    if data.Condition == 'Clear':
        Icon = PhotoImage(file=os.path.join('new_icons', 'output-onlinepngtools (9).png'))
    elif data.Condition == 'Partly cloudy' or data.Condition == 'Clouds':
        Icon = PhotoImage(file=os.path.join('new_icons', 'output-onlinepngtools (8).png'))
    fg = 'white'
    bg = f'{SunnyNight}'
else:
    fg = 'black'
# --------------------------------------- Uv Meter Device ------------------------------------------ #\

UvIndex = int(getattr(data, 'Uv', 0) + 6)
try:
    UvImage = PhotoImage(file=os.path.join('Uv', f'autodraw_4_17_2021__{UvIndex}_-removebg-preview.png'))
except EXCEPTION:
    UvImage = PhotoImage(file=os.path.join('Uv', 'autodraw_4_17_2021__18_-removebg-preview.png'))

# --------------------------------------- UI ------------------------------------------ #

font = 'Arial'

window.configure(bg=f'{Background}')

UvImageLabel = Label(master=window, bg=Background, image=UvImage)
Logo = PhotoImage(file=os.path.join('new_icons', 'output-onlinepngtools.png'))

TodayMax = Label(master=window, bg=Background, text=f'{forecast_data.MaxZeroC}°C', font=(f'{font}', 12, 'normal'),
                 fg=f'{fg}')
TodayMin = Label(master=window, bg=Background, text=f'{forecast_data.MinZeroC}°C', font=(f'{font}', 12, 'normal'),
                 fg=f'{fg}')


Sunrise = astronomy_data.sunrise
Sunset = astronomy_data.sunset

SunriseLabel = Label(master=window, bg=Background, text=f'Sunrise: {Sunrise}', font=(f'{font}', 14, 'normal'),
                     fg=f'{fg}')
SunsetLabel = Label(master=window, bg=Background, text=f'Sunset: {Sunset}', font=(f'{font}', 14, 'normal'), fg=f'{fg}')

IconImage = Label(master=window, bg=Background, image=Icon)
Location = Label(master=window, bg=Background, text=f"{data.City}, {getattr(data,'Region','')}, {data.Country}",
                 font=(f'{font}', 20, 'italic'), fg=f'{fg}')

CurrentTemperature = Label(master=window, bg=Background, text=f'{data.TempC}°C',
                           font=(f'{font}', 40, 'normal'), fg=f'{fg}')

if Ui.there_is_thunder():
    CurrentCondition = Label(master=window, bg=Background, text='Thunder',
                             font=(f'{font}', 18, 'normal'), fg=f'{fg}')
else:
    CurrentCondition = Label(master=window, bg=Background, text=f'{data.Condition}',
                             font=(f'{font}', 18, 'normal'), fg=f'{fg}')

FeelsLike = Label(master=window, bg=Background, text=f'Feels Like: {data.FeelsLikeC}°C',
                  font=(f'{font}', 15, 'normal'), fg=f'{fg}')
Humidity = Label(master=window, bg=Background, text=f'{data.Humidity}%',
                 font=(f'{font}', 16, 'normal'), fg=f'{fg}')
Weathery = Label(master=window, bg=Background, text=f'Weathery',
                 font=(f'Courier', 50, 'italic'), fg=f'{fg}')
LogoImage = Label(master=window, bg=Background, image=Logo)
MadeBy = Label(master=window, bg=Background, text='Made By Felipe Serrou\n      with Python\'s Tkinter',
               font=(f'Courier', 8, 'italic'), fg=f'{fg}')

GotaImage = Label(master=window, bg=Background, image=Gota)

# Labels for Weather Forecast Icons
DayOne = Label(master=window, bg=Background, image=f'{ConditionOneIcon}')
DayTwo = Label(master=window, bg=Background, image=f'{ConditionTwoIcon}')
DayThree = Label(master=window, bg=Background, image=f'{ConditionThreeIcon}')
DayFour = Label(master=window, bg=Background, image=f'{ConditionFourIcon}')
DayFive = Label(master=window, bg=Background, image=f'{ConditionFiveIcon}')
DaySix = Label(master=window, bg=Background, image=f'{ConditionSixIcon}')
DaySeven = Label(master=window, bg=Background, image=f'{ConditionSevenIcon}')

# Labels for Weekday
TomorrowDay1 = Label(master=window, bg=Background, text=f'{Tomorrow1}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')
TomorrowDay2 = Label(master=window, bg=Background, text=f'{Tomorrow2}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')
TomorrowDay3 = Label(master=window, bg=Background, text=f'{Tomorrow3}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')
TomorrowDay4 = Label(master=window, bg=Background, text=f'{Tomorrow4}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')
TomorrowDay5 = Label(master=window, bg=Background, text=f'{Tomorrow5}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')
TomorrowDay6 = Label(master=window, bg=Background, text=f'{Tomorrow6}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')
TomorrowDay7 = Label(master=window, bg=Background, text=f'{Tomorrow7}',
                     font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Max1 = Label(master=window, bg=Background, text=f'{forecast_data.MaxOneC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min1 = Label(master=window, bg=Background, text=f'{forecast_data.MinOneC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

Max2 = Label(master=window, bg=Background, text=f'{forecast_data.MaxTwoC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min2 = Label(master=window, bg=Background, text=f'{forecast_data.MinTwoC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

Max3 = Label(master=window, bg=Background, text=f'{forecast_data.MaxThreeC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min3 = Label(master=window, bg=Background, text=f'{forecast_data.MinThreeC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

Max4 = Label(master=window, bg=Background, text=f'{forecast_data.MaxFourC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min4 = Label(master=window, bg=Background, text=f'{forecast_data.MinFourC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

Max5 = Label(master=window, bg=Background, text=f'{forecast_data.MaxFiveC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min5 = Label(master=window, bg=Background, text=f'{forecast_data.MinFiveC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

Max6 = Label(master=window, bg=Background, text=f'{forecast_data.MaxSixC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min6 = Label(master=window, bg=Background, text=f'{forecast_data.MinSixC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

Max7 = Label(master=window, bg=Background, text=f'{forecast_data.MaxSevenC}°C',
             font=(f'{font}', 15, 'normal'), fg=f'{fg}')

Min7 = Label(master=window, bg=Background, text=f'{forecast_data.MinSevenC}°C',
             font=(f'{font}', 9, 'normal'), fg=f'{fg}')

current_playback = None

normal_list = [0, 1, 2, 6, 11, 12, 13]
rain_list = [10, 7]
thunder = 14

music = ['spongebob-production-music-hawaiian-happiness.mp3', 'reverie.mp3', 'plantasia.mp3', 'all-star.mp3']


def play():
    global current_playback
    print(f'Audio feature not available on this system')


def stop():
    global current_playback
    if current_playback:
        current_playback.stop()


MusicButton = Button(master=window, bg=Background,  text='♫',
                     font=(f'{font}', 20, 'bold'), fg=f'{fg}', command=play)
StopButton = Button(master=window, bg=Background,  text='X',
                    font=(f'{font}', 6, 'bold'), fg=f'{fg}', command=stop)


def change_temp_f():
    CurrentTemperature.configure(text=f'{data.TempF}°F')
    FeelsLike.configure(text=f'Feels Like: {data.FeelsLikeF}°F')

    Min1.configure(text=f'{forecast_data.MinOneF}°F')
    Max1.configure(text=f'{forecast_data.MaxOneF}°F')

    Min2.configure(text=f'{forecast_data.MinTwoF}°F')
    Max2.configure(text=f'{forecast_data.MaxTwoF}°F')

    Min3.configure(text=f'{forecast_data.MinThreeF}°F')
    Max3.configure(text=f'{forecast_data.MaxThreeF}°F')

    Min4.configure(text=f'{forecast_data.MinFourF}°F')
    Max4.configure(text=f'{forecast_data.MaxFourF}°F')

    Min5.configure(text=f'{forecast_data.MinFiveF}°F')
    Max5.configure(text=f'{forecast_data.MaxFiveF}°F')

    Min6.configure(text=f'{forecast_data.MinSixF}°F')
    Max6.configure(text=f'{forecast_data.MaxSixF}°F')

    Min7.configure(text=f'{forecast_data.MinSevenF}°F')
    Max7.configure(text=f'{forecast_data.MaxSevenF}°F')

    TodayMax.configure(text=f'{forecast_data.MaxZeroF}°F')
    TodayMin.configure(text=f'{forecast_data.MinZeroF}°F')


def change_temp_c():
    CurrentTemperature.configure(text=f'{data.TempC}°C')
    FeelsLike.configure(text=f'Feels Like: {data.FeelsLikeC}°C')

    Min1.configure(text=f'{forecast_data.MinOneC}°C')
    Max1.configure(text=f'{forecast_data.MaxOneC}°C')

    Min2.configure(text=f'{forecast_data.MinTwoC}°C')
    Max2.configure(text=f'{forecast_data.MaxTwoC}°C')

    Min3.configure(text=f'{forecast_data.MinThreeC}°C')
    Max3.configure(text=f'{forecast_data.MaxThreeC}°C')

    Min4.configure(text=f'{forecast_data.MinFourC}°C')
    Max4.configure(text=f'{forecast_data.MaxFourC}°C')

    Min5.configure(text=f'{forecast_data.MinFiveC}°C')
    Max5.configure(text=f'{forecast_data.MaxFiveC}°C')

    Min6.configure(text=f'{forecast_data.MinSixC}°C')
    Max6.configure(text=f'{forecast_data.MaxSixC}°C')

    Min7.configure(text=f'{forecast_data.MinSevenC}°C')
    Max7.configure(text=f'{forecast_data.MaxSevenC}°C')

    TodayMax.configure(text=f'{forecast_data.MaxZeroC}°C')
    TodayMin.configure(text=f'{forecast_data.MinZeroC}°C')


ChangeButtonC = Button(text='°C', command=change_temp_c)
ChangeButtonF = Button(text='°F', command=change_temp_f)

# ---------------------------------------- RENDERING ---------------------------------------- #

IconImage.place(x=100, y=80)
Location.place(x=130, y=15)
CurrentTemperature.place(x=360, y=110)
CurrentCondition.place(x=130, y=220)
FeelsLike.place(x=360, y=200)
Humidity.place(x=410, y=245)
TodayMax.place(x=500, y=120)
TodayMin.place(x=500, y=145)

Weathery.place(x=120, y=565)
LogoImage.place(x=485, y=480)
MadeBy.place(x=190, y=635)

ChangeButtonC.place(x=30, y=20)
ChangeButtonF.place(x=70, y=20)

UvImageLabel.place(x=125, y=220)
GotaImage.place(x=365, y=240)

# Forecast Rendering
DayOne.place(x=980, y=40)
TomorrowDay1.place(x=760, y=40)
Max1.place(x=880, y=40)
Min1.place(x=900, y=65)

DayTwo.place(x=980, y=130)
TomorrowDay2.place(x=760, y=130)
Max2.place(x=880, y=130)
Min2.place(x=900, y=155)

DayThree.place(x=980, y=220)
TomorrowDay3.place(x=760, y=220)
Max3.place(x=880, y=220)
Min3.place(x=900, y=245)

DayFour.place(x=980, y=310)
TomorrowDay4.place(x=760, y=310)
Max4.place(x=880, y=310)
Min4.place(x=900, y=335)

DayFive.place(x=980, y=400)
TomorrowDay5.place(x=760, y=400)
Max5.place(x=880, y=400)
Min5.place(x=900, y=425)

DaySix.place(x=980, y=490)
TomorrowDay6.place(x=760, y=490)
Max6.place(x=880, y=490)
Min6.place(x=900, y=515)

DaySeven.place(x=980, y=580)
TomorrowDay7.place(x=760, y=580)
Max7.place(x=880, y=580)
Min7.place(x=900, y=605)

SunriseLabel.place(x=360, y=300)
SunsetLabel.place(x=360, y=330)

MusicButton.place(x=35, y=80)
StopButton.place(x=16, y=80)

window.mainloop()

# TODO: sunrise & sunset times
