class User:
    """A class for each Facebook User subscribed to the bot"""

    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name

    def __repr__(self):
        return str(self.user_id) + ": " + self.name
