from config import open_weather_token
from pprint import pprint
import requests
import datetime


def get_weather(city, open_weather_token):

    code_to_emoji ={
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U00001F327'
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric'
        )
        data = r.json()
        #  pprint(data)

        city = data['name']
        current_temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp
        print(f'Погода в городе: {city}\nТемпература:{current_temp}°С\n' 
              f'Влажность:{humidity}\nДавление: {pressure}мм.рт.столба\n'
              f'Восход солнца: {sunrise_timestamp} Закат солнца : {sunset_timestamp}\n'
              f'Длинна дня {length_of_day}')
    except Exception as ex:
        print(ex)
        print('Wrong name place')




def main():
    city = input('Enter your place\n')
    get_weather(city, open_weather_token)


if __name__ == '__main__':
    main()
