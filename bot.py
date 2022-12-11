bot_url = "https://discord.com/api/oauth2/authorize?client_id=1051614245940375683&permissions=8&scope=bot"

import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
print("the token is", TOKEN)
client = discord.Client(intents=discord.Intents.default())

@client.event
async def on_message(message):
    prompt = str(message.content)

    # check for the string 
    #  [i]
    #  I like coffe
    #  [a]
    #  Great I like coffee too.


    # the prompt is one part
    # the response is another part of the same message
    channel = message.channel
    username = str(message.author).split("#")[0]
    # check that the message is not sent by the AI bot
    # check that the username is not the bot
    if username != "open-chat-gpt":
        print("the message is", message)
        print("the username is", username)
        print("the prompt is", prompt)
        # Save to the server 
        response = "hello world"
        await channel.send(f'We got a response from the bot: {response}')
               
client.run(TOKEN)