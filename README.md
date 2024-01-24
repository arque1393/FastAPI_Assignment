# Problem Statement 

FastAPI Simple Quiz API  <br>
In this FastAPI assignment, you'll be creating simple quiz APIs.  <br>
Create 2-3 quizzes, each with three multiple-choice questions.  <br>
Each question should have a statement and a list of options (A, B, C, D, etc.).  <br>
Store quiz data in Postgres DB  <br>
API Endpoints (Below are just examples you should be creating your own as per best practices)** :  <br>
GET /quizzes** : Retrieve a specific quiz. Return the quiz questions and options.  <br>
POST /submit** : Allow users to submit their quiz answers. Should include the user's answers.  <br>
GET /result** : Return the quiz result for a specific quiz, showing the user's score and the correct answers.  <br>
Validation and Error Handling** :  <br>
Validate user input to ensure they select valid options.  <br>
Handle errors gracefully and provide meaningful error messages in the API responses.  <br>

Evaluation Criteria  <br>
1 point for creating the server with FastAPI   <br>
1 point for creating the routes (total 3 points)   <br>
2 points for Database connection  <br>
2 points for validation and error handling  <br>
2 points for code cleanliness and best practices  <br>

# Solution Approach 
## Designing Database Model 

### Admin
1. can create new quize 
2. add or remove questions in a quize 
3. change value of each question

**admin_id** : Primary key for the admin table.<br>
**username** : Admin's username for login.<br>
**password_hash** : Hashed password for security.<br>
**email** : Admin's email address.<br>


### Quize
**quiz_id** : Primary key for the quiz table. <br>
**admin_id** : Foreign key referencing the admin who created the quiz. <br>
**title** : Title of the quiz. <br>
**description** : Description of the quiz. <br>
**created_at** : Timestamp indicating when the quiz was created. <br>

### Question Table
**question_id** : Primary key for the question table. <br>
**quiz_id** : Foreign key referencing the quiz to which the question belongs. <br>
**text** : The text of the question. <br>
**option1, option2, option3, option4** : Multiple choice options. <br>
**correct_option** : The correct option among the choices. <br>

### Participant
**participant_id** : Primary key for the participant table. <br>
**username** : Participant's username for login. <br>
**password_hash** : Hashed password for security. <br>
**email** : Participant's email address. <br>

### Score
**score_id** : Primary key for the score table. <br>
**participant_id** : Foreign key referencing the participant who played the quiz. <br>
**quiz_id** : Foreign key referencing the quiz for which the score is recorded. <br>
**score** : The score obtained by the participant in the quiz. <br>

### Relationship 
quiz (1) <--> (N) question      <br>
admin (1) <--> (N) quiz         <br>
participant (1) <--> (N) score  <br>
quiz (1) <--> (N) score         <br>

# End Points Design 

Certainly! To design the API endpoints for your quiz system, you can follow RESTful principles and create endpoints that allow interaction with the different resources in your system. Below are some suggested API endpoints:

1. **Admin Endpoints:**
   - **Create Admin:** : `POST /admins`

   - **Get Admin Profile:** : `GET /admins/{admin_id}`

   - **Create Quiz:**  `POST /quizzes`

   - **Get Quiz Details:** : `GET /quizzes/{quiz_id}`

   - **Update Quiz:** : `PUT /quizzes/{quiz_id}`

   - **Delete Quiz:** : `DELETE /quizzes/{quiz_id}`

   - **Add Question to Quiz:** : `POST /quizzes/{quiz_id}/questions`

   - **Remove Question from Quiz:** : `DELETE /quizzes/{quiz_id}/questions/{question_id}`

2. **Participant Endpoints:**
   - **Create Participant:** : `POST /participants`

   - **Get Participant Profile:** : `GET /participants/{participant_id}`

   - **Take Quiz:** : `POST /participants/{participant_id}/quizzes/{quiz_id}/take`

   - **Get Quiz Scores for Participant:** : `GET /participants/{participant_id}/scores`

3. **General Quiz Endpoints:**

   - **Get All Quizzes:** : `GET /quizzes`
      Valid for Both Admin and Participants

   - **Get Quiz Details:** : `GET /quizzes/{quiz_id}`
      Valid for Both Admin and Participants

   - **Get Quiz Questions:** : `GET /quizzes/{quiz_id}/questions`
      Valid for Both Admin and Participants
      
   - **Submit Quiz Answers:** : `POST /quizzes/{quiz_id}/submit`
      Valid for Participants

   - **Get Quiz Scores:** : `GET /quizzes/{quiz_id}/scores`
      Valid for Both Admin and Participants
