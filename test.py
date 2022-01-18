from time import sleep
from botlib.bot import Bot

bot = Bot()
power = 0
steering_angle = 0.0

bot._steer_motor.calibrate()
bot._forklift.set_custom_height(1)
bot.drive_power(100)
sleep(5)
bot.drive_power(-100)
sleep(5)
