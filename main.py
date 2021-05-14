import discord

client = discord.Client()
TOKEN = "" #Write API key here.
bad_users = []
bad_user_count = 0
channel : discord.VoiceChannel

@client.event
async def on_ready():
    print("Bot is ready.")

@client.event
async def on_message(message):
    if message.content.startswith("-stop"):
        await client.close()
    if message.content.startswith("-here"):
        global channel
        channel = message.channel
    if message.content.startswith("-bad"):
        content = message.content
        word_list = content.split()
        bad_user = ""
        for substr in word_list:
            if(substr.startswith("<@!")):
                bad_user = substr
                break
        bad_users.append(int(bad_user[3:21]))

        
        
@client.event
async def on_voice_state_update(member: discord.Member, before: discord.VoiceState, after: discord.VoiceState):
    global bad_user_count
    global channel
    if member.id in bad_users:
        if before.channel == None:
            bad_user_count += 1
        if after.channel == None:
            bad_user_count -= 1
    new_name = f"BadUserCount-{bad_user_count}"
    await channel.edit(name=new_name)

client.run(TOKEN)