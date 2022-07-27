import discord
import os

client = discord.Client()

@client.event  #these 'events' are to listen for stuff that happens
async def on_ready():  #this is for when the bot successfully logs on the first time
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):  #this triggers when a message shows that ISNT the bot itself
    if message.author == client.user:
        return  #essentially do nothing

    msg = message.content

    if msg.startswith('?help'):
        await message.channel.send("say 'who asked' in your message")

    if "who" in msg and "asked" in msg: #checks to see if who AND asked are in the same string message
        await message.channel.send("i did")

client.run(os.getenv('TOKEN'))
