from fastapi import FastAPI, Depends
from _models import Admin, Participant, Quiz
from fastapi import FastAPI, HTTPException
from db import _setup, models
from utilities import is_email_taken
from sqlalchemy.orm import Session

app = FastAPI()
models.Base.metadata.create_all(_setup.engine)

@app.get('/')
async def root():
    return {"Data":['data1', 'data2']}

@app.post("/admins")
async def create_admin(admin: Admin, session:Session = Depends(_setup.get_db)):    
    if is_email_taken(admin.email, models.Admin, session):
        raise HTTPException(status_code=400, detail="Email is already taken")    
    new_admin = models.Admin(email = admin.email,_password = admin.password)
    session.add(new_admin)
    session.commit()
    session.refresh(new_admin)
    return new_admin

@app.get('/admins/{id}')
async def get_admins(id:int,  session:Session = Depends(_setup.get_db)):
    admin = session.query(models.Admin).filter(models.Admin.admin_id == id).first()
    if admin : return admin
    else:raise HTTPException(status_code = 404, detail = "ID does not exist")
 
@app.post("/participants")
async def create_participant(participant: Participant, session:Session = Depends(_setup.get_db)):    
    if is_email_taken(participant.email, models.Participant, session):
        raise HTTPException(status_code=400, detail="Email is already taken")    
    new_participant = models.Participant(email = participant.email,_password = participant.password)
    session.add(new_participant)
    session.commit()
    session.refresh(new_participant)
    return new_participant

@app.get('/participants/{id}')
async def get_participants(id:int,  session:Session = Depends(_setup.get_db)):
    participant = session.query(models.Participant).filter(models.Participant.id == id).first()
    if not participant : 
        raise HTTPException(status_code = 404, detail = "ID does not exist")
    return participant

@app.post('/admins/{id}/quizzes')
async def create_quiz(id:int, quiz:Quiz, session:Session = Depends(_setup.get_db)):
    new_quiz = models.Quiz(title = quiz.title, description = quiz.description, admin_id = id)
    session.add(new_quiz)
    session.commit()
    session.refresh(new_quiz)

# @app.get('/quizzes/{quiz_id}')
# async def update_quize(quiz_id:int, session:Depends(_setup.get_db)):
#     # update_quiz = session.query(Quiz).filter(Quiz.quiz_id == quiz_id).first()
#     # if update_quiz:
#     #     for field, value in quiz.dict().items():
#     #         setattr(update_quiz, field, value)
#     #     session.commit()
#     #     session.refresh(update_quiz)
#     # return update_quiz
#     return {}


# Update Quiz: : PUT /quizzes/{quiz_id}
# Delete Quiz: : DELETE /quizzes/{quiz_id}

# Add Question to Quiz: : POST /quizzes/{quiz_id}/questions
# Remove Question from Quiz: : DELETE /quizzes/{quiz_id}/questions/{question_id}