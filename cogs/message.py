import discord
from discord.ext import commands


class MessageCog(commands.Cog):
  def __init__(self, client):
    self.client = client
  
  @commands.Cog.listener()
  async def on_member_join(self, ctx, member):
    channel = client.get_channel(1171739092552257587)
    embed = discord.Embed(
      color = discord.color.green,
      title = test
    )
    await channel.send(embed=embed)

def setup(client):
  client.add_cog(MessageCog(client))