# manga-request-bot
A module for reuqesting mangas

## Info
This bot is used to fetch the requests from telegram and will send it to google sheets, from where it is easier to analyse the requests.

## Telegram Channel
[MangaDigestion](https://t.me/MangaDigestion)

## Commands
```
/start - Start the Bot
/help - Usage info
/mrequest - Request Mangas by manga name
/crequest - Request Mangas by manga url and channel id
```

### /start - command
```
/start command is used to start a bot.
```

### /help - command
```
/help command is used to get details of the bot commands and how to use them.
```

### /mrequest - command
```
/mrequest command is used to request manga by it's name, can be used with multiple manga name splited with comma ','

example:
/mrequest Grand Blue
/mrequest Grand Blue, Soul Land
```

### /crequest - command
```
/crequest command is used to request mangaURL and channelID, there are some bots that are automated which will need URL of the manga, and Channel ID from where the automated bot will post the manga chapters.
__Channel ID can be extracted from the url of web version of telegram.__

example:
/crequest https://mangafreak.online/manga/martial-peak/ -10088377449
```

## Env Variables

`API_ID` - Get the value from [my.telegram.org](https://my.telegram.org/apps) here.

`API_HASH` - Get the value from [my.telegram.org](https://my.telegram.org/apps) here.

`BOT_TOKEN` - Make a bot from [@BotFather](https://t.me/BotFather) and enter token here.

`GSPREAD_JSON` - A link of google sheets API JSON file hosted in the cloud, Configure it in https://console.cloud.google.com. For more help [watch this video.](https://www.youtube.com/watch?v=bu5wXjz2KvU)

## Deploy
You can deploy your own project on [Heroku](https://www.heroku.com/)

## Help
We are always here to help, visit our Telegram Group [MangaDigestionCommunity](https://t.me/MangaDigestionCommunity) to ask any questions.
