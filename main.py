import discord
import os
import json
from discord.ext import commands
from ping_your_mother import ping_your_mother
from discord.utils import get
from discord import Intents

intents = discord.Intents().all()
#####client = discord.Bot(intents=intents)

#bot = commands.Bot(command_prefix='', description="Test Bot for discord.py")
#client = commands.Bot(command_prefix='.')

client = discord.Client()

#change...2 trying to update the commit...

# Message for every log:
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


# Simple response to verify conectivity:
@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('Hello'):
        await message.channel.send('Hi sweetie')


#Third tutorial, here we go!

#@client.command()
#async def reactrole(ctx, emoji, role: discord.Role,*,message):

#  emb = discord.Embed(description=message)
#  msg = await ctx.channel.send(embed=emb)
#  await msg.add_reaction(emoji)

#with open('reactrole.json') as json_file:
#  data = json.load(json_file)

#  new_react_role = {
#    'role_name':role.name,
#    'role_id':role.id,
#    'emoji':emoji,
#    'message_id':msg.id
#  }

#  data.append(new_react_role)

# with open('reactrole.json,''w') as j:
#   json.dump(data,j, indent=4)


# Second tutorial... Fail :(
@client.event
async def on_raw_reaction_add(payload):
    ourMessageID = 879432093170536478

    if ourMessageID == payload.message_id:
        member = payload.member
        guild = member.guild

        emoji = payload.emoji.name
        if emoji == 'Rust':
            role = discord.utils.get(guild.roles, name="Rust")
        elif emoji == 'Python':
            role = discord.utils.get(guild.roles, name="Python")
        elif emoji == 'Java':
            role = discord.utils.get(guild.roles, name="Java")
        elif emoji == 'GoLang':
            role = discord.utils.get(guild.roles, name="GoLang")
        elif emoji == 'C_':
            role = discord.utils.get(guild.roles, name="C++")
        await member.add_roles(role)


@client.event
async def on_raw_reaction_remove(payload):
    ourMessageID = 879432093170536478

    if ourMessageID == payload.message_id:
        guild = client.get_guild(payload.guild_id)
        emoji = payload.emoji.name

        if emoji == 'Rust':
            role = discord.utils.get(guild.roles, name="Rust")
        elif emoji == 'Python':
            role = discord.utils.get(guild.roles, name="Python")
        elif emoji == 'Java':
            role = discord.utils.get(guild.roles, name="Java")
        elif emoji == 'GoLang':
            role = discord.utils.get(guild.roles, name="GoLang")
        elif emoji == 'C_':
            role = discord.utils.get(guild.roles, name="C++")
        member = await (guild.fetch_member(payload.user_id))
        if member is not None:
            await member.remove_roles(role)
        else:
            print("Member not found")


ping_your_mother()
client.run(os.getenv('TOKEN'))
