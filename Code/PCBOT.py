import os
from discord.ext import commands
import asyncio
import sys
import os

screenshot_channel = ""
command_channel = ""
guild_id = ""
location = "./"
if "Code/PCBOT.py" in (sys.argv[0]).replace("\\", "/"):
    location = (sys.argv[0].replace("\\", "/")).replace("Code/PCBOT.py" , "")

with open(f"{location}data/guild_id.txt" , "r") as file:
    guild_id = file.read()
    file.close()
with open(f"{location}data/screenshot_channel_id.txt" , "r") as file:
    screenshot_channel = file.read()
    file.close()
with open(f"{location}data/command_channel_id.txt" , "r") as file:
    command_channel = file.read()
    file.close()

client = commands.Bot()
@client.event
async def on_ready():
    print(f"\n{client.user.display_name} has risen !!!!!!")

@client.slash_command(guild_ids=[int(guild_id)], name= "state" , description="Everything to do with the computer's state.")
async def state(ctx, option : str, * , time_sec : int = None):
    if str(ctx.channel.id) == command_channel:
        if time_sec is None:
            time_sec = ""
        elif time_sec is not None:
            time_sec = f"/t {time_sec}"
        if option.lower() == "help":
            await ctx.respond("```\n option: shutdown - shutsdown the computer \n option: restart - restarts computer \n option: signout - signout from computer \n option: abort - abort operation \n time_sec : <time in sec> - duration until execution of command \n ``` ")
        elif option.lower() == "shutdown":
            os.system(f"shutdown /s {time_sec}")
            await ctx.respond("Shuting pc down, please use `/state option: abort`- to abort.")
        elif option.lower() == "restart":
            os.system(f"shutdown /r {time_sec}")
            await ctx.respond("Restarting pc down, please use `/state option: abort` - to abort")
        elif option.lower() == "signout":
            if time_sec != "":
                os.system(f"shutdown /l ")
                await ctx.respond("Logging out from computer")
            elif time_sec == "":
                await ctx.respond("Sorry loggout can't me timed... please try again")
        elif option.lower() == "abort":
            os.system(f"shutdown /a")
            await ctx.respond("Operation has been aborted")
    else:
        return
    
@state.error
async def state_error(ctx, error):
    ctx.respond(f"ERROR: ```\n {error} \n```")

with open(f"{location}data/token.txt" , "r") as token:
    client.run((token.read()).strip())
    token.close()