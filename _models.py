from pydantic import BaseModel, EmailStr
class Admin(BaseModel):
    password: str
    email: EmailStr

class AdminShow(Admin):
    admin_id: int
    
    class Config:
        orm_mode = True

class Quiz(BaseModel):
    title: str
    description: str

class QuizShow(BaseModel):
    title: str
    description: str
    totalMarks:int
    class Config:
        orm_mode = True

class Question(BaseModel):
    text: str
    option1: str
    option2: str
    option3: str
    option4: str
    correct_option: str

class QuestionShow(BaseModel):    
    text: str
    option1: str
    option2: str
    option3: str
    option4: str
    class Config:
        orm_mode = True
class QuestionShow_with_id                                                                                                                                                                                                                                                                                                                                                                                                                                                                   (BaseModel):  
    question_id:int  
    text: str
    option1: str
    option2: str
    option3: str
    option4: str
    class Config:
        orm_mode = True
class UserAnswers(BaseModel):
    question_id:int
    answer_option:str

class Participant(BaseModel):
    password: str
    email: EmailStr

class ParticipantShow(BaseModel):
    participant_id: int
    email:EmailStr
    class Config:
        orm_mode = True

class Score(BaseModel):
    participant_id: int
    quiz_id: int
    score: int

class ScoreShow(BaseModel):   
    score:int
    class Config:
        orm_mode = True
