class Config(object):
    LOGGER = True
    API_ID = "27383453" 
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"
    TOKEN = "6797752601:AAHrEu4VBbnFnnrV9jja8gGavrnXZENgtFI"  
    OWNER_ID = "6762113050"
    
    SUPPORT_CHAT = "MASTIWITHFRIENDSXD" 
    START_IMG = "https://telegra.ph/file/487a4f14fa6c7222cd6aa.jpg"
    EVENT_LOGS = "-1002018556839"
    MONGO_DB_URI= "mongodb+srv://SHASHANK:STRANGER@shashank.uj7lold.mongodb.net/?retryWrites=true&w=majority"
   
    DATABASE_URL = "postgres://u4g7epl1eascgt:p039208bc961ee80650fe6d893faa86ea5a6ffe2d6b44e379bbab09046d58fac7@cb5ajfjosdpmil.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d93jaska2dlb3u"  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        ""
    )
    TIME_API_KEY = ""

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

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