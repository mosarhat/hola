"""
Really refer to the following as it explains the code pretty well:
https://github.com/Rapptz/discord.py/blob/master/discord/flags.py
"""
import discord 
from secret_sauce import *

# an intents object that is set to default using the default method 

intents = discord.Intents.default()

intents.message_content = True

# we'll set up a client, an instance of discord.Client
# represents the bot connection to Discord

client = discord.Client(intents=intents)
print(client.application)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run('your token here')