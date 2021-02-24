import discord
from discord.ext import commands
import os
import praw
import random
import asyncio
reddit=praw.Reddit(client_id="zbhc-7ufGQ4ZTA",
                  client_secret="Cvm97EdyUFXFDYyYvyitAGsOdxP7HA",
                  username="KingshukK",
                  password="Protection2@",
                  user_agent="Meme")

client = commands.Bot(command_prefix="e!")
@client.event
async def on_ready():
    print("Ready")

@client.command()
async def meme(ctx):
    subreddit=reddit.subreddit("memes")
    all_subs=[]

    top=subreddit.top(limit=50)

    for submission in top:
        all_subs.append(submission)

    random_sub=random.choice(all_subs)

    name=random_sub.title
    url=random_sub.url

    em=discord.Embed(title=name)

    em.set_image(url=url)

    await ctx.send(embed=em)
    while True:
        await asyncio.sleep(600)	

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

client.run(ODE0MDE5NjQ1MzMzMDQ1Mjc5.YDXw3w.0pL9NxppIxGmRNo8kLpUae1d6fM)