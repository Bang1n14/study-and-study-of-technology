"""Based from https://www.youtube.com/watch?v=fa1FUW1jLAE&t=53s """


import requests
import datetime
from config import tg_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tg_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Скажи в каком городе ты хочешь узнать какая сейчас погода ')


@dp.message_handler()
async def get_weather(message: types.Message):
    code_to_emoji = {
        'Clear': 'Ясно \U00002600',
        'Clouds': 'Облачно \U00002601',
        'Rain': 'Дождь \U0001F327',
        'Drizzle': 'Дождь \U0001F327',
        'Thundershtorm': 'Гроза \U0001F329',
        'Snow': 'Снег \U0001F328',
        'Mist': 'Туман \U0001F32B'
    }
    try:
        r = requests.get(
            f'https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric'
        )
        data = r.json()

        city = data['name']
        current_temp = data['main']['temp']

        weather_emoji = data['weather'][0]['main']
        if weather_emoji in code_to_emoji:
            we = code_to_emoji[weather_emoji]
        else:
            we = 'Нету смайлика'

        humidity = data['main']['humidity']
        pressure = data['main']['pressure'] * 0.750063755419211
        sunrise_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunrise'])
        sunset_timestamp = datetime.datetime.fromtimestamp(data['sys']['sunset'])
        length_of_day = sunset_timestamp - sunrise_timestamp

        await message.reply(f'Погода в городе: {city}\nТемпература:{current_temp}°С {we}\n'
                            f'Влажность: {humidity}%\nДавление: {int(pressure)}мм.рт.столба\n'
                            f'Восход солнца: {sunrise_timestamp}\nЗакат солнца : {sunset_timestamp}\n'
                            f'Длина дня {length_of_day}')

    except Exception as ex:
        await message.reply('\U0001F31AПроверьте написание города\U0001F31A')


if __name__ == '__main__':
    executor.start_polling(dp)
