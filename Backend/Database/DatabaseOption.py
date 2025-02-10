import dotenv
import os

class DatabaseOption:
    dotenv.load_dotenv()
    def __init__(self,host:str=os.getenv("HOST"), user:str = os.getenv("DB_USER"), pwd:str = os.getenv("PASSWD"), db_name:str = os.getenv("DB_NAME")):

        self.host = host
        self.user = user
        self.pwd = pwd
        self.db_Name = db_name