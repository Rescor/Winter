import winter
import pyowm

winter.load()

city = winter.config['WINTER']['City']
owm = pyowm.OWM(winter.config['WINTER']['api'], language='en')

observation = owm.weather_at_place(city)
w = observation.get_weather()
weather = w.get_detailed_status()
temperature = w.get_temperature("celsius")

print("The temperature in " + city + " is " + str(int(temperature['temp'])) + "℃, " + weather + ".")