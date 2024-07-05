#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
import re
from os import environ
import os

id_pattern = re.compile(r'^.\d+$')


API_ID = int(os.environ.get("API_ID", "22353942"))
API_HASH = os.environ.get("API_HASH", "a71c2aa4f6b764734411512973e34763")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7350355274:AAENQcdyg3-lqcAWDopEdRVEvcUWqhnu7QE")
ADMIN = int(os.environ.get("ADMIN", '6643388068')) 
FSUB_UPDATES = os.environ.get("FSUB_CHANNEL", "")
FSUB_GROUP = os.environ.get("FSUB_GROUP", "")
CAPTION = os.environ.get("CAPTION", "")
#ALL FILES UPLOADED - CREDITS 🌟 - @Sunrises_24
DOWNLOAD_LOCATION = "./DOWNLOADS"
group = environ.get('GROUP', '-1002107484984')
GROUP = int(group) if group and id_pattern.search(group) else None
SUNRISES_PIC= "https://graph.org/file/12e81862346199c521ae8.jpg"  # Replace with your Telegraph link
AUTH_USERS = int(os.environ.get("AUTH_USERS", '6643388068'))



