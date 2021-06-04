from discord.ext.commands import Bot as BotBase

PREFIX = "P+"
OWNER_IDS = [844186332313288726]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("waking py++...")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Py++ is Online...")

    async def on_disconnect(self):
        print("Py++ is Offline...")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print("Py++ Cleaned codes...")

        else:
            print("Py++ is back...")

    async def on_message(self, message):
        pass


bot = Bot()
