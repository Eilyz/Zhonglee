import discord
from discord.ext import commands

from utils.buttons import RoleMenuSetupButtons


class Owner(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(aliases=["rms"])
    @commands.is_owner()
    async def role_menu_setup(self, ctx: commands.Context):
        embed = discord.Embed(
            color=discord.Color.purple(),
            title="Vanity Role Menu",
            description="Here you can create/delete/edit your vanity role.\nRole icon is optional and role color does not require the #, just input the value.",
        )
        embed.add_field(
            name="Creating",
            value="You'll enter the role name, color in hexadecimal format (without the #) and the icon url which is an "
            "image url. (make sure the image link ends with .png for transparent icons)",
        )
        embed.add_field(
            name="Deleting",
            value="Nothing special here, bot will handle the work you just need to press the big red "
            "button.",
        )
        embed.add_field(
            name="Editing",
            value="Rules for when creating also applies here.",
        )
        embed.set_footer(
            text="Only available for nitro boosters.",
        )
        await ctx.send(embed=embed, view=RoleMenuSetupButtons())


async def setup(self: commands.Bot):
    await self.add_cog(Owner(self))
