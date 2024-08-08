
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "27383453" # integer value, dont use ""
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"
    TOKEN = "6797752601:AAHrEu4VBbnFnnrV9jja8gGavrnXZENgtFI"  # This var used to be API_KEY but it is now TOKEN, adjust accordingly.
    OWNER_ID = "6762113050" # If you dont know, run the bot and do /id in your private chat with it, also an integer
    
    SUPPORT_CHAT = "MASTIWITHFRIENDSXD"  # Your own group for support, do not add the @
    START_IMG = "https://telegra.ph/file/487a4f14fa6c7222cd6aa.jpg"
    EVENT_LOGS = "-1002018556839"  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority"
    # RECOMMENDED
BOT_USERNAME = getenv("BOT_USERNAME" , "StrangerSuperbot")
    DATABASE_URL = getenv("DATABASE_URL", "postgres://iarfggbc:Vxzh_kG7cxa1kHR5faxcd1kuA4R-UT9E@rosie.db.elephantsql.com/iarfggbc")
    CASH_API_KEY = (
        ""  # Get your API key from https://www.alphavantage.co/support/#api-key
    )
    TIME_API_KEY = ""
    # Get your API key from https://timezonedb.com/api

    # Optional fields
    BL_CHATS = []  # List of groups that you want blacklisted.
    DRAGONS = []  # User id of sudo users
    DEV_USERS = []  # User id of dev users
    DEMONS = []  # User id of support users
    TIGERS = []  # User id of tiger users
    WOLVES = []  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
