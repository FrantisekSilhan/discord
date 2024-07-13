import discord
from discord.ext import commands
from utils import prettify_member_name

class MessageCog(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.log_channel_id = 1261746740206374977
    self.allowed_guild_id = 1261746739623231499

  @commands.Cog.listener()
  async def on_member_join(self, member):
    if member.guild.id == self.allowed_guild_id:
      channel = self.client.get_channel(self.log_channel_id)
      embed = discord.Embed(
        color = discord.Color.green(),
        description = "**{}** joined the server.".format(prettify_member_name(member))
      )
      await channel.send(embed=embed)

  @commands.Cog.listener()
  async def on_member_remove(self, member):
    if member.guild.id == self.allowed_guild_id:
      channel = self.client.get_channel(self.log_channel_id)
      embed = discord.Embed(
        color = discord.Color.red(),
        description = "**{}** left the server.".format(prettify_member_name(member))
      )
      await channel.send(embed=embed)

def setup(client):
  client.add_cog(MessageCog(client))
