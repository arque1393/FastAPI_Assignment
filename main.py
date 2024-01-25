from typing import List
from fastapi import FastAPI, Depends
from _models import Admin, Participant, Quiz,QuizShow, Question, QuestionShow
from fastapi import FastAPI, HTTPException
from db import _setup, models
from utilities import is_email_taken
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(_setup.engine)

@app.get('/')
async def root():
    return {"Data":['data1', 'data2']}

@app.post("/admins", tags=['Admin'])
async def create_admin(admin: Admin, session:Session = Depends(_setup.get_db)):    
    if is_email_taken(admin.email, models.Admin, session):
        raise HTTPException(status_code=400, detail="Email is already taken")    
    new_admin = models.Admin(email = admin.email,_password = admin.password)
    session.add(new_admin)
    session.commit()
    session.refresh(new_admin)
    return new_admin

@app.get('/admins/{id}',  tags=['Admin'])
async def get_admins(id:int,  session:Session = Depends(_setup.get_db)):
    admin = session.query(models.Admin).filter(models.Admin.admin_id == id).first()
    if admin : return admin
    else:raise HTTPException(status_code = 404, detail = "ID does not exist")
 
@app.post("/participants", tags=['Participant'])
async def create_participant(participant: Participant, session:Session = Depends(_setup.get_db)):    
    if is_email_taken(participant.email, models.Participant, session):
        raise HTTPException(status_code=400, detail="Email is already taken")    
    new_participant = models.Participant(email = participant.email,_password = participant.password)
    session.add(new_participant)
    session.commit()
    session.refresh(new_participant)
    return new_participant

@app.get('/participants', tags=['Participant'])
async def get_participants(id:int, response_model=List[Participant], session:Session = Depends(_setup.get_db)):
    participants = session.query(models.Participant).all()
    if not participants : 
        raise HTTPException(status_code = 404, detail = "ID does not exist")
    return participants

@app.get('/participants/{id}',  tags=['Participant'])
async def get_participants(id:int,  session:Session = Depends(_setup.get_db)):
    participant = session.query(models.Participant).filter(models.Participant.id == id).first()
    if not participant : 
        raise HTTPException(status_code = 404, detail = "ID does not exist")
    return participant


@app.post('/admins/{id}/quizzes', tags=['Admin'])
async def create_quiz(id:int, quiz:Quiz, session:Session = Depends(_setup.get_db)):
    new_quiz = models.Quiz(title = quiz.title, description = quiz.description, admin_id = id)
    session.add(new_quiz)
    session.commit()
    session.refresh(new_quiz)
@app.get('/admins/{admin_id}/quizzes/{quiz_id}',response_model=QuizShow)
async def update_quize(admin_id:int, quiz_id:int, quiz: Quiz, session:Session = Depends(_setup.get_db)):
    get_quiz = session.query(Quiz).filter(Quiz.quiz_id == quiz_id and Quiz.admin_id == admin_id).first()
    if not get_quiz:
        raise HTTPException(status_code = 404, detail = "ID does not exist")
    return get_quiz

@app.put('/admins/{admin_id}/quizzes/{quiz_id}',response_model=QuizShow)
async def update_quize(admin_id:int, quiz_id:int, quiz: Quiz, session:Session = Depends(_setup.get_db)):
    update_quiz = session.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
    if update_quiz:
        for field, value in quiz.dict().items():
            setattr(update_quiz, field, value)
        session.commit()
        session.refresh(update_quiz)
    return update_quiz
@app.delete("/quizzes/{quiz_id}")
def delete_quiz(quiz_id: int, session: Session = Depends(_setup.get_db)):    
    quiz = session.query(Quiz).filter(Quiz.id == quiz_id).first()
    if quiz:
        session.delete(quiz)
        session.commit()
        return {"message": f"Deleted Quiz: ID {quiz_id}"}
    raise HTTPException(status_code=404, detail=f"Quiz with ID {quiz_id} not found.")

@app.post("/quizzes/{quiz_id}/question")
async def create_question(quiz_id:int, question:Question, session:Session = Depends(_setup.get_db)):
    new_question = models.Question(**question.dict(),quiz_id=quiz_id)

@app.get("/quizzes/{quiz_id}/question")
async def create_question(quiz_id:int, question:Question,
                          response_model=List[QuestionShow], session:Session = Depends(_setup.get_db)):
    quiz_question_list = session.query(Question).all()
    return quiz_question_list

@app.get("/question")
async def get_all_questions(response_model=List[QuestionShow], 
                            session:Session=Depends(_setup.get_db)):
    all_question = session.query(Question).all()
    return all_question
 
@app.delete("/question/{question_id}")
def delete_quiz(question_id: int, session: Session = Depends(_setup.get_db)):    
    question = session.query(Question).filter(Quiz.id == question_id).first()
    if question:
        session.delete(question)
        session.commit()
        return {"message": f"Deleted Quiz: ID {question_id}"}
    raise HTTPException(status_code=404, detail=f"Quiz with ID {question_id} not found.")


# Take Quiz: : POST /participants/{participant_id}/quizzes/{quiz_id}/take
# Get Quiz Scores for Participant: : GET /participants/{participant_id}/scores
# Get Quiz Scores: : GET /quizzes/{quiz_id}/scores
# Submit Quiz Answers: : POST /quizzes/{quiz_id}/submit