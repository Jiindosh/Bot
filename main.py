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
    embed.set_footer(text="discord.gg/a7KHDT9gFT")
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
    embed.set_footer(text="discord.gg/a7KHDT9gFT")
    await ctx.send(embed=embed)


@client.command(name='del')
async def delete(ctx, number_of_messages: int):
    messages = await ctx.channel.history(limit=number_of_messages + 1).flatten()

    for each_messages in messages:
        await each_messages.delete()

@client.command()
async def userinfo(ctx, *, user: discord.User = None): # b'\xfc'
    if user is None:
        user = ctx.author
    date_format = "%a, %d %b %Y %I:%M %p"
    embed = discord.Embed(color=0xdfa3ff, description=user.mention)
    embed.set_author(name=str(user), icon_url=user.avatar_url)
    embed.set_thumbnail(url=user.avatar_url)
    embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))
    members = sorted(ctx.guild.members, key=lambda m: m.joined_at)
    embed.add_field(name="Join position", value=str(members.index(user)+1))
    embed.add_field(name="Registered", value=user.created_at.strftime(date_format))
    if len(user.roles) > 1:
        role_string = ' '.join([r.mention for r in user.roles][1:])
        embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)
    perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])
    embed.add_field(name="Guild permissions", value=perm_string, inline=False)
    embed.set_footer(text='ID: ' + str(user.id))
    return await ctx.send(embed=embed)
    if isinstance(ctx.channel, discord.DMChannel):
        return

client.run(token)
