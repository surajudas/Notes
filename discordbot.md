# Notes on making a discord bot from scratch

## Meta
- Using :- [Pycord](https://pycord.readthedocs.io/en/master/index.html)
- Tutorials :- [lucas](https://www.youtube.com/watch?v=nW8c7vT6Hl4&list=PLW3GfRiBCHOhfVoiDZpSz8SM_HybXRPzZ&index=1)
- Different available Events :- [Event rerence](https://discordpy.readthedocs.io/en/stable/api.html#event-reference)
- Intents :- [intents](https://discordpy.readthedocs.io/en/stable/api.html#intents)
- Use '|| {link_to_file ||' for spoiler tags

## Imports
```py
import discord
from discord.ext import commands
```
## Basic Run

## Event
- A piece of code that runs when a specific activity has occured

## Intents
- To do read certain values(msgs, members,...) from the server you need to set that intent property of your client as `True`
```py
client.intents.messages = True
```

## Commands
- name the function what you want your command to be
- The 1st parameter you give to the function will be the context of the command, commanly represented by `ctx`
- you can have aliases for the command by supplying a list of strings in the function decorator
```py
@client.command(aliases=['test', 'speed'])
async def ping(ctx):
    await ctx.send(f"your ping is: {round(client.latency * 1000)}ms")
```
> Note: For some reason on_message and commands don't seem to work at the same time  
Fix: Overriding the default provided on_message forbids any extra commands from running. To fix this, add a bot.process_commands(message) line at the end of your on_message. For example:
```py
@bot.event
async def on_message(message):
    # do some extra stuff here

    await bot.process_commands(message)
```

## Cogs
- Organises code

## Baclground tasks
- Will do later if needed

## Errors
- All errors are handled in the same function context
- An event called on_command_error is made to catch all the errors
- An if statement can be used to get the specific error you want to act upon
```py
# Error handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please choose a difficulty mode")
```

## Checks
### Custom checks
- maybe will need

## Custom prefixes
- looks like a pain to implement 

## Converters

## Misc stuff
- Embeds can be sent to make bot replies stand out
```py
@client.command()
async def embed(ctx):
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=discord.Color.blue())
    embed.add_field(name="Field 1 Title", value="This is the value for field 1. This is NOT an inline field.", inline=False)
    embed.set_footer(text="This is the footer. It contains text at the bottom of the embed")
    await ctx.send(embed=embed)
```

- Store your bot token as an env variable using the dotenv module
  - First create a file called `.env` (no file name) which should have BOT_TOKEN="1234567890"
  - load the environment and then in the client.run call call the os.getenv method
```py
import os
from nextcord.ext import commands

# There are other ways to load environment variables but this is one
from dotenv import load_dotenv # https://pypi.org/project/python-dotenv/

# load_dotenv reads from a file called .env in the same directory as the python files which should roughly look like BOT_TOKEN="1234567890"
load_dotenv()

bot = commands.Bot(command_prefix="$")

# run the bot using the token in .env
bot.run(os.getenv('BOT_TOKEN'))
```