from os import environ

import discord
from discord.ext import commands

client = commands.Bot(command_prefix='*')
token = environ.get('TOKEN')


@client.event
async def on_ready():
    print('Jinbot en Ligne.')


@client.command()
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.ban(user, reason=reason)
    embed = discord.Embed(title="**Bannissement**", description="Ce membre a été banni du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.red())
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/796861724366995457.gif")
    embed.add_field(name="Membre banni : ", value=user.name, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="Bot développé par 𝓙ɪήժøƨħ_,Ƭħε Ðɪƨħøήørεժ#7992 ")
    await ctx.send(embed=embed)


@client.command()
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.kick(user, reason=reason)
    embed = discord.Embed(title="**Expulsion**", description="Ce membre a été expulsé du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.orange())
    embed.set_thumbnail(url="https://media.tenor.com/images/27f16871c55a3376fa4bfdd76ac2ab5c/tenor.gif")
    embed.add_field(name="Membre expulsé : ", value=user.name, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="Bot développé par 𝓙ɪήժøƨħ_,Ƭħε Ðɪƨħøήørεժ#7992 ")
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
    embed.add_field(name="Nom de l'utilisateur : ", value=member.name, inline=False)
    embed.add_field(name="ID de l'utilisateur : ", value=member.id, inline=False)
    embed.add_field(name="Compte crée le ", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="A rejoint le serveur le ", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Rôle le plus haut", value=member.top_role.mention)
    embed.set_footer(text="Bot développé par 𝓙ɪήժøƨħ_,Ƭħε Ðɪƨħøήørεժ#7992 ")
    await ctx.send(embed=embed)





client.run(token)