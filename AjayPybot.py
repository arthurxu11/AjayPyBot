import discord, requests, time
from random import choice
from discord.ext import commands
from bs4 import BeautifulSoup as soup

client = commands.Bot(command_prefix = "!")

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.command()
async def fees(ctx, args):
        try:
            amount = int(args)
        except:
            return

        if amount <= 0:
            return

        stockx1 = round(amount * 0.875, 2)
        stockx2 = round(amount * 0.88, 2)
        stockx3 = round(amount * 0.885, 2)
        stockx4 = round(amount * 0.89, 2)
        goat = round((amount * 0.905) - 5, 2)
        if amount >= 100:
            ebay = round((amount * 0.971) - 0.3, 2)
        else:
            ebay = round(amount - ((amount*0.9)+(amount * 0.971 - 0.3)), 2)

        grailed = round(amount - ((amount*0.06)+(amount * 0.029 - 0.3)), 2)

        embed = discord.Embed(title="The Cook Lab Seller Fees", colour=3304416)
        embed.add_field(name="StockX Level 1", value="$"+str(stockx1), inline=True)
        embed.add_field(name="StockX Level 2", value="$"+str(stockx2), inline=True)
        embed.add_field(name="StockX Level 3", value="$"+str(stockx3), inline=True)
        embed.add_field(name="StockX Level 4", value="$"+str(stockx4), inline=True)
        embed.add_field(name="Goat", value="$"+str(goat), inline=True)
        embed.add_field(name="EBay", value="$"+str(ebay), inline=True)
        embed.add_field(name="Grailed", value="$"+str(grailed), inline=True)
        embed.set_footer(text="The Cook Lab")

        await ctx.channel.send(embed=embed)

@fees.error
async def fees_error(ctx, error):
    pass

@client.command()
@commands.cooldown(1, 60, commands.BucketType.user)
async def view(ctx, args):
    name = ctx.author
    await ctx.channel.send("Adding 50 views to your post now "+str(name))
    x= 0
    while x < 50:
        try:
            link = str(args)
            headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36',
                'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8'
            }
            requests.get(link, headers=headers)
            x += 1
            time.sleep(2)
        except:
            return

@view.error
async def view_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        msg = 'This feature has a 1 minute cooldown. There is {:.2f}s left until you can use it again'.format(error.retry_after)
        await ctx.send(msg)
    else:
        raise error

client.run("NzQzNTUwOTk3NDkzNzEwODQ4.XzWT1A.oPDbocnFlZPSELT9ebatLHUT9Gg")
