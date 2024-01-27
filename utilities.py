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

def evalute_score(quiz_id, answers, question, session):
    ## Let Assume each question has only 1 score and no negative for wrong.
    score = 0 
    questions = session.query(question).filter_by(quiz_id = quiz_id)
    for question_id, answer in [(item.question_id, item.answer_option) for item in answers] : 
        if questions.filter_by(question_id=question_id).first().correct_option==answer:
            score +=1

    return score 
        