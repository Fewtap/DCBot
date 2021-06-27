import discord
import os
#from dotenv import load_dotenv

#insert token here
TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


#Listens for messages
@client.event
async def on_message(message):
    

    



client.run(TOKEN)
