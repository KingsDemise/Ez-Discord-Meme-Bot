import discord
from discord.ext import commands
import os
import praw
import random
import asyncio
reddit=praw.Reddit(client_id="u kno it",
                  client_secret="u kno it too",
                  username="your reddit username",
                  password="your pass",
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

client.run("token here")
