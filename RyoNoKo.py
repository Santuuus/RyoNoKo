import discord
import datetime
import random
import requests
from discord import app_commands
from discord.ext import tasks
from config import TOKEN, MUSIXTOKEN

intents = discord.Intents.all()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

#Commands
#Is it Jujutsu Kaisen?
@tree.command(name = "jjk-thursday", description = "Is it Jujutsu Kaisen Thursday??")
async def wednesday(interaction):
    #if it is wednesday
    if datetime.datetime.today().weekday() == 2:
        await interaction.response.send_message("It is JJK Thursday!")
        #send another message
        await interaction.channel.send("https://tenor.com/view/jujutsu-thursday-jujutsu-jujutsu-kaisen-jujutsu-kaisen-thursday-gojo-gif-13734841367417869316")
    else:
        await interaction.response.send_message("It is not JJK Thursday.")
       # await interaction.channel.send("https://tenor.com/view/ruby-hoshino-oshi-no-ko-anime-tears-crying-gif-16026934856871427303")

#Time until next Jujutsu Kaisen episode
@tree.command(name="next-episode", description="Time until the next episode?")
async def next_episode(interaction):
    # Get the current date and time
    current_datetime = datetime.datetime.now()

    # Get the current day of the week (Monday is 0 and Sunday is 6)
    current_weekday = current_datetime.weekday()

    # Calculate the number of days until the next Thursday
    days_until_next_thursday = (3 - current_weekday + 7) % 7

    # Set the target time as 3 PM
    target_time = datetime.time(15, 56, 0)
    
    #Get Unix timestamp for next wednesday at 3 PM
    target_timestamp = datetime.datetime.combine(current_datetime.date() + datetime.timedelta(days=days_until_next_thursday), target_time).timestamp()

    #if it is wednesday and past 3 PM
    if current_weekday == 3 and current_datetime.time() >= target_time:
        # Add 7 days to the timestamp
        target_timestamp += 7 * 24 * 60 * 60
    
    #if it is wednesday between 3 PM and 4 PM
    if current_weekday == 3 and current_datetime.time() >= datetime.time(15, 56, 0) and current_datetime.time() < datetime.time(18, 56, 0):
        await interaction.response.send_message("# Episode out now!")
    else:
        # Print the remaining time
        await interaction.response.send_message(f"Next Jujutsu Kaisen episode: <t:{int(target_timestamp)}:R>")

#Get a random line from a song of the selected artist
#@tree.command(name="lyrics", description="Get a random line from a song of the selected artist (first 30% of the lyrics because API)")
#@app_commands.describe(artist_name = "The name of the artist")
#@app_commands.checks.cooldown(1, 30, key=lambda i: i.user.id)
#async def lyrics(interaction, artist_name: str):
   #await interaction.response.send_message("Currently unavailable.", ephemeral=True)

    # url = f"http://api.musixmatch.com/ws/1.1/track.search?apikey={MUSIXTOKEN}&q_artist={artist_name}&page_size=500&f_has_lyrics=1"
    # print(f"Get tracks: {url}")
    # response = requests.get(url)
    # data = response.json()

    # # Check if songs were found
    # if data["message"]["header"]["status_code"] == 200:
    #     track_list = data["message"]["body"]["track_list"]
        
    #     if track_list:
    #         # Select a random song from the list
    #         track = random.choice(track_list)
    #         track_name = track["track"]["track_name"]
    #         artist = track["track"]["artist_name"]
            
    #         # Make the request to the Musixmatch API to get the lyrics of the selected song
    #         url = f"http://api.musixmatch.com/ws/1.1/matcher.lyrics.get?apikey={MUSIXTOKEN}&q_track={track_name}&q_artist={artist_name}"
    #         print(f"Get lyrics: {url}")
    #         response = requests.get(url)
    #         data = response.json()
            
    #         # Check if lyrics were found
    #         if data["message"]["header"]["status_code"] == 200:
    #             if "lyrics" in data["message"]["body"]:
    #                 lyrics = data["message"]["body"]["lyrics"]["lyrics_body"]
    #                 # Remove the final part of the lyrics starting from a line with "..."
    #                 lines = lyrics.split("\n")
    #                 ellipsis_index = next((i for i, line in enumerate(lines) if "..." in line), len(lines))
    #                 lines = lines[:ellipsis_index]
                    
    #                 # Remove empty lines
    #                 lines = [line for line in lines if line.strip()]
    #                 if lines:
    #                     random_line = random.choice(lines)
    #                     await interaction.response.send_message(f"*{random_line}* - **{track_name} by {artist}** ")
    #                 else:
    #                     await interaction.response.send_message(f"No lyrics found for song {track_name}")
    #         else:
    #             await interaction.response.send_message(f"Lyrics not found for song {track_name}")
    #     else:
    #         await interaction.response.send_message(f"No songs found for {artist_name}.")
    # elif data["message"]["header"]["status_code"] == 404:
    #     await interaction.response.send_message(f"Artist {artist_name} not found.")
    # else:
    #     await interaction.response.send_message("API Error")

#Live ROY reaction
@tree.command(name="roy", description="Live ROY reaction")
async def roy(interaction):
    await interaction.response.send_message(file=discord.File("assets/royreaction.png"))

#Quaso
@tree.command(name="quaso", description="QUASO")
async def roy(interaction):
    await interaction.response.send_message(file=discord.File("assets/quaso.png"))

#Bot uptime
@tree.command(name="uptime", description="Bot uptime")
async def uptime(interaction):
    if interaction.user.id == 282662959241756683:
        await interaction.response.send_message("Uptime: maior que o do <@1099352698572243007>")
    else:
        #calculate uptime
        uptime = datetime.datetime.now() - start_time
        #send message
        if uptime.days < 1:
            await interaction.response.send_message(f"Uptime: {uptime.seconds // 3600} hour(s), {uptime.seconds % 3600 // 60} minute(s) and {uptime.seconds % 3600 % 60} second(s)")
        else:
            await interaction.response.send_message(f"Uptime: {uptime.days} day(s), {uptime.seconds // 3600} hour(s), {uptime.seconds % 3600 // 60} minute(s) and {uptime.seconds % 3600 % 60} second(s)")

#Get Real
@tree.command(name="get-real", description="Get Real")
async def getReal(interaction):
    await interaction.response.send_message("https://tenor.com/view/oshi-no-ko-anime-ai-hoshino-idol-gif-8712266706126317077")

#Error handling
@tree.error
async def on_error(interaction, error):
    if isinstance(error, app_commands.errors.CommandOnCooldown):
        await interaction.response.send_message(f"Command on cooldown. Try again in {error.retry_after:.2f} seconds.", ephemeral=True)
    else:
        raise error


#Start the bot
@client.event
async def on_ready():
    await tree.sync()
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Ryo playing Bass"))
    global start_time 
    start_time = datetime.datetime.now()
    print("Ready!")

#Responds to mentions
@client.event
async def on_message(message):
    if client.user.mentioned_in(message) and message.author.id != 1099352698572243007:
        if message.mention_everyone:
            return
        await message.reply("Oshi No Ko Reference")
    elif message.author.id == 1099352698572243007:
        #if message contains "precisas de ajuda"
        if "precisas de ajuda" in message.content.lower():
            await message.reply("Preciso que te cales <a:peperonimo:1101073938039177350>", mention_author=False)
        if "stay malding bozo" in message.content.lower():
            await message.reply("Mald deez nuts.", mention_author=False)
     

#Run
client.run(TOKEN)