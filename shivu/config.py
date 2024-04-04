class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/a
OWNER_ID = 5691178083
sudo_users = "5691178083", "5791955148", "1938688666", "5930690809", "6831910507", "5151095145"
GROUP_ID = "-1002137911091"
TOKEN = "6906842854:AAGR61KidTvhia9MJvBCJVvt3yNPqhNAh60"
mongo_url = "mongodb+srv://kronos:1q2w3e4r5t6y7u8i9o0p@kronos0.2hfeyzv.mongodb.net/?retryWrites=true&w=majority"
PHOTO_URL = ["https://telegra.ph/file/11ef347fe9cca05e7ec8d.jpg", "https://telegra.ph/file/1551b798deb9a40508b2c.jpg", "https://telegra.ph/file/9c2fa21967a93d876deb9.jpg", "https://telegra.ph/file/900f73d2e740d7061b6f6.jpg", "https://telegra.ph/file/9b4fd107c50441bb80647.jpg"]
SUPPORT_CHAT = "spartans_mainchats"
UPDATE_CHAT = "waifuhunterlogz"
BOT_USERNAME = "WaifuhunteRZbot"
CHARA_CHANNEL_ID = "-1002011392805"
api_id = 26626068
api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
