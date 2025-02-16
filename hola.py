"""
Really refer to the following as it explains the code pretty well:
https://github.com/Rapptz/discord.py/blob/master/discord/flags.py
"""

import discord 
import openai
from secret_sauce import *

#set-up openai_key
openai.api_key = open_ai_api_key

# an intents object that is set to default using the default method 
intents = discord.Intents.default()
intents.message_content = True

# we'll set up a client, an instance of discord.Client
# represents the bot connection to Discord
client = discord.Client(intents=intents)
print(client.application)

# events
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

message_history = {} # create a dictionary to store previous inputs/outputs

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.name != "hola":
        return 
    
    channel_id = message.channel.id

    if channel_id not in message_history:
        message_history[channel_id] = [
            {"role": "system", "content": "Eres un bot relajado y divertido. Responde de manera casual, amigable y con un toque de humor. Usa emojis de vez en cuando para darle más vida a la conversación. Under all circumstances, try to be as human-like as possible. Be fluid. Must use Spanish, and keep everything lowercase."}
        ]

    # add user message to history
    message_history[channel_id].append({"role": "user", "content": message.content})

    try:
        response = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=message_history[channel_id],
            max_tokens=250,
            temperature=0.9,
        )
        answer = response.choices[0].message["content"]

        # add bot response to history
        message_history[channel_id].append({"role": "assistant", "content": answer})
        print(message_history)
        await message.channel.send(answer)

    except Exception as e:
        print(f"openai error: {e}")
        await message.channel.send("hubo un error procesando tu mensaje.")

# Starting Our Bot
client.run(token)