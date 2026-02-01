import os

class Config(object):
    BOT_TOKEN = os.environ.get("BOT_TOKEN","8323958485:AAEFerYEi_-Vtcbo-EqR2H-eaROITSOhroE")
    API_ID = int(os.environ.get("API_ID","30560523"))
    API_HASH = os.environ.get("API_HASH","17ab58948bc24d85d961a39e058478a2")
    AUTH_USER = os.environ.get('AUTH_USERS', '8342427239').split(',')
    AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
    HOST = "https://drm-api-six.vercel.app"
    CREDIT = " 𝙎𝘼𝙄𝙉𝙄 𝘽𝙊𝙏𝙎"


