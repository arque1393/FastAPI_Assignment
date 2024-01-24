import re
from pydantic import EmailStr
email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# def validate_email(email):
#     return bool(re.match(email_regex, email))

def is_username_taken(username: str) -> bool:
    if username == 'bb': return True
    # TODO 


def is_email_taken(email: EmailStr) -> bool:
    # Replace this with your logic to check if the email is already taken
    # TODO
    # For example, query your database
    return False