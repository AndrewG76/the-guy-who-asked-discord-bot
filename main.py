import discord
import os

client = discord.Client()

theOriginalMeme = ["who asked"]
theTwistedOne = ["i asked"]


@client.event  #these 'events' are to listen for stuff that happens
async def on_ready(
):  #this is for when the bot successfully logs on the first time
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):  #this triggers when a message shows that ISNT the bot itself
    if message.author == client.user:
        return  #essentially do nothing

    msg = message.content

    if msg.startswith('?help'):
        await message.channel.send("say 'who asked' in your message")

    if any(word in msg.lower() for word in theOriginalMeme):
        await message.channel.send("i did")

    if any(word in msg.lower() for word in theTwistedOne):
        await message.channel.send("you too? :flushed:")


client.run(os.getenv('TOKEN'))
