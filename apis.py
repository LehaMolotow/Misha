import asyncio
import time
from datetime import datetime
from models.infos import InfoModel

class Settings(object):
    light_on = 0
    light_off = 0
    pump_on = 0
    pump_off = 0
    wind_on = 0
    wind_off = 0
    map = ("light_on",
           "light_off",
           "pump_on",
           "pump_off",
           "wind_on",
           "wind_off")

    def __init__(self, **kwargs):
        for key in self.map:
            setattr(self, key, 0)


    def set_items(self, **kwargs):
        for key, item in kwargs.items():
            if key in self.map:
                setattr(self, key, int(item))

    def get_items(self):
        for item in self.map:
            yield item, self.__getattribute__(item)


def light_on():
    print('light_on')

    return 0


def light_off():
    print('light_off')

    return 0


def pump_on():
    print('pump_on')

    return 0


def pump_off():
    print('pump_off')
    return 0


def wind_on():
    print('wind_on')
    return 0


def wind_off():
    print('wind_off')

    return 0


def get_state():
    print('get_state')


    answer = {'temp': 0, 'wet': 0}
    return answer


async def wraper():
    current_time = int(time.strftime('%y'))
    while True:
        # какой сейчас час
        if int(time.strftime('%y')) != current_time:
            current_time = int(time.strftime('%y'))
            try:
                commands = {}
                for command, value in settings.get_items():
                    commands[command] = value

                if settings.light_on != settings.light_off:
                    if settings.light_off == current_time:
                        light_off()
                    if settings.light_on == current_time:
                        light_on()

                if settings.wind_on != settings.wind_off:
                    if settings.wind_off == current_time:
                        wind_off()
                    if settings.wind_on == current_time:
                        wind_on()

                if settings.pump_off != settings.pump_on:
                    if settings.pump_on == current_time:
                        pump_on()
                    if settings.pump_off == current_time:
                        pump_off()

            except Exception as e:
                print(e)
                raise SystemExit

        to_db = InfoModel(**get_state())
        to_db.time = datetime.utcnow()
        to_db.save()

        await asyncio.sleep(10)

settings = Settings()
