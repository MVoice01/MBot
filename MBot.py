import discord
import random
import asyncio
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s:˓→%(message)s'))
logger.addHandler(handler)
client = discord.Client()
print('booting up...')

@client.event
async def on_ready():
    print('logged in successfully')

@client.event
async def on_message(message):
    if message.content.startswith('ping'):
        await client.send_message(message.channel, "**Pong!** :ping_pong:")
    elif message.content.startswith('Hello'):
        await client.send_message(message.channel, random.choice( ['Hi!', 'Hello,how are you?', 'Hello there!'] ))

client.run('MzMyODQ1OTAxNDI2OTgyOTEy.DEZE4Q.hVwjzEr-W1mRYVJ98R8fHCyLt_s')
