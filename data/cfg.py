import configparser

class Config:
    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        self.config.read(file_name)

    def get_token(self):
        return self.config['BOT']['token']
    
config = Config('config.ini')

print(config.get_token())