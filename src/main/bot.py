import os
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN') #URL del bot creado en discord developer

bot = commands.Bot(command_prefix='!') #Prefijo del bot

#Función para realizar una operación matemática: suma
@bot.command(name = 'sum')
async def sumar(ctx, n1, n2):
  response = int(n1) + int(n2)
  await ctx.send(response)

#Función para realizar una operación matemática: resta
@bot.command(name = 'rest')
async def restar(ctx, n1, n2):
  response = int(n1) - int(n2)
  await ctx.send(response)

#Función para realizar una operación matemática: multiplicación
@bot.command(name = 'multi')
async def multiply(ctx, n1, n2):
  response = int(n1) * int(n2)
  await ctx.send(response)

#Función para realizar una operación matemática: división
@bot.command(name = 'div')
async def division(ctx, n1, n2):
  response = int(n1) // int(n2)
  await ctx.send(response)

bot.run(TOKEN)
