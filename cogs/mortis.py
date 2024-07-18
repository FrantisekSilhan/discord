import discord
from discord.ext import commands
from utils import prettify_member_name
import requests
import os

class MortisCog(commands.Cog):
  def __init__(self, client):
    self.client = client
    self.log_channel_id = 1261746740206374977
    self.allowed_guild_id = 1261746739623231499

  @commands.slash_command(name="link", description="Link your Discord account to your Mortis account")
  async def link(self, ctx, code: str):
    user = ctx.author.id
    response = requests.post("https://mortis.icu/discord/link", json={"code": code, "discordId": user}, headers={"authorization": os.environ["API_KEY"]})
    if response.status_code == 200:
      await ctx.respond("Your Discord account has been linked to your Mortis account.", ephemeral=True)
    elif response.status_code == 404:
      await ctx.respond("The code you entered is invalid.", ephemeral=True)
    else:
      await ctx.respond("An error occurred while linking your Discord account to your Mortis account.", ephemeral=True)

  @commands.slash_command(name="unlink", description="Unlink your Discord account from your Mortis account")
  async def unlink(self, ctx):
    user = ctx.author.id
    response = requests.post("https://mortis.icu/discord/unlink", json={"discordId": user}, headers={"authorization": os.environ["API_KEY"]})
    if response.status_code == 200:
      await ctx.respond("Your Discord account has been unlinked from your Mortis account.", ephemeral=True)
    else:
      await ctx.respond("An error occurred while unlinking your Discord account from your Mortis account.", ephemeral=True)

def setup(client):
  client.add_cog(MortisCog(client))
