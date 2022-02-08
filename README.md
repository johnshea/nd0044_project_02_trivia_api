# Trivia API

This is the second project in Udacity's Full Stack Web Developer Nanodegree Program.

This project was to create, test, and document the required Trivia API endpoints to work with the Udacity provided frontend.

This project requires a working PostgreSQL server.

## Project Setup
Clone the project repository.
```bash
$ git clone https://github.com/johnshea/nd0044_project_02_trivia_api.git
```
# Database Setup
Change into the project's `backend` directory.
```bash
$ cd backend
```
Log in to the PostgreSQL server.
```bash
$ psql postgres
```
Run the `setup.sql` script.

This script will create the production (`trivia`) and testing (`trivia_test`) databases. It will also create a user `student` with a password of `student`.
```
\i setup.sql
```
Exit the PostgreSQL server.
```
\q
```
Load initial data in to the production (`trivia`) and testing (`trivia_test`) databases.
```
$ psql trivia < trivia.psql -U student
$ psql trivia_test < trivia.psql -U student
```

# Backend Setup
Change into the project's `backend` directory.
```bash
$ cd backend
```
Create a virtual environment.
```bash
$ python3 -m venv venv
```
Activate the virtual environment.
```bash
$ source venv/bin/activate
```
Install the required project dependencies.
```bash
$ pip install -r requirements.txt
```
Define the user and password that the flask script will use.
```bash
$ export FLASK_DB_USER=postgres
$ export FLASK_DB_USER_PASSWORD=postgres
```
Define the flask environment variables.
```bash
$ export FLASK_APP=flaskr
$ export FLASK_ENV=development
```
Run the flask server.
```bash
$ flask run
```
#
_NOTE_: When finished, to exit the virtual environment run:
```bash
$ deactivate
```

# Testing the Backend API Code
Define the user and password that the testing script will use.
```bash
$ export FLASK_DB_USER=postgres
$ export FLASK_DB_USER_PASSWORD=postgres
```
Change into the `backend` directory.
```bash
$ cd backend
```
Drop and create the `trivia_test` database.
```bash
$ dropdb trivia_test -U student
$ createdb trivia_test -U student
```
Populate the `trivia_test` database with the required testing data.
```bash
$ psql trivia_test < trivia.psql -U student
```
Run the testing script.
```bash
$ python3 test_flaskr.py
```

# Frontend Setup
NOTE - The frontend application requires `node` and `npm`. Please install these if they are not already installed on your system.
Change into the project's `frontend` directory.
```bash
$ cd frontend
```
Install the necessary dependencies.
```bash
$ npm install
```
Run the frontend application.
```bash
$ npm run start
```
Open your browser and navigate to http://localhost:3000


## API Documentation

The "Trivia API" endpoints are built using REST architecture.

The responses are JSON encoded with the traditional HTTP status codes.

Standard HTTP verbs (GET, POST, DELETE) are used.

## Authentication

No authentication is used nor needed.

## CORS
The API endpoints allow CORS requests from all origins.

## Errors
Errors are returned as JSON objects in the following format:
```
{
    "success": false,
    "error": 404,
    "message": "Not Found"
}
```
200 - OK  Successful request
400 - Bad Request
404 - Not Found
422 - Unprocessable Entity
500 - Internal Server Error

## Questions
This object represents a question in the Trivia game.

The question object

Attributes
id: int required
Unique identifier for this object.

question: string required
The text of the question.

answer: string required
The text answer for this question.

category: int in test_flaskr - string required (db is int, model is string????)
The category id (int) for this question.

difficulty: int required
The difficulty rating of this question. A value between 1 and 5 inclusive.



## Categories
This object represents a category.
Questions are required to have only one category assigned to them.

The category object
Attributes
id: int required
Unique identifier for this object

type: string required
Text description of the category

### GET `/categories`

Returns a list of all categories ordered by their id in ascending order.

Example request
`$ curl -X GET  http://127.0.0.1:5000/categories`

Example response
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}
```

### GET `/questions`

Returns a list of question objects, list of category objects, total numbers of questions, and the current category id.

Supports pagination with query parameter `page`.

If the page argument is less than or equal to zero, an error code of `400` is returned.

If the page argument exceeds the maximum page number based on questions per page, an error code of `404` is returned.

Example request
`curl -X GET  http://127.0.0.1:5000/questions?page=1`

Example response
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "current_category": 1, 
  "questions": [
    {
      "answer": "Apollo 13", 
      "category": 5, 
      "difficulty": 4, 
      "id": 2, 
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    }, 
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }, 
    {
      "answer": "Muhammad Ali", 
      "category": 4, 
      "difficulty": 1, 
      "id": 9, 
      "question": "What boxer's original name is Cassius Clay?"
    }, 
    {
      "answer": "Brazil", 
      "category": 6, 
      "difficulty": 3, 
      "id": 10, 
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    }, 
    {
      "answer": "Uruguay", 
      "category": 6, 
      "difficulty": 4, 
      "id": 11, 
      "question": "Which country won the first ever soccer World Cup in 1930?"
    }, 
    {
      "answer": "George Washington Carver", 
      "category": 4, 
      "difficulty": 2, 
      "id": 12, 
      "question": "Who invented Peanut Butter?"
    }, 
    {
      "answer": "Lake Victoria", 
      "category": 3, 
      "difficulty": 2, 
      "id": 13, 
      "question": "What is the largest lake in Africa?"
    }, 
    {
      "answer": "The Palace of Versailles", 
      "category": 3, 
      "difficulty": 3, 
      "id": 14, 
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }, 
    {
      "answer": "Agra", 
      "category": 3, 
      "difficulty": 2, 
      "id": 15, 
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ], 
  "total_questions": 19
}
```

### DELETE `/questions/<int:question_id>`

Delete a question by its id.

If the question id does not exist, an error code of `400` is returned.

Example request
`curl -X DELETE http://127.0.0.1:5000/questions/2`

Example response
```
{
  "success": true
}
```

### POST `/questions`

This endpoint is capable of either creating a new question or searching questions for a given search term.

If the body is empty, an error code of `400` is returned.

If the request body contains `searchTerm`, a search of the property `question` will be performed and it will return questions where the searchTerm exists.

If the request body does not contain `searchTerm` it will attempt to create a new question.

When creating a new question, if any of the required fields are not provided (question, answer, category, difficulty), an error code of `400` is returned.

Example request - search
`curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"searchTerm": "title"}'`

Example response - search
```
{
  "current_category": 1, 
  "questions": [
    {
      "answer": "Maya Angelou", 
      "category": 4, 
      "difficulty": 2, 
      "id": 5, 
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }, 
    {
      "answer": "Edward Scissorhands", 
      "category": 5, 
      "difficulty": 3, 
      "id": 6, 
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ], 
  "success": true, 
  "total_questions": 2
}
```

Example request - create new question
`curl -X POST http://127.0.0.1:5000/questions -H "Content-Type: application/json" -d '{"question": "The Big Apple is in which state?", "answer": "New York", "difficulty": 1, "category": 3}'
`

Example response - create new question
```
{
  "success": true
}
```

### GET `/categories/<int:category_id>/questions`

Returns a list of questions for a specified category.

If the provided category id does not exist, an error code of `400` is returned.

Example request
`curl -X GET  http://127.0.0.1:5000/categories/2/questions`

Example response
```
{
  "current_category": 2, 
  "questions": [
    {
      "answer": "Escher", 
      "category": 2, 
      "difficulty": 1, 
      "id": 16, 
      "question": "Which Dutch graphic artist\u2013initials M C was a creator of optical illusions?"
    }, 
    {
      "answer": "Mona Lisa", 
      "category": 2, 
      "difficulty": 3, 
      "id": 17, 
      "question": "La Giaconda is better known as what?"
    }, 
    {
      "answer": "One", 
      "category": 2, 
      "difficulty": 4, 
      "id": 18, 
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    }, 
    {
      "answer": "Jackson Pollock", 
      "category": 2, 
      "difficulty": 2, 
      "id": 19, 
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ], 
  "total_questions": 4
}
```

### POST `/quizzes`

Returns a random question within the given category, if provided, and that is not one of the previous questions.

If the body is empty, an error code of `400` is returned.

If no questions are found `None` is returned for the `question` field in the response.

If the previous quesitons parameter is not supplied, an error code of `400` is returned.

Example request
`curl -X POST http://127.0.0.1:5000/quizzes -H "Content-Type: application/json" -d '{"previous_questions": [5, 9],"quiz_category": {"type": "History", "id": "4"}}'
`

Example response
```
{
  "question": {
    "answer": "George Washington Carver", 
    "category": 4, 
    "difficulty": 2, 
    "id": 12, 
    "question": "Who invented Peanut Butter?"
  }, 
  "success": true
}
```
