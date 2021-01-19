import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix='&')
token = os.environ.get('TOKEN')

@client.event
async def on_ready():
    print('Bot prêt')

@client.command()
async def ban(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.ban(user, reason = reason)
    embed = discord.Embed(title="**Bannissement**", description="Ce membre a été banni du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.red())
    embed.set_thumbnail(url="https://cdn.discordapp.com/emojis/796861724366995457.gif")
    embed.add_field(name="Membre banni : ", value=user.name, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="discord.gg/a7KHDT9gFT")
    await ctx.send(embed=embed)

@client.command()
async def kick(ctx, user: discord.User, *, reason="Aucune raison n'a été spécifiée."):
    await ctx.guild.kick(user, reason = reason)
    embed = discord.Embed(title="**Expulsion**", description="Ce membre a été expulsé du serveur",
                          url="https://www.discord.gg/a7KHDT9gFT", colour=discord.Colour.orange())
    embed.set_thumbnail(url="https://i.giphy.com/media/dYQfIcryc28bS6132z/giphy.gif")
    embed.add_field(name="Membre expulsé : ", value=user.name, inline=False)
    embed.add_field(name="Modérateur : ", value=ctx.author.name, inline=False)
    embed.add_field(name="Raison", value=reason, inline=True)
    embed.set_footer(text="discord.gg/a7KHDT9gFT")
    await ctx.send(embed=embed)

client.run(token)
