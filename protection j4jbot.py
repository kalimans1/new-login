import discord
from discord.ext import commands
from datetime import datetime, timedelta

intents = discord.Intents.all()  # Tüm niyetleri aç
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Bot {bot.user} olarak giriş yaptı.')
    
    # Bot başlatıldığında ses kanalına gir
    guild = bot.get_guild(1214280471496892516)  # Sunucunun ID'si
    voice_channel = guild.get_channel(1273631658955903017)  # Ses kanalının ID'si
    
    if voice_channel:
        await voice_channel.connect()
        print(f"{voice_channel.name} ses kanalına katıldı.")
    else:
        print("Ses kanalı bulunamadı.")

@bot.event
async def on_message(message):
    if message.guild.id == 1214280471496892516:  # Sunucunun ID'si
        member = message.author
        account_age = datetime.utcnow() - member.created_at
        
        if account_age < timedelta(days=15):
            role = discord.utils.get(message.guild.roles, id=1274767209301807185)  # Rol ID'si
            if role:
                await member.add_roles(role)
                print(f"{member.display_name} kullanıcısına {role.name} rolü verildi.")
    
    await bot.process_commands(message)

bot.run(process.env.token)  # Gerçek bot token'ınızı buraya ekleyin
