
from datetime import datetime

class Spy_info:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status = None


class Chat_msg:

    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me

spy = Spy_info('Avantika','Ms.',20,4)

friend_one = Spy_info('srishti','Ms.',4.9,23)
friend_two = Spy_info('ishan','Mr.',4.39,20)
friend_three = Spy_info('priyanka','Ms.',4.95,27)

myfriends = [friend_one, friend_two, friend_three]

