class BotConfig():
    def __init__(self, delay=2):
        self.delay = delay
        self.admins = [248283246, 7327655623]
        self.count_messages = 300
        self.generation = False
        self.error_message = False
        self.count_errors = 0

    def get_delay(self):
        return self.delay
    
    def set_admin(self, id):
        self.admins.append(id)

    def get_admins(self):
        return self.admins


config = BotConfig()
