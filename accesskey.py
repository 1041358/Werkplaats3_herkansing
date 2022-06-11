import string
import random

characters = list(string.ascii_uppercase + string.digits + "@#$%^*()")

def accesskey_function():
    accesskey = []
    for i in range(16):
	    accesskey.append(random.choice(characters))
    return "".join(accesskey)
