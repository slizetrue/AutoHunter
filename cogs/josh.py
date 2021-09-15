import discord
import os
import random
from discord.ext import commands
from time import sleep

class Socials(commands.Cog):

    def _init_(self, client):
        self.client = client

    @commands.command()
    async def aplhayt(self, ctx):
        await ctx.send(f'https://www.youtube.com/channel/UCpliXPL-kvCX6PTuE-2dAvA')


def setup(client):
    client.add_cog(Socials(client))
