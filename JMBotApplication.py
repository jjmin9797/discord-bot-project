import discord
import sys, os
from service.HelloService import HelloService

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user}")


@client.event
async def on_message(message):
    if not message.content.startswith("$") or message.author == client.user:
        return
    messageContent = message.content.split()

    if message.content.startswith("$인사"):
        await message.channel.send("반갑습니다람쥐.")
    print(messageContent)
    print("넘어옴")


client.run("MTA5NzQ4MjkzNDkzNzczNTI1OQ.G8VURf.W07thL-yX-Pf_sAB_QRmdz8HQl1LLiOQ3B0sK8")
