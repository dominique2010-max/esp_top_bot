import discord
import random 
from discord.ext import commands
import requests 
import os 
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.command()
async def consejos (ctx):
    await ctx.send("Hola,preguntame todas tus dudas con respecto al medio ambiente  y yo te las respondere")


@bot.command()
async def respuesta(ctx, consejos:str):
    await ctx.send("Hola , {respuesta}  ")
    #wait ctx.send("Hola , respuesta")


respuesta  = {
    "Plastico:Sabias que el plastico se demora minimo 100 anos en descomponerse ",
    "Co2:toda maquina que trabaja con gasolina porduce el material co2,ese gas es el causante de el calentamiento global",
}

@bot.event
async def on_ready():
    print(f"✅ El bot está conectado como {bot.user}")

@bot.command(name="consejos")
async def preguntar(ctx, *, tema: str):
    tema = tema.lower()
    if tema in respuesta:
        await ctx.send(respuesta[tema])
    else:
        await ctx.send("No tengo información sobre ese tema 😔. Intenta con palabras como: deforestación, plástico, calentamiento global, reciclaje o agua.")

bot.run("token")
