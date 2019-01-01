import discord
from discord.ext import commands
import random

#Bot TOKEN
TOKEN = 'NTI5NjY5NTE4ODUxNTcxNzMz.Dw0NNw.S0xG6Qde9HaUyMenyK1pl2tEFoc'

#Define the Discord.Client
client = commands.Bot(command_prefix = 'rd')

#Tell me when the bot is ready.
@client.event
async def on_ready():
    print('"Balde Poderoso" is connected to the Discord Client server and ready to execute commands.')
    await client.change_presence(game=discord.Game(name='Type "rdcommands"!'))

#Commands:
##Dice Rolls
###D4
@client.command(pass_context = True)
async def D4(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 4
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
###D6
@client.command(pass_context = True)
async def D6(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 6
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
###D8
@client.command(pass_context = True)
async def D8(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 8
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
###D10
@client.command(pass_context = True)
async def D10(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 10
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
###D12
@client.command(pass_context = True)
async def D12(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 12
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
###D20
@client.command(pass_context = True)
async def D20(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 20
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
###D100
@client.command(pass_context = True)
async def D100(ctx):
    message = ctx.message.content
    message_array = ctx.message.content.split()
    authorID = ctx.message.author.id
    authorName = ctx.message.author.name
    diceValue = 100
    #Detect Math Operations
    if len(message_array) > 1 and len(message_array) < 3:
        if message_array[1] == '+':
            await client.say("<@{}>, please insert a number after the `+`.".format(authorID))
        elif message_array[1] == '-':
            await client.say("<@{}>, please insert a number after the `-`.".format(authorID))
        elif message_array[1] == '*':
            await client.say("<@{}>, please insert a number after the `*`.".format(authorID))
        elif message_array[1] == '/':
            await client.say("<@{}>, please insert a number after the `/`.".format(authorID))
        else:
            await client.say("<@{}>, `{}` is not a valid operation sign.".format(authorID, message_array[1]))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit():
        value = int(message_array[2])
        if message_array[1] == '+':
            result = random.randint(1, diceValue)
            total = result + value
            await client.say("<@{}> `{}` + {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '-':
            result = random.randint(1, diceValue)
            total = result - value
            await client.say("<@{}> `{}` - {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '*':
            result = random.randint(1, diceValue)
            total = result * value
            await client.say("<@{}> `{}` * {} = {}".format(authorID, result, value, total))
        elif message_array[1] == '/':
            result = random.randint(1, diceValue)
            total = result / float(value)
            await client.say("<@{}> `{}` / {} = {}".format(authorID, result, value, total))
    elif len(message_array) > 1 and len(message_array) == 3 and message_array[2].isdigit() == False:
        await client.say("<@{}> `{}` is not a valid number.".format(authorID, message_array[2]))
    elif len(message_array) == 1:
        result = random.randint(1, diceValue)
        await client.say("<@{}> `{}` = {}".format(authorID, result, result))
####################################

##Help Command:
@client.command()
async def commands():
    #Create the Embed
    embed = discord.Embed(
        title = 'HELP:',
        description = 'The bot supports 7 dices, including D4, D6, D8, D10, D12, D20 and D100.',
        colour = discord.Colour.purple()
    )

    #Modify the Embed
    embed.set_footer(text = '''The prefix for bot commands is \'rd\'.
The help command is *rdcommands*''')
    embed.set_author(name = 'Balde Poderoso')
    ##Fields for the dice commands
    embed.add_field(name = 'D4', value = 'rdD4 `<operation sign|empty>` `<value|empty>`', inline = True)
    embed.add_field(name = 'D6', value = 'rdD6 `<operation sign|empty>` `<value|empty>`', inline = True)
    embed.add_field(name = 'D8', value = 'rdD8 `<operation sign|empty>` `<value|empty>`', inline = True)
    embed.add_field(name = 'D10', value = 'rdD10 `<operation sign|empty>` `<value|empty>`', inline = True)
    embed.add_field(name = 'D12', value = 'rdD12 `<operation sign|empty>` `<value|empty>`', inline = True)
    embed.add_field(name = 'D20', value = 'rdD20 `<operation sign|empty>` `<value|empty>`', inline = True)
    embed.add_field(name = 'D100', value = 'rdD100 `<operation sign|empty>` `<value|empty>`', inline = True)

    #Post the embed as a message
    await client.say(embed=embed)

#Run the Bot Script
client.run(TOKEN)
