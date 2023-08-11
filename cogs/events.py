import traceback

from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(
        self, ctx: commands.Context, error: commands.CommandError
    ):
        try:
            raise error
        except commands.CommandNotFound:
            return
        except commands.CommandOnCooldown:
            return
        except commands.NoPrivateMessage:
            await ctx.author.send("This command cannot be used in DMs.")
        except commands.DisabledCommand:
            await ctx.send("This command is disabled.")
        except commands.NotOwner:
            await ctx.send("This command is owner only.")
        except Exception as e:
            traceback.print_exception(type(e), e, e.__traceback__)

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Username: {self.bot.user.name}")
        print(f"ID: {str(self.bot.user.id)}")


async def setup(self: commands.Bot):
    await self.add_cog(Events(self))
