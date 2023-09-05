import requests
import random
import string

#It generate ramdom user name
def username():
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(12))


def signup():
    username = username()
    


def login():
    pass