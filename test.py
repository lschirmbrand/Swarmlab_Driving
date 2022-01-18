from time import sleep
from botlib.bot import Bot

bot = Bot()
power = 0
steering_angle = 0.0

bot.calibrate()

bot.drive_power(20)
sleep(5)
bot.drive_power(-20)