import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import email_draft, openai_comp

intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

load_dotenv()

@bot.event
async def on_message(message):
  user_message = str(message.content)
  channel = str(message.channel.name)
  
  if message.author == bot.user:
    return
  
  if channel == "announcements":
    print(user_message)
    def check(reaction, user):
      return (
        user == message.author
          and str(reaction.emoji) == "✅"
          and reaction.message.id == message.id
      )
    reaction, user = await bot.wait_for('reaction_add',check=check)
    if(reaction):
        print("YESSSSS")
        print("Sending email...")
        email_draft.start_draft("maxsrobotics@gmail.com", "TEST 1", openai_comp.comp(user_message, 1000))

bot.run(os.getenv('DISCORD_TOKEN'))