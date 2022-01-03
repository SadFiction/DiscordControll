import asyncio
from datetime import datetime
import threading
import os
import sys
import asyncio
import discord
from discord.channel import TextChannel
from discord.ext import commands

screenshot_channel = ""
command_channel = ""
guild_id = ""
location = "./"
if "Code/PCBOT.pyw" in (sys.argv[0]).replace("\\", "/"):
    location = (sys.argv[0].replace("\\", "/")).replace("Code/PCBOT.pyw" , "")

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

@client.slash_command(guild_ids=[int(guild_id)], name= "screenshot", descriptSion = "get's a random screenshot")
async def screenshot(ctx, other : str = None):
    import os

    import RandomScreenshotGetter
    if str(ctx.channel.id) == screenshot_channel:
        running = None
        if other is None:
            running = True

        elif other.lower() == "help":
            await ctx.respond("This command retrieves an image from an image uploading site where people unkowingly upload the screenshot they take to the 'cloud', this is completely legal ( i checked ).")
        while running:
        
            await ctx.respond("Getting your screenshot...")
        
            name = await RandomScreenshotGetter.screenshotGetter().get(location=(f"{location}data/"))
        
            try:
            
                await ctx.respond("Here's your random screenshot ( type 'other: help' for more info ) ", file=discord.File(fp=f"{location}data/screenshot{name}.png"))   
                running = False
            
        
            except(Exception):
                await ctx.respond("Oops...something happened...")
        
        
            try:
                os.remove(f"{location}data/screenshot{name}.png")
            except(FileNotFoundError):
                pass
    else:
        return

@screenshot.error
async def screenshot_error(ctx, error):
    ctx.respond(f"ERROR: ```\n {error} \n```")

@client.slash_command(guild_ids=[int(guild_id) ], name="apps" , description = "open or close apps")
async def appOpener(ctx, app: str, option : str  = None ):
    if option is not None:
        option = option.replace('\\' , '/')
    if str(ctx.channel.id) == command_channel:
        if app.lower() == "help":
            await ctx.respond("```\n osu - opens osu \n discord - opens discord \n steam - opens steam \n chrome - opens chrome ; option : <url> \n code - opens visual studio code ; option: <project name or location>\n minecraft - opens minecraft \n roblox - opens roblox \n ```")
        if app.lower() == "osu":
            if option is None:
                os.system("start C:/Users/trool/AppData/Local/osu!/osu!.exe" )
                await ctx.respond(f"Done. {app} has been opened")
            elif option == "close":
                os.system("taskkill /IM osu!.exe")
                await ctx.respond(f"Done. {app} has been closed")
        elif app.lower() == "discord":
            if option is None:
                os.system("start C:/Users/trool/AppData/Local/Discord/app-1.0.9003\Discord.exe" )
                await ctx.respond(f"Done. {app} has been opened")
            elif option == "close":
                closed = False
                for _ in range(10):
                    try:
                        os.system("taskkill /IM /T Discord.exe")
                        closed = True
                    except(Exception):
                        pass
                if closed:
                    await ctx.respond(f"Done. {app} has been closed")
        elif app.lower() == "steam":
            if option is None:
                os.system("start C:/Program Files (x86)/Steam/steam.exe" )
                await ctx.respond(f"Done. {app} has been opened")
            elif option == "close":
                os.system("taskkill /IM steam.exe ")
                await ctx.respond(f"Done. {app} has been closed")
        elif app.lower() == "chrome":
            import webbrowser
            if option == None:
                webbrowser.open()
                await ctx.respond(f"Done. {app} has been opened")
            elif option  == "close":
                os.system("taskkill /IM chrome.exe")
                await ctx.respond(f"Done. {app} has been closed")
            elif option != None:
                webbrowser.open(option)
                await ctx.respond(f"Done. {app} has been opened")
        elif app.lower() == "code":
            if option == None:
                os.system("code")
                await ctx.respond(f"Done. {app} has been opened")
            if option == "close":
                os.system("taskkill /IM Code.exe")
                await ctx.respond(f"Done. {app} has been closed")
            elif option != None:
              try:
                if "c:" in option.lower() :
                    os.system(f"code {option}  " )
                elif "d:" in option.lower() :
                    os.system(f"code {option}  " )
                elif "e:" in option.lower():
                    os.system(f"code {option}  " )
                else:
                    os.system(f"code C:/Users/trool/OneDrive/Documents/{option}/")
              except(FileNotFoundError):
                  await ctx.respond("Seems like file doesn't exist")
              await ctx.respond(f"Done. {app} has been opened")
        elif app.lower() == "minecraft":
            if option is None:
                os.system(f"start C:/Program Files/Badlion Client/Badlion Client.exe")
                await ctx.respond(f"Done. {app} has been opened")
            elif option == "close":
                os.system(f"taskkill /IM Badlion Client.exe")
                await ctx.respond(f"Done. {app} has been closed")
        elif app.lower() == "roblox":
            if option is None:
                import webbrowser
                webbrowser.open("www.roblox.com")
                await ctx.respond(f"Done. {app} has been opened")
            if option == "close":
                os.system(f"taskkill /IM chrome.exe /F")
                os.system(f"taskkill /IM RobloxPlayerLauncher.exe /F")
                os.system(f"taskkill /IM RobloxPlayerBeta.exe /F")
                await ctx.respond(f"Done. {app} has been closed")



        
        
with open(f"{location}data/token.txt" , "r") as token:

    client.run((token.read()).strip())
    token.close()


