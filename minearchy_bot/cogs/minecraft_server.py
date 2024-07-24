from __future__ import annotations

from typing import TYPE_CHECKING

from discord.ext import commands
from discord.ext.commands import Cog, command
from discord.ui import Button, View

if TYPE_CHECKING:
    from discord.ext.commands import Context

    from .. import MinearchyBot


class MinecraftServer(
    Cog,
    name = "Minecraft Server",
    description = "Utilities for the Minecraft server.",
):
    def __init__(self, bot: MinearchyBot) -> None:
        self.bot = bot

    @commands.group(
        invoke_without_command = True,
        brief = "Sends the server IP.",
        help = "Sends the server IP.",
    )
    async def ip(self, ctx: Context) -> None:
        await ctx.reply(
            f"Java edition IP: `{self.bot.server.java.ip}`\nBedrock edition IP:"
            f" `{self.bot.server.bedrock.ip}`\nNote: Minecraft 1.21 is required to join."
        )

    @ip.command(
        brief = "Sends the Java edition IP.",
        help = "Sends the Java edition IP."
    )
    async def java(self, ctx: Context) -> None:
        await ctx.reply(
            "The IP to connect on Minecraft Java edition is"
            f" `{self.bot.server.java.ip}`\nNote: Minecraft 1.21 is required to join."
        )

    @ip.command(
        brief = "Sends the Bedrock edition IP.",
        help = "Sends the Bedrock edition IP.",
    )
    async def bedrock(self, ctx: Context) -> None:
        await ctx.reply(
            "The IP to connect on Minecraft Bedrock edition is"
            f" `{self.bot.server.bedrock.ip}`\nNote: Minecraft 1.21"
            " is required to join."
        )

    @command(
        aliases = ("servers",),
        brief = "Sends info about a specific server.",
        help = "Sends info about a specific server.",
    )
    async def server(self, ctx: Context, server: str | None = None) -> None:
        servers = {
            "smp": "The SMP is a server where people can play survival Minecraft alongside other members of the community, with a multitude of features such as shops, auctions and more.",
            "kitpvp": "The KitPvP server is a server where players can fight each other with preset items called kits. These kits can be used in prebuilt arenas. The aim of KitPvp is too defeat your opponent in combat, with whatever kit you chose.",
        }

        if server is None:
            await ctx.reply(
                f"You must specify a server. The available servers are: {', '.join(f'`{s}`' for s in servers)}."
            )
            return

        server = server.lower()
        if server not in servers:
            await ctx.reply(
                f"Invalid server. The available servers are: {', '.join(f'`{s}`' for s in servers)}."
            )
            return

        await ctx.reply(servers[server])

    @command(
        aliases = ("players", "playerlist"),
        brief = "Shows information about the Minecraft server.",
        help = "Shows the total player count, the Minecraft server IP and the server latency.",
    )
    async def status(self, ctx: Context) -> None:
        status = await self.bot.server.status()

        if (online := status.players.online) == 0:
            message = "The Minecraft server has nobody online :(."
        else:
            player_list = '\n'.join(f"- {player.name}" for player in status.players.sample)
            message = f"The Minecraft server has {online} players online:\n{player_list}"

        await ctx.reply(message)

    @command(
        brief = "Sends the link to the wiki.",
        help = "Sends the link to the wiki."
    )
    async def wiki(self, ctx: Context) -> None:
        view = View()
        view.add_item(
            Button(
                label = "Go to the wiki!",
                url = "https://landsofminearchy.com/wiki",
            )
        )
        await ctx.reply(view = view)

    @command(
        brief = "Sends the link to the store.",
        help = "Sends the link to the store.",
    )
    async def store(self, ctx: Context) -> None:
        view = View()
        view.add_item(
            Button(
                label = "Go to the store!",
                url = "https://landsofminearchy.com/store",
            )
        )
        await ctx.reply(view = view)

    @command(
        aliases = ("forums",),
        brief = "Sends the link to the forum.",
        help = "Sends the link to the forum.",
    )
    async def forum(self, ctx: Context) -> None:
        view = View()
        view.add_item(
            Button(
                label = "Go to the forum!",
                url = "https://landsofminearchy.com/forum",
            )
        )
        await ctx.reply(view = view)

    @command(
        aliases = ("map",),
        brief = "Sends the link to the dynmap.",
        help = "Sends the link to the dynmap.",
    )
    async def dynmap(self, ctx: Context) -> None:
        view = View()
        view.add_item(
            Button(
                label = "Go to the dynmap!",
                url = "https://landsofminearchy.com/dynmap",
            )
        )
        await ctx.reply(
            content = "The dynmap is an interactive, live map of our Minecraft server.", view = view
        )

    @command(
        brief = "Sends the links you can use to vote for the Minecraft server.",
        help = "Sends the links you can use to vote for the Minecraft server.",
    )
    async def vote(self, ctx: Context) -> None:
        view = View()
        view.add_item(
            Button(
                label = "Vote for the Minecraft server!",
                url = "https://landsofminearchy.com/vote",
            )
        )
        await ctx.reply(view = view)

    @command(
        name = "staff-application",
        aliases = (
            "apply",
            "staff-applications",
        ),
        brief = "Sends the link to the staff application.",
        help = "Sends the link to the staff application.",
    )
    async def staff_application(self, ctx: Context) -> None:
        view = View()
        view.add_item(
            Button(
                label = "Apply for staff!",
                url = "https://docs.google.com/forms/d/1I7Rh_e-ZTXm5L51XoKZsOAk7NAJcHomUUCuOlQcARvY/viewform",
            )
        )
        await ctx.reply(view = view)


async def setup(bot: MinearchyBot) -> None:
    await bot.add_cog(MinecraftServer(bot))
