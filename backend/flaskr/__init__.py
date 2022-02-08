import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random
import math

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10

def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__)
  setup_db(app)
  
  '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
  CORS(app)

  '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
  @app.after_request
  def after_request(response):
      response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
      response.headers.add('Access-Control-Allow-Methods', 'GET,POST,DELETE,OPTIONS')
      return response

  '''
  @TODO: 
  Create an endpoint to handle GET requests 
  for all available categories.
  '''
  @app.route('/categories', methods=['GET'])
  def all_categories():

    categories = Category.query.order_by(Category.id).all()
    categories_result = {}
    for cat in categories:
      categories_result[cat.id] = cat.type

    return jsonify({
      "success": True,
      "categories": categories_result
    })


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''
  @app.route('/questions', methods=['GET'])
  def get_questions():
    questions = Question.query.order_by(Question.id).all()
    formatted_questions = [question.format() for question in questions]

    categories = Category.query.order_by(Category.id).all()
    # formatted_categories = [{category.id: category.type} for category in categories]
    categories_result = {}
    for cat in categories:
      categories_result[cat.id] = cat.type

    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    if page <= 0:
      abort(400)

    if page > math.ceil(len(questions) / QUESTIONS_PER_PAGE):
      abort(404)
    
    return jsonify({
      "questions": formatted_questions[start:end],
      "total_questions": len(questions),
      "categories": categories_result,
      "current_category": 1
    })

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''
  @app.route('/questions/<int:question_id>', methods=['DELETE'])
  def delete_question(question_id):
    question_to_delete = Question.query.filter(Question.id == question_id).one_or_none()

    if not question_to_delete:
      abort(400)

    question_to_delete.delete()

    return jsonify({
      "success": True,
    })

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''
  @app.route('/questions', methods=['POST'])
  def create_new_question():
    data = request.get_json()

    if not data:
      abort(400)

    question = data.get('question', None)
    answer = data.get('answer', None)
    difficulty = data.get('difficulty', None)
    category = data.get('category', None)
    search_term = data.get('searchTerm', None)

    if search_term:
        questions = Question.query.filter(Question.question.ilike(f'%{search_term}%')).all()
        formatted_questions = [question.format() for question in questions]

        return jsonify({
          "success": True,
          "questions": formatted_questions,
          "total_questions": len(formatted_questions),
          "current_category": 1
        })

    else:
      if not question or not answer or not category or not difficulty:
        abort(400)
      
      new_question = Question(question, answer, category, difficulty)
      new_question.insert()

      return jsonify({
        "success": True
      })


  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
  @app.route('/categories/<int:category_id>/questions', methods=['GET'])
  def get_questions_by_category_id(category_id):

    category = Category.query.filter(Category.id == category_id).one_or_none()
    
    # Abort if provided category does not exist
    if not category:
      abort(400)
    
    questions = Question.query.filter(Question.category == category_id).all()
    formatted_questions = [question.format() for question in questions]

    return jsonify({
      "questions": formatted_questions,
      "total_questions": len(formatted_questions),
      "current_category": category_id
    })

  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''
  @app.route('/quizzes', methods=['POST'])
  def create_quizzes():
    data = request.get_json()

    if not data:
      abort(400)

    # Abort if required parameter is not provided
    if "previous_questions" not in data:
      abort(400)

    previous_questions = data.get('previous_questions')

    quiz_category = data.get('quiz_category', None)

    if quiz_category:
        category_id = int(quiz_category['id'])
        questions = Question.query.filter(Question.category == category_id).filter(Question.id.notin_(previous_questions)).order_by(Question.id).all()
    else:
        questions = Question.query.filter(Question.id.notin_(previous_questions)).order_by(Question.id).all()

    if questions:
        question = random.choice(questions)

        return jsonify({
          "success": True,
          "question": question.format()
        })
    else:
        return jsonify({
          "success": True,
          "question": None
        })


  '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  '''
  @app.errorhandler(400)
  def bad_request(error):
    return jsonify({
      "success": False,
      "message": "Bad Request",
      "error": 400
    }), 400

  @app.errorhandler(404)
  def not_found(error):
    return jsonify({
      "success": False,
      "message": "Not Found",
      "error": 404
    }), 404

  @app.errorhandler(422)
  def unprocessable_entity(error):
    return jsonify({
      "success": False,
      "message": "Unprocessable Entity",
      "error": 422
    }), 422

  @app.errorhandler(500)
  def internal_server_error(error):
    return jsonify({
      "success": False,
      "message": "Internal Server Error",
      "error": 500
    }), 500

  return app

    