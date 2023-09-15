import os

API_ID = int(os.environ.get("API_ID", "23572120"))
API_HASH = os.environ.get("API_HASH", "87e5640ca80bcad76ed7228d69dbbd7c")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6516995458:AAHpAvgTIg-mXSlVMhei-wtRbTwS0YcD2Jw")
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", "-1001772303732")
IS_PRIVATE = os.environ.get("IS_PRIVATE",False) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID"))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', 'PadhoBeBakiMaiDekhLunga')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
