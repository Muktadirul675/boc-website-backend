import re


def is_a_valid_email(email):

    pattern = "\S+@\S+\.com"
    match = re.match(pattern, email)

    if match:
        return True
    

    return False

def make_username(username):
    username = username.split()
    username = "".join(username)

    return username

print(make_username("MD Mukta9 6 5"))

