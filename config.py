import os

class Config(object):
    BOT_TOKEN = os.environ.get("7824594954:AAGvEYjOq2lMo0g2n5VYss_ooWwBqsRqIAY")
    API_ID = int(os.environ.get("29410975"))
    API_HASH = os.environ.get("f7b94f03cb81efef112761048cb1b4b1")
    VIP_USER = os.environ.get('VIP_USERS', '').split(',')
    VIP_USERS = [int(7457390260) for user_id in VIP_USER]
