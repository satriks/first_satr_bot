import aiohttp
import requests
from environs import Env

env = Env()
env.read_env()

YA_WEATHER_TOKEN: str = env('YAWeather')
URL = 'https://api.weather.yandex.ru/v2/informers'

WATHER_NAME = {
    'clear' : 'ясно',
    'partly-cloudy' : 'малооблачно',
    'cloudy' : 'облачно с прояснениями',
    'overcast' : 'пасмурно',
    'drizzle' : 'морось',
    'light-rain' : 'небольшой дождь',
    'rain' : 'дождь',
    'moderate-rain' : 'умеренно сильный дождь',
    'heavy-rain' : 'сильный дождь',
    'continuous-heavy-rain' : 'длительный сильный дождь',
    'showers' : 'ливень',
    'wet-snow' : 'дождь со снегом',
    'light-snow' : 'небольшой снег',
    'snow' : 'снег',
    'snow-showers' : 'снегопад',
    'hail' : 'град',
    'thunderstorm' : 'гроза',
    'thunderstorm-with-rain' : 'дождь с грозой',
    'thunderstorm-with-hail' : 'гроза с градом',
}

MOON_CODE = {
    'moon-code-0' : 'полнолуние',
    'moon-code-1': 'убывающая луна',
    'moon-code-2' : 'убывающая луна',
    'moon-code-3' : 'убывающая луна',
    'moon-code-4' : 'последняя четверть',
    'moon-code-5': 'убывающая луна',
    'moon-code-6' : 'убывающая луна',
    'moon-code-7' : 'убывающая луна',
    'moon-code-8' : 'новолуние',
    'moon-code-9' : 'растущая луна',
    'moon-code-10' : 'растущая луна',
    'moon-code-11' : 'растущая луна',
    'moon-code-12' : 'первая четверть',
    'moon-code-13' : 'растущая луна',
    'moon-code-14' : 'растущая луна',
    'moon-code-15' : 'растущая луна',
}


# def get_weather():
#     haader = {'X-Yandex-API-Key':YA_WEATHER_TOKEN}
#     param = {'lat':55.664268,
#              'lon': 37.753020,
#              'lang': 'ru_RU',
#              }
#
#     response = requests.get(URL, params=param, headers=haader)
#
#     data = response.json()
#     response_icon = requests.get(f"https://yastatic.net/weather/i/icons/funky/dark/{data['forecast']['parts'][0]['icon']}.svg")
#
#     return (f"По данным Яндекс Погоды\n" \
#            f"Погода сейчас: {data['fact']['temp']} градуса. Ощущается как {data['fact']['feels_like']} градусов\n" \
#            f"*********************************************************\n" \
#            f"Сегодня ожидается {data['forecast']['parts'][0]['temp_avg']} градусов. "\
#            f"В целом сегодня {WATHER_NAME[data['forecast']['parts'][0]['condition']]}\nСкорость ветра {data['forecast']['parts'][0]['wind_speed']} м/с" \
#            f"  порывы до {data['forecast']['parts'][0]['wind_gust']}м/с\n" \
#            f"Луна  - {MOON_CODE[data['forecast']['moon_text']]}. Восход - {data['forecast']['sunrise']}. Закат - {data['forecast']['sunset']}", response_icon)

async def get_weather():

    haader = {'X-Yandex-API-Key':YA_WEATHER_TOKEN}
    param = {'lat':55.664268,
             'lon': 37.753020,
             'lang': 'ru_RU',
             }

    async with aiohttp.ClientSession(headers=haader) as session:
        async with session.get('https://api.weather.yandex.ru/v2/informers', params=param) as response:
            data = await response.json()

    return (f"По данным Яндекс Погоды\n" \
           f"Погода сейчас: {data['fact']['temp']} градуса. Ощущается как {data['fact']['feels_like']} градусов\n" \
           f"***********************************\n" \
           f"Сегодня ожидается {data['forecast']['parts'][0]['temp_avg']} градусов. "\
           f"В целом сегодня {WATHER_NAME[data['forecast']['parts'][0]['condition']]}\nСкорость ветра {data['forecast']['parts'][0]['wind_speed']} м/с" \
           f"  порывы до {data['forecast']['parts'][0]['wind_gust']}м/с\n" \
           f"Луна  - {MOON_CODE[data['forecast']['moon_text']]}. Восход - {data['forecast']['sunrise']}. Закат - {data['forecast']['sunset']}",)



if __name__ == '__main__':
    print(*get_weather())