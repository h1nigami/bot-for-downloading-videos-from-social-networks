import configparser

class Config:
    def __init__(self, file_name):
        self.config = configparser.ConfigParser()
        self.config.read(file_name)

    def get_token(self, section, option):
        return self.config.get(section=section, option=option)
    
