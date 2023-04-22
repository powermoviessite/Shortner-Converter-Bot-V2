# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "17193413"))
API_HASH = os.environ.get("API_HASH", "5e50e6380252d9d487093bae4171bf91")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5958464071:AAEYQHOmyZnxQ0ksNjpT1La0GDJoh_mDNzw")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1606667548")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "powermovies")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://powermovies:powermovies11@cluster0.je3b1k7.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1606667548")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001649801629")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "@PowerMoviesBots") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://te.legra.ph/file/a8241af47262bd4f67523.jpg') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
