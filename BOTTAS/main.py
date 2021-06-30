import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

client = commands.Bot(command_prefix = "!", intents=intents)

@client.event
async def on_ready():
    print("The bot is on ready for use!!!")
    print("..............................")


@client.command()
async def hello(ctx):
    await ctx.send("Hello i am BOTTAS")


@client.command()
async def fkn(ctx):
    await ctx.send("Vai toma no cú clyde")

    
@client.event
async def on_member_join(member):
    channel = client.get_channel(859557683144425506)
    await channel.send('Eae Gatinha')


@client.event
async def on_member_remove(member):
    channel = client.get_channel(859557683144425506)
    await channel.send('Davi não deixa mais eu te chamar de gatinha então tchau só')

client.run('ODU5NTU1NjQ0MTUxNTYyMjg3.YNuZkw.3qGadTqf4NreZZg-xUkiaVebcm4')
