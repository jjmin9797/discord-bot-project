class HelloService:
    async def sendHello(message):
        await message.channel.send("Hello World!")
