from config import bot
from utils.starter import starter
from utils.request import request

try:
    starter()
    request()
except Exception as e:
    print(e)

bot.run()