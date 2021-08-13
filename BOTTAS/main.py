import random
import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("The bot is on ready for use!!!")

#Commands
@client.command()
async def hello(ctx):
    await ctx.send("Hello i am BOTTAS")


@client.command()
async def covid(ctx):
        await ctx.send("I hate covid!")


@client.event
async def on_member_join(member):
    channel = client.get_channel()
    await channel.send('Helloo!')


@client.event
async def on_member_remove(member):
    channel = client.get_channel()
    await channel.send('GoodBye')



client.run('')#TokenHere
