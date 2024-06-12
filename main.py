# TOKEN = "MTI1MDQzMDExNzMxMDYyNzg1MQ.GKkdbe.XzDZui97qq8vpx8F3NLzMga6zrU-vYOq8qkzC0"
import os
import discord
from discord.utils import get
from discord import FFmpegPCMAudio
from youtube_dl import YoutubeDL
from discord.ext import commands
from discord import app_commands
from myserver import server_on


bot = commands.Bot(command_prefix='x!', intents=discord.Intents.all())

@bot.command
async def play(ctx, url):
    await ctx.channel.send('ctx = '+str(ctx.content)+'url = '+str(url))
    voice_channel = ctx.author.voice.channel
    voice_client = get(bot.voice_clients, guild=ctx.guild)

    
    if voice_client == None:
        ctx.channel.send('Joined')
        await voice_channel.connect()
        voice_client = get(bot.voice_clients, guild=ctx.guild)
    
    YDL_OPTION = {'format':'bastaudio','noplaylist':'True'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    if not voice_client.is_playing():
        with YoutubeDL(YDL_OPTION) as ydl:
            info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
        voice_client.play(FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))
        voice_client.is_playing()
    else :
        await ctx.channel.send('Already playing song')
        return
server_on()
bot.run(os.getenv(TOKEN))
