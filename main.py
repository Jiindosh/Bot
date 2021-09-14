from os import environ

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='*')
token = environ.get('TOKEN')


@client.event
async def on_ready():
    print('Jinbot en Ligne.')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="mon code"))

@client.command()
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="**Bannissement**", description="Ce membre a été banni du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.red())
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/796861724366995457.gif")
    embed.add_field(name="Membre banni : ", value=user.name, inline=False)
    embed.add_field(name="ID : ", value=user.id, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="Bot développé par ꒻꒐ꋊ꒯ꄲꇙꁝ_#2960 ")
    await ctx.send(embed=embed)

@client.command()
async def unban(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.unban(user, reason=reason)
    embed = discord.Embed(title="**Débannissement**", description="Ce membre a été débanni du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.orange())
    embed.set_thumbnail(url="https://media.giphy.com/media/r8iF8ZVnq2bQN5hwVt/giphy.gif")
    embed.add_field(name="Membre débanni : ", value=user.name, inline=False)
    embed.add_field(name="ID : ", value=user.id, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="Bot développé par ꒻꒐ꋊ꒯ꄲꇙꁝ_#2960 ")
    await ctx.send(embed=embed)


@client.command()
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="**Expulsion**", description="Ce membre a été expulsé du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.orange())
    embed.set_thumbnail(url="https://media.tenor.com/images/27f16871c55a3376fa4bfdd76ac2ab5c/tenor.gif")
    embed.add_field(name="Membre expulsé : ", value=user.name, inline=False)
    embed.add_field(name="ID : ", value=user.id, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="Bot développé par ꒻꒐ꋊ꒯ꄲꇙꁝ_#2960 ")
    await ctx.send(embed=embed)


@client.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_messages in messages:
        await each_messages.delete()

@client.command(name='ui')
async def userinfo(ctx, member: discord.Member = None):
    if not member:  # if member is no mentioned
        member = ctx.message.author  # set member as the author
    embed = discord.Embed(title=f"**Informations à propos de {member}**", colour=discord.Color.gold())
    embed.set_thumbnail(url="https://media.giphy.com/media/0GsNMsRwDKKMjiwIe5/giphy.gif")
    embed.add_field(name="Nom de l'utilisateur : ", value=member.name, inline=True)
    embed.add_field(name="ID de l'utilisateur : ", value=member.id, inline=True)
    embed.add_field(name="Compte crée le ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
    embed.add_field(name="A rejoint le serveur le ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
    embed.add_field(name="Rôle le plus haut", value=member.top_role.mention, inline=True)
    embed.set_footer(text="Bot développé par ꒻꒐ꋊ꒯ꄲꇙꁝ_#2960 ")
    await ctx.send(embed=embed)

@client.command(name="aide")
async def info(ctx):
    embed = discord.Embed(title="Voici une liste des commandes disponibles : \n(...) = Argument obligatoire | [...] = Argument optionnel",
                          colour=discord.Colour.magenta())
    embed.set_thumbnail(url="https://media.giphy.com/media/fssa6xzdaLuDP938Y9/giphy.gif")
    embed.add_field(name="Modération :", value="  • *kick (membre) [raison] : Permet d'expulser un utilisateur du serveur "
                                               "\n• *ban (membre) [raison] : Permet de bannir un utilisateur du serveur"
                                               "\n• *unban (ID) [raison] : Permet de débannir un utilisateur du serveur", inline=False)
    embed.add_field(name="Informations :", value="• *ui (membre) : Affiche des informations sur un utilisateur", inline=False)
    embed.set_footer(text="Bot développé par ꒻꒐ꋊ꒯ꄲꇙꁝ_#2960")
    await ctx.send(embed=embed)

#•
client.run(token)