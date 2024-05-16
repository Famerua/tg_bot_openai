BOT_TOKEN: str
with open("token.txt") as f:
    BOT_TOKEN = f.read()

OPENAI_TOKEN: str
with open("openai_api.txt") as f:
    OPENAI_TOKEN = f.read()
