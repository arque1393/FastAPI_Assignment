import re
from pydantic import EmailStr
email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

# def validate_email(email):
#     return bool(re.match(email_regex, email))

def is_username_taken(username: str) -> bool:
    if username == 'bb': return True
    # TODO 


def is_email_taken(email: EmailStr, model,session) -> bool:
    '''email is email string object of fastapi for email validate, 
model is any database schema model that are derrived from Base'''
    existing_object = session.query(model).filter_by(email=email).first()
    return existing_object is not None