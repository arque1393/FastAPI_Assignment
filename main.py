from fastapi import FastAPI
from _models import Admin 
from fastapi import FastAPI, HTTPException
from db import _setup, models
from utilities import is_username_taken,is_email_taken

app = FastAPI()

models.Base.metadata.create_all(_setup.engine)


@app.get('/')
async def root():
    return {"Data":['data1', 'data2']}

admins = []
@app.post("/admins")
async def create_admin(admin: Admin):    
    if is_username_taken(admin.username):
        raise HTTPException(status_code=400, detail="Username is already taken")
    if is_email_taken(admin.email):
        raise HTTPException(status_code=400, detail="Email is already taken")
    ## 
    admins.append(admin)
    # TODO 
    created_admin = {"username": admin.username, "email": admin.email}
    return created_admin

@app.get('/admins/{id}')
async def get_admins(id:int):
    return admins[id].dict()


# Get Admin Profile: : GET /admins/{admin_id}
# Create Quiz: POST /quizzes
# Update Quiz: : PUT /quizzes/{quiz_id}
# Delete Quiz: : DELETE /quizzes/{quiz_id}
# Add Question to Quiz: : POST /quizzes/{quiz_id}/questions
# Remove Question from Quiz: : DELETE /quizzes/{quiz_id}/questions/{question_id}