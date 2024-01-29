import re
from pydantic import EmailStr
'''
This module is for extra utilities function that required
'''
email_regex = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')

def is_email_taken(email: EmailStr, model,session) -> bool:
    '''check in database the given email is already exist or not
it is work for both admin and participants 
input:
    email : Email String
    model : model or table where to check
    session : SQLAlchemy Database Session Utility 
'''
    existing_object = session.query(model).filter_by(email=email).first()
    return existing_object is not None

def evalute_score(quiz_id, answers, question, session):
    ''' This function evalute the score of participant 
Initially it is assumed that all questions are contains 1 marks. 
input:
    quiz_id : integer | Id of the quiz
    answers : the  answer model that is submited by user it is List of dict
    question: question model or Question table
    session : SQLAlchemy Database Session Utility 
'''
    ## Let Assume each question has only 1 score and no negative for wrong.
    score = 0 
    questions = session.query(question).filter_by(quiz_id = quiz_id)
    for question_id, answer in [(item.question_id, item.answer_option) for item in answers] : 
        if questions.filter_by(question_id=question_id).first().correct_option==answer:
            score +=1
    return score 
        