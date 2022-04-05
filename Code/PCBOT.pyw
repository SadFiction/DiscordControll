#discord modules

from ast import arguments
from pydoc import describe
from discord.channel import TextChannel
from discord.commands.commands import slash_command
from discord.ext import commands

#other modules
from datetime import datetime
import threading, asyncio, media, os, sys, discord

from numpy import byte
try:
    import simplejson as json
except(ModuleNotFoundError):
    import json


client = commands.Bot()
med = media.media()
location = (sys.argv[0].replace("\\", "/")).replace("Code/PCBOT.pyw" , "") if "Code/PCBOT.pyw" in (sys.argv[0]).replace("\\", "/") else "./"
with open(f"{location}data/mainData.json", "r") as file:
    data = json.load(file) 
    guild_id = data["guildID"]
    token = data["token"]


@client.event
async def on_ready():
    print(f"\n{client.user.display_name} has risen !!!!!!")
    
@client.event
async def on_message(message):
    volumeUpOther = ["volume up", "vp" , "vol up", "up" , "+" ]
    volumeDownOther = ["volume down", "vd" , "vol dw" , "vol down", "down", "-"]
    pauseOther = ["pause", "pa", "#", "p"]
    nextOther = ["next", "nxt", "n", ">"]
    previousOther = ["previous", "prev", "pre", "pr", "<"]
    muteOther = ["mute", "mte", "m", "mu"]
    
    for i in pauseOther:
        if message.content.lower() == i:
            med.pause()
            await message.channel.send("` Paused/Unpaused `")
    for i in nextOther:
        if message.content.lower() == i:
            med.next()
            await message.channel.send("` Next `")
    for i in previousOther:
        if message.content.lower() == i:
            med.previous()
            await message.channel.send("` Previous `")
    for i in volumeDownOther:
        if i in message.content.lower():
            number = (((message.content.lower()).strip()).replace(i, "")).strip()
            try:
                if number == "":
                    med.volDw()
                    await message.channel.send("`  Volume Down  `")
                else:
                    number = int(number)
                    med.volDw(number)
                    await message.channel.send("`  Volume Down by "+ str(number) + "  `")
            except(Exception):
                return
    for i in volumeUpOther:
        if i in message.content.lower():
            number = ((message.content.lower().strip()).replace(i, "")).strip()
            try:
                if number == "":
                    med.volUp()
                    await message.channel.send("`  Volume Up  `")
                else:
                    number = int(number)
                    med.volUp(number)
                    
                    await message.channel.send("`  Volume Up by "+ str(number) + "  `")
                    
            except(Exception):
                return
    for i in muteOther:
        if message.content.lower() == i:
            med.mute()
            await message.channel.send("`  Muted/Unmuted  `")
        
        

@client.slash_command(guild_ids=[int(guild_id)], name= "state" , description="Everything to do with the computer's state.")
async def state(ctx, option : str, * , time_sec : int = None):
        time_sec = "" if time_sec is None else  f"/t {time_sec}"
        if option.lower() == "help":
            await ctx.respond("```\n Option: shutdown - shutsdown the computer \n Option: restart - restarts computer \n Option: signout - signout from computer(doesn't support timing) \n Option: abort - abort operation \n time_sec : <time in sec> - duration until execution of command \n ``` ")
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
@state.error
async def state_error(ctx, error):
    await ctx.respond(f"ERROR: ```\n {error} \n```")

@client.slash_command(guild_ids=[int(guild_id)], name="program_add", description="add programs to the 'program' command")
async def programAdd(ctx,  app_name: str, app_path:str, arguments = None, description : str = None):
    if os.path.exists(app_path):
        
        with open(f"{location}data/programs.json" , "r") as f:
            data= json.load(f)
            temp = data["apps"]
            build =  {
                "name" : app_name,
                "path" : app_path,
                "description" : description,
                "arguments" : arguments
            }
            temp.append(build)
            f.close()
        with open(f"{location}data/programs.json" , "w") as fl:
            json.dump(data, fl, indent=3)
            fl.close()
        await ctx.respond(f"```\nAdded... \nName:{app_name}, Path:{app_path}, Description:{description} ;```")
    else:
        await ctx.respond(f" {app_path} doesn't exist ...")

@client.slash_command(guild_ids=[int(guild_id)], name="program_remove", description="remove programs from the 'program' command ")
async def programRemove(ctx, name: str):
    found = False
    obj = json.load(open(f"{location}data/programs.json"))
    for i in range(len(obj["apps"])):
        if obj["apps"][i]["name"] == name:
            obj["apps"].pop(i)
            found = True
            break
    with open(f"{location}data/programs.json", "w") as file:
        json.dump(obj, fp=file, sort_keys=True, indent=3,  separators=(',', ': '))

    if found:
        await ctx.respond(f"{name.capitalize()} has been removed.")
    else:
        await ctx.respond(f"{name.capitalize()} could not be found")

@state.error
async def state_error(ctx, error):
    await ctx.respond(f"ERROR: ```\n {error} \n```")

@client.slash_command(guild_ids=[int(guild_id) ], name="program" , description="open or close programs")
async def program(ctx, app: str, option : str  = None ):
    if os.path.exists(app):
        os.system(f"start {app}")
    else:    
        if app.lower() == "help":
            with open(f"{location}data/programs.json", "r") as file:
                data = json.load(file)
                message = "```\nPROGRAMS:"
                for i in data["apps"]:
                    message += "\n\n" + f"Name : {i['name']}, Path: {i['path']} , Description: {i['description']}, Arguments : {i['arguments']}"
                message += "```"
                if message == "```\n```":
                    await ctx.respond("Please add programs by using the /add_app command") 
                else:
                    await ctx.respond(message)
        else:
            with open(f"{location}data/programs.json", "r") as file:
                data = json.load(file)
                
                errors = 0
                for i in data["apps"]:
                    if app.lower() == i["name"].lower():
                        if option is None or option == "start":
                            os.system(f"start {i['path']} {i['arguments'] if i['arguments'] is not None else ''}")
                            await ctx.respond(f"{i['name'].capitalize()} has been started.")
                        if option == "close":
                            os.system(f"taskill /IM {os.path.basename(i['path'])} /F")
                            await ctx.respond(f"{i['name'].capitalize()} has been closed.")
                    else:
                        errors += 1
                await ctx.respond("That is not valid option, could not find in programs.json") if errors == len(data["apps"]) else ""
                    
@program.error
async def program_error(ctx, error):
    await ctx.respond(f"ERROR: ```\n {error} \n```")


@client.slash_command(guild_ids=[int(guild_id)], name = "macro" , description="Macros for tasks.")
async def macro(ctx, task : str , option : str = None):
    if task.lower() == "help":
        await ctx.respond("Work in progress")

@client.slash_command(guild_ids=[int(guild_id)], name="browser", description="access the webbrowser")
async def browser(ctx, url : str):
    import webbrowser
    if url == "youtube":
        webbrowser.open("www.youtube.com")
    elif url == "netflix":
        webbrowser.open("www.netflix.com")
    elif url == "reddit":
        webbrowser.open("wwww.reddit.com")
    else:
        webbrowser.open(url)

    await ctx.respond("Done")

@browser.error
async def browser_error(ctx, error):
    await ctx.respond(f"ERROR: ```\n {error} \n```")

@client.slash_command(guild_ids=[int(guild_id)], name="cmd", description="Run shell commands")
async def cmd(ctx, command : str):
    os.system(command)
    await ctx.respond("done...")

@cmd.error
async def cmd_error(ctx, error):
    await ctx.respond(f"ERROR: ```\n {error} \n```")

@client.slash_command(guild_ids=[int(guild_id)], name="powershell", description="Run powershell commands")
async def powershell(ctx, command : str):
    import subprocess
    completed = subprocess.run(["powershell", "-Command", command], capture_output=True)
    await ctx.respond(f"```\n {(completed.stdout).decode('utf-8')}```")

@cmd.error
async def powershell_error(ctx, error):
    await ctx.respond(f"ERROR: ```\n {error} \n```")

client.run(token)
    




