from discord.ext import commands
import discord
import time

bot = commands.Bot(command_prefix="/")
client = discord.Client()


default_intents=discord.Intents.default()
default_intents.members = True
client = discord.Client (intents=default_intents)

datednd = "On n'a pas encore définis de date !"

@bot.event
async def on_ready () :
	print("Le bot est prêt")

@bot.command(name="dnd")
async def dnd(ctx):
	"""
	Sert a consulter ou modifier la date de la prochaine session de dnd
	"""
	channel = ctx.channel
	embed = discord.Embed(title="Donjons et Dragons", description = "Voulez vous consulter 👓 ou modifier 🖋️ la date ?", colour = discord.Colour.green())
	messages_ = await channel.send(embed=embed)
	await messages_.add_reaction("👓")
	await messages_.add_reaction("🖋️")
	await ctx.message.delete()
	message = ctx.message.author
	def checkmessage(message) :
		return message.author == ctx.message.author and ctx.message.channel == message.channel
	def checkEmoji(reaction, user) :
		return ctx.embed.author == user and embed.id == reaction.embed.id and (str(reaction.emoji) == "👓" or str(reaction.emoji) == "🖋️")

	try:
		reaction, user = await bot.wait_for("reaction_add", timeout = 10, check = checkEmoji)
		if reaction.emoji == "👓" :
			await ctx.send(datednd)
		elif reaction.emoji == "🖋️" :
			await ctx.send("Quand voulez-vous que soit la prochaine session ?")
	except:
		await ctx.send("La commande a été anulé")


@bot.command(name = 'vent')
async def vent(ctx) :
	"""
	sert a marquer quand on s'est prits un vent
	"""
	t = time.localtime()
	current_time = time.strftime("%H:%M:%S", t)
	await ctx.channel.send("Vent prit à " + current_time)
	await ctx.message.delete()

@bot.command(name = 'sondage')
async def sondage(ctx,*, msg):
	"""
	Sert a créer des sondage (à séparer avec "/")
	"""
	channel = ctx.channel
	try:
		op1 , op2 = msg.split("/")
		txt = f"Réagis avec 1️⃣ pour {op1} ou avec 2️⃣ pour {op2}"
	except:
		await channel.send("Correct Syntax: [Choicel] / [Choice2]" )
		return

	embed = discord.Embed(title="Sondage", description = txt, colour = discord.Colour.red())
	message_ = await channel.send(embed=embed)
	await message_.add_reaction("1️⃣")
	await message_.add_reaction("2️⃣")
	await ctx.message.delete()

@bot.command(name="say")
async def say(ctx, *, message):
	"""
	Sert a faire parler le bot
	"""
	await ctx.message.delete()
	await ctx.channel.send(message)


@client.event
async def on_member_join(member) :
	general_channel = client.get_channel(301830405978324992)
	await general_channel.send(content=f"Bienvenue dans la compagnie sans nom {member.display_name} !")

@bot.event
async def on_ready() :
	print("Le bot est prêt !")


bot.run("*****************************************")

