from telethon import TelegramClient, events
from telethon.tl.types import User
from langdetect import detect
from deep_translator import GoogleTranslator
import textwrap
import os
import requests
import json
import random
import aiohttp
import nextcord
from dotenv import load_dotenv

load_dotenv()

# Channel routing configuration
# Format: "telegram_channel_id": "discord_webhook_url"
CHANNEL_ROUTES = {
    "1556054753": "https://discord.com/api/webhooks/1405388660030967889/Hj_m-A7gZZ-pX82nFSkeXMqCMOPZG_4mn7JU6lmxRIf3bgi9wlp3XeCsmkPB9rpdYwri",  # Watcher Guru 1 -> Discord Channel 1
    "2504978188": "https://discord.com/api/webhooks/1405388451020537906/41ldIZBZ5uKgPT8TrnmswguPTCsIHJjET5ZZEDDirgQo3zy8-6qbfPqgHbT0ljtw56Ni",  # Bloss VIP 2 -> Discord Channel 2
    "2586124539": "https://discord.com/api/webhooks/1405388846639747207/QeWoQerIS-DLwgkM_NXc-acFa1s3HEyffgxpWYJI9SMdYlnHCsGNnFJKqBZERRUBhgMl",  # Cap VIP 3 -> Discord Channel 3
    "2204471065": "https://discord.com/api/webhooks/1405392442232012930/5mFyS6z6Cxfnkr4QWD3kIub7TA2S4nLdpvAe4fjZ93C5AVTTMkHY8nbC1ok86G6IRpks",  # New Channel -> Captain Hook
    "2241695394": "https://discord.com/api/webhooks/1405392706930212864/KqyNqkUPiZOxXsqMmZz9Pb2qsHUxbOlB30JcAS2W1nEOgPOlb73lvc_yGbPh2QJFFO5Q",  # New Channel -> Spidey Bot
    "2418841577": "https://discord.com/api/webhooks/1405392966968934440/aok9us2ORdm3umBj4SfSpi7e5GdeBfuIcbzVsct4eQMfnL3bfq1xKHNKK5Ef7Sup3vPz",  # New Channel -> Captain Hook
    "2616444563": "https://discord.com/api/webhooks/1405393068437405738/YC-pPZixq87xNVGrRvqTx-04MggP9l_lkF9SlFZQcTakFhfDkKIU7tJcSifjrcQ_XR3h",  # New Channel -> Captain Hook
    "1648271934": "https://discord.com/api/webhooks/1405388660030967889/Hj_m-A7gZZ-pX82nFSkeXMqCMOPZG_4mn7JU6lmxRIf3bgi9wlp3XeCsmkPB9rpdYwri",  # New Channel -> Spidey Bot
    "1651524056": "https://discord.com/api/webhooks/1405388660030967889/Hj_m-A7gZZ-pX82nFSkeXMqCMOPZG_4mn7JU6lmxRIf3bgi9wlp3XeCsmkPB9rpdYwri",  # New Channel -> Spidey Bot
    "1380328653": "https://discord.com/api/webhooks/1405388660030967889/Hj_m-A7gZZ-pX82nFSkeXMqCMOPZG_4mn7JU6lmxRIf3bgi9wlp3XeCsmkPB9rpdYwri",  # New Channel -> Spidey Bot
    "2312090328": "https://discord.com/api/webhooks/1405393748053069846/oRN7ZxPE1mhbGOV_gMEkJ6f_E_a0Wex3GicmF2651ZVPAamPXjIGp-dCXSVIS5qAOAOE",  # New Channel -> Spidey Bot
    "1557336382": "https://discord.com/api/webhooks/1405388660030967889/Hj_m-A7gZZ-pX82nFSkeXMqCMOPZG_4mn7JU6lmxRIf3bgi9wlp3XeCsmkPB9rpdYwri",  # New Channel -> Spidey Bot
    "1219306781": "https://discord.com/api/webhooks/1405388660030967889/Hj_m-A7gZZ-pX82nFSkeXMqCMOPZG_4mn7JU6lmxRIf3bgi9wlp3XeCsmkPB9rpdYwri",  # New Channel -> Spidey Bot
    "2380293749": "https://discord.com/api/webhooks/1405394759974916116/1VPHZ0p2jPUJj6rcO2FOH4fr9qqjC0i6WwRZR3WfJzLdsxBy_x1WraXJPbTjiTOzqINu",  # New Channel -> Captain Hook
}

# No fallback webhook - only send to configured channels
FALLBACK_WEBHOOK = None

appid = os.environ.get("APPID")
apihash = os.environ.get("APIHASH")
apiname = os.environ.get("APINAME")
dlloc = os.environ.get("DLLOC", "./temp/")
input_channels_entities = os.environ.get("INPUT_CHANNELS")
blacklist = os.environ.get("BLACKLIST")
translate = bool(os.environ.get("TRANSLATE"))

if blacklist == 'True':
    blacklist = True

if input_channels_entities is not None:
    input_channels_entities = list(map(int, input_channels_entities.split(',')))

# Create temp directory if it doesn't exist
os.makedirs(dlloc, exist_ok=True)

async def imgur(mediafile):
    url = "https://api.imgur.com/3/upload"

    payload = {
        'album': 'ALBUMID',
        'type': 'file',
        'disable_audio': '0'
    }

    files = [
        ('video', open(mediafile, 'rb'))
    ]

    headers = {
        'Authorization': str(random.randint(1, 10000000000))
    }

    response = requests.post(url, headers=headers, data=payload, files=files)
    return json.loads(response.text)

def get_webhook_for_channel(channel_id):
    """Get the appropriate webhook URL for a given channel ID"""
    channel_id_str = str(channel_id)
    webhook_url = CHANNEL_ROUTES.get(channel_id_str, FALLBACK_WEBHOOK)
    if channel_id_str in CHANNEL_ROUTES:
        print(f'Found route for channel {channel_id_str}')
    else:
        print(f'No route found for channel {channel_id_str}, using fallback')
    return webhook_url

def start():
    client = TelegramClient(apiname, appid, apihash)
    client.start()
    print('Started Multi-Channel Bot')
    print(f'Input channels: {input_channels_entities}')
    print(f'Blacklist: {blacklist}')
    print(f'Channel routes configured: {len(CHANNEL_ROUTES)}')

    @client.on(events.NewMessage(chats=input_channels_entities, blacklist_chats=blacklist))
    async def handler(event):
        if isinstance(event.chat, User):
            return  # Ignore messages from users or bots

        msg = event.message.message
        channel_id = event.chat.id
        webhook_url = get_webhook_for_channel(channel_id)
        
        # Skip if no webhook is configured for this channel
        if webhook_url is None:
            print(f'No webhook configured for channel {channel_id}, skipping...')
            return
            
        print(f'Channel ID: {channel_id} | Using webhook: {webhook_url[:50]}...')

        if translate:
            try:
                if msg != '' and detect(textwrap.wrap(msg, 2000)[0]) != 'en':
                    msg += '\n\n' + 'Translated:\n\n' + GoogleTranslator(source='auto', target='en').translate(msg)
            except:
                pass

        if event.message.sender.username is not None:
            username = event.message.sender.username
        else:
            username = event.chat.title

        if event.message.media is not None and event.message.file:
            dur = event.message.file.duration
            if dur is None:
                dur = 1

            if dur > 60 or event.message.file.size > 209715201:
                print('Media too long or too big!')
                msg += f"\n\nLink to Video: https://t.me/c/{event.chat.id}/{event.message.id}"
                await send_to_webhook(msg, username, webhook_url)
                return
            else:
                path = await event.message.download_media(dlloc)
                if event.message.file.size > 8388608:
                    await picimgur(path, msg, username, webhook_url)
                else:
                    await pic(path, msg, username, webhook_url)
                os.remove(path)
        else:
            await send_to_webhook(msg, username, webhook_url)

    client.run_until_disconnected()

async def picimgur(filem, message, username, webhook_url):
    async with aiohttp.ClientSession() as session:
        try:
            webhook = nextcord.Webhook.from_url(webhook_url, session=session)
            print('Sending w media Imgur')
            try:
                image = await imgur(filem)
                image = image['data']['link']
                print(f'Imgur: {image}')
                await webhook.send(content=image, username=username)
            except Exception as ee:
                print(f'Error {ee.args}')
            for line in textwrap.wrap(message, 2000, replace_whitespace=False):
                await webhook.send(content=line, username=username)
        except Exception as e:
            print(f'Error {e.args}')

async def pic(filem, message, username, webhook_url):
    async with aiohttp.ClientSession() as session:
        try:
            print('Sending w media')
            webhook = nextcord.Webhook.from_url(webhook_url, session=session)
            try:
                f = nextcord.File(filem)
                await webhook.send(file=f, username=username)
            except:
                print('Uploading to imgur')
                try:
                    image = await imgur(filem)
                    image = image['data']['link']
                    print(f'Imgur: {image}')
                    await webhook.send(content=image, username=username)
                except Exception as ee:
                    print(f'Error {ee.args}')
            for line in textwrap.wrap(message, 2000, replace_whitespace=False):
                await webhook.send(content=line, username=username)
        except Exception as e:
            print(f'Error {e.args}')

async def send_to_webhook(message, username, webhook_url):
    async with aiohttp.ClientSession() as session:
        print('Sending w/o media')
        webhook = nextcord.Webhook.from_url(webhook_url, session=session)
        for line in textwrap.wrap(message, 2000, replace_whitespace=False):
            await webhook.send(content=line, username=username)

if __name__ == "__main__":
    start()
