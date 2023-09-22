import discord
import asyncio


class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def setup_hook(self) -> None:
        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(1154054239274938410)  # channel ID goes here
        while not self.is_closed():
            counter += 1
            await channel.send(counter)
            await asyncio.sleep(3)  # task runs every 60 seconds


client = MyClient(intents=discord.Intents.default())
client.run('MTE0NDU5Nzk0NDk3NzMzMDE3Ng.G-Gaxf.yoYmk6grUWNL3W_xqQuUafIw83_ExahfudBu6E')