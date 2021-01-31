import os

class Config:
    aid = int(os.environ.get("API_ID", "2327886"))
    ahash = os.environ.get("API_HASH", "b27fc6b63c22a6917438a57bc616075c")
    bot_token = os.environ.get("BOT_TOKEN", "1392937433:AAFj4L8wHUfeWG94iGrxSH3ZNh5fkbEroL0")
    sudo = [1078841825, 1076632911]
    # try:
    #     sudo = set(int(x) for x in os.environ.get("SUDO", "").split(','))
    # except ValueError:
    #     raise Exception("Your sudo users list does not contain valid integers.")
    
