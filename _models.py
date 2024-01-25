from pydantic import BaseModel, EmailStr
from typing import List
from datetime import datetime


from pydantic import BaseModel, EmailStr
from typing import List

class Admin(BaseModel):
    password: str
    email: EmailStr

class AdminShow(Admin):
    admin_id: int
    
    class Config:
        orm_mode = True

class Quiz(BaseModel):
    title: str
    description: str = None

class QuizShow(Quiz):
    quiz_id: int
    d_at: datetime
    
    class Config:
        orm_mode = True

class Question(BaseModel):
    quiz_id: int
    text: str
    option1: str
    option2: str
    option3: str
    option4: str
    correct_option: str

class QuestionShow(Question):    
    class Config:
        orm_mode = True

class Participant(BaseModel):
    password: str
    email: EmailStr

class ParticipantShow(Participant):
    participant_id: int
    
    class Config:
        orm_mode = True

class Score(BaseModel):
    participant_id: int
    quiz_id: int
    score: int

class ScoreShow(Score):   
    class Config:
        orm_mode = True
