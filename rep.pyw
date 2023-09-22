# This example requires the 'message_content' intent.
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@bot.event
async def on_message(message):
    if message.author.id == bot.user.id:
        return

    if "hi" in message.content:
        await message.channel.send("Chào bạn")  
    
    if "admin" in message.content:
        await message.channel.send("Hiện tại admin đang bận, bạn vui longf liên hệ với ngài KING để được tư vấn")



client.run('MTE0NDU5Nzk0NDk3NzMzMDE3Ng.G-Gaxf.yoYmk6grUWNL3W_xqQuUafIw83_ExahfudBu6E')

