from urllib import response
import gspread
from datetime import date
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

# Getting .json key | Get the Google Spread Key from https://console.cloud.google.com
response = requests.get(os.getenv('GSPREAD_JSON'))
data = response.json()
try:
    os.mkdir('gspread')
except:
    pass

with open('gspread/tg-manga-bot-request.json', 'w') as f:
    json.dump(data, f)

print("JSON file downloaded!")


ss = gspread.service_account('gspread/tg-manga-bot-request.json')
sh = ss.open('tg-manga-bot-requests')
wks1 = sh.worksheet('Sheet1')
wks2 = sh.worksheet('Sheet2')

class requestmangaapi:
    def add_manganame_sheet1(manga_name, name, username):
        manga_name_list = manga_name.split(",")
        for manga_name in manga_name_list:
            today = date.today()
            date1 = today.strftime("%B %d, %Y")
            str_list = list(filter(None, wks1.col_values(1)))
            next_row = str(len(str_list)+1)
            wks1.update(f'A{next_row}', manga_name)
            wks1.update(f'B{next_row}', date1)
            wks1.update(f'C{next_row}', name)
            wks1.update(f'D{next_row}', username)

    def add_request_info_sheet2(manga_url, channel_id, name, username):
        today = date.today()
        date1 = today.strftime("%B %d, %Y")
        str_list = list(filter(None, wks2.col_values(1)))
        next_row = str(len(str_list)+1)
        wks2.update(f'A{next_row}', manga_url)
        wks2.update(f'B{next_row}', channel_id)
        wks2.update(f'C{next_row}', date1)
        wks2.update(f'D{next_row}', name)
        wks2.update(f'E{next_row}', username)