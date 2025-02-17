from discord.ext import commands

# Variáveis
token = "bgags76xgd7esag6wedq988dusqw9xsdjq98wdxqh8.asdxjas787"  # your discord token 
channel_ids = [123456789435, 987654433212, 123456789009887]  # channels ids
claim_emojis = ["💖", "💗", "💘", "❤️", "💓", "💕", "♥️"]
channels = {}  
perssornagens = ["Pain"] #wish list
client = commands.Bot(command_prefix="%")

@client.event
async def on_ready():
    print("Selfbot is ready to be used.")
    print(f"Logged in as {client.user.name}")
    print("Command Prefix is %")
    
  
    for channel_id in channel_ids:
        try:
            channel = client.get_channel(channel_id)
            if channel is None:
                raise Exception(f"Channel with ID {channel_id} not found.")
            channels[channel_id] = channel 
            print(f"Canal {channel.name} (ID: {channel.id}) carregado com sucesso.")
        except Exception as e:
            print(f"Failed to retrieve channel with id {channel_id}\nError: {e}")

async def auto_claim(message):
    for component in message.components:
        for button in component.children:
            print(f"Found button with custom_id: {button.custom_id}, emoji: {button.emoji}, label: {button.label}")
            if button.emoji and button.emoji.name in claim_emojis:
                print(f"Claim Button (Heart Emoji). Clicking...")
               
                await button.click()

@client.event
async def on_message(message):
  
    if message.author.id == 432610292342587392 and message.channel.id in channel_ids:
        if message.content:
            print(f"Message from {message.author.id} in channel {message.channel.id}: {message.content}\n")
        
        if message.components and message.embeds:
            for embed in message.embeds:
                character_name = embed.author.name if embed.author else "N/D"
                if character_name in perssornagens:
                    await auto_claim(message)
    
    await client.process_commands(message)

client.run(token)