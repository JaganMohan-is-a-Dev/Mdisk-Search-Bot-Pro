# (c) @RoyalKrrishna

import os
# from dotenv import load_dotenv

# load_dotenv()


class Config(object):
    API_ID = int(os.getenv("API_ID", 13115322))
    API_HASH = os.getenv("API_HASH", "f28fbd1367ddda2e6f863c3129323743")
    BOT_TOKEN = os.getenv("BOT_TOKEN", "5478011283:AAF8wL2dZIeh2p7j-ocz5TtydqowKtRQZ90")
    BOT_SESSION_NAME = os.getenv("BOT_SESSION_NAME", "MdiskSearchRobot")
    USER_SESSION_STRING = os.getenv("USER_SESSION_STRING", "1BQANOTEuMTA4LjU2LjEzMAG7csLbWKKZ6obqCgKth3Cep09dW6xAW4ga2nxJ4S3SCuPuTyLb8+lOPrLoTys0LfCw95o60POH7MgLKedV83laJKwNtgqcd0dxGpMmJdiZ+IxVhDplTkRlbVZ88BwNtlCa8C+xSTFIb/9/ut1icQBFUfjrui7Np1DopwYVtfU+b4CiCqseTXylHJcgiklSqw9nQoZizVv1F5FdW7WsdZlhltEex+VEGBoXoVeYCyefTZSEHlZ5VcnAh/MdnzAad/9gnJLS3+L7VixneARTeDBosvFK9zvTZhJFefUhAPE0NDoZs3UPglWHn93cBLQR1tID0rOdd5wQp3NEgEwMqpNTtw==")
    CHANNEL_ID = int(os.getenv("CHANNEL_ID", -1001731898377))
    BOT_USERNAME = os.getenv("BOT_USERNAME", "URL_UPLODER_MB_BOT")
    BOT_OWNER = int(os.getenv("BOT_OWNER", 1459910748))
#    OWNER_USERNAME = os.getenv("OWNER_USERNAME", "MR_JAGANMOHAN")
    BACKUP_CHANNEL = os.getenv("BACKUP_CHANNEL", "Telugu_Babai")
#    GROUP_USERNAME = os.getenv("GROUP_USERNAME")
    START_MSG = os.getenv("START_MSG", "Hello 👋 bro Movies kavalante search cheyali Mari late endhuku")
    START_PHOTO = os.getenv("START_PHOTO", "https://telegra.ph/file/4a47e76b30ab30380780f.jpg")
    HOME_TEXT = os.getenv("HOME_TEXT", "Hi Bro")
    UPDATES_CHANNEL = os.getenv("UPDATES_CHANNEL", "-1001767843542")
    DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://Jagan:753753753@cluster0.zisdn.mongodb.net/?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.getenv("LOG_CHANNEL", "-1001712123362"))
    RESULTS_COUNT = int(os.getenv("RESULTS_COUNT", 10))
    BROADCAST_AS_COPY = os.getenv("BROADCAST_AS_COPY", "True")
    UPDATES_CHANNEL_USERNAME = os.getenv("UPDATES_CHANNEL_USERNAME", "Telugu_Babai")
    FORCE_SUB = os.getenv("FORCE_SUB", "True")
    AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", 300))
    MDISK_API = os.getenv("MDISK_API", "zwxo6CxXnwc5vnNqj7PT")
    VERIFIED_TIME  = int(os.getenv("VERIFIED_TIME", "1"))
    ABOUT_BOT_TEXT = os.getenv("ABOUT_TEXT", "in Next update")
    ABOUT_HELP_TEXT = os.getenv("HELP_TEXT", "Na gurinchi neku endhuku movie chudu")
