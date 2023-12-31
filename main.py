import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from utils.buttons import RoleMenuSetupButtons

load_dotenv()


class Zhongli(commands.Bot):
    def __init__(self):
        super().__init__(intents=discord.Intents.all(), command_prefix=".")
        self.client_id = 1139610284693127270
        self.owner_ids = [488699894023061516, 159764169636184064]
        self.token = os.getenv("DISCORD_TOKEN")
        self.remove_command("help")

    async def setup_hook(self):
        for extension in os.listdir("cogs"):
            if extension.endswith(".py"):
                try:
                    await self.load_extension(f"cogs.{extension[:-3]}")
                except Exception as e:
                    print(
                        f"Failed to load extension {extension[:-3]}\n{type(e).__name__}: {e}"
                    )
        self.add_view(RoleMenuSetupButtons(timeout=None))
        await self.tree.sync()

    def run(self):
        super().run(self.token, reconnect=True)


Zhongli = Zhongli()


# Context menus goes here
@Zhongli.tree.context_menu(name="Avatar")
async def avatar(interaction: discord.Interaction, member: discord.Member):
    embed = discord.Embed(color=discord.Color.random(), title=f"{member.name}'s Avatar")
    embed.set_image(url=member.avatar.url)
    await interaction.response.send_message(embed=embed)


@Zhongli.tree.context_menu(name="Server Avatar")
async def avatar(interaction: discord.Interaction, member: discord.Member):
    embed = discord.Embed(
        color=discord.Color.random(), title=f"{member.name}'s Server Avatar"
    )
    embed.set_image(url=member.display_avatar.url)
    await interaction.response.send_message(embed=embed)


Zhongli.run()
