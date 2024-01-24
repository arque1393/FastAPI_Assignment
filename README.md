## Problem Statement 

FastAPI Simple Quiz API  <br>
In this FastAPI assignment, you'll be creating simple quiz APIs.  <br>
Create 2-3 quizzes, each with three multiple-choice questions.  <br>
Each question should have a statement and a list of options (A, B, C, D, etc.).  <br>
Store quiz data in Postgres DB  <br>
API Endpoints (Below are just examples you should be creating your own as per best practices):  <br>
GET /quizzes: Retrieve a specific quiz. Return the quiz questions and options.  <br>
POST /submit: Allow users to submit their quiz answers. Should include the user's answers.  <br>
GET /result: Return the quiz result for a specific quiz, showing the user's score and the correct answers.  <br>
Validation and Error Handling:  <br>
Validate user input to ensure they select valid options.  <br>
Handle errors gracefully and provide meaningful error messages in the API responses.  <br>

Evaluation Criteria  <br>
1 point for creating the server with FastAPI   <br>
1 point for creating the routes (total 3 points)   <br>
2 points for Database connection  <br>
2 points for validation and error handling  <br>
2 points for code cleanliness and best practices  <br>

## Solution Approach 

#### User Type: 
1. Participant 
2. Admin 

#### Participant Properties 
1. email 
2. full name
3. 

