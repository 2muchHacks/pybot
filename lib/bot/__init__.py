from discord import Intents
import os
from discord import Embed
from discord.ext.commands import Bot as BotBase

PREFIX = "P+"
OWNER_IDS = [844186332313288726]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None

        super().__init__(
            command_prefix=PREFIX,
             owner_ids=OWNER_IDS,
             intents=Intents.all()
        )

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("waking py++...")
        super().run(os.environ['DISCORD_TOKEN'])

    async def on_connect(self):
        print("Py++ is Online...")

    async def on_disconnect(self):
        print("Py++ is Offline...")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("Py++ Cleaned codes...")
            channel = self.get_channel(850607259796504607)
            await channel.send("i am now online :eyes:")

            embed = Embed(title="PY++ here :wink:", description="I am brother of FUN++ but \'PYTHONIFIED', yes thats the word ...")
            fields = [("Name :", "Age  :", True),
                      ("PY++#9619","3 sec", True),
                      ("me belongs to", "2muchHacks#0419", False)]
            for name, value, inline in fields:          
                embed.add_field(name=name, value=value, inline=inline)
            await channel.send(embed=embed)    

        else:
            print("Py++ is back...")

    async def on_message(self, message):
        pass


bot = Bot()
