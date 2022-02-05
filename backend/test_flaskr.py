import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = "postgres://{}:{}@{}/{}".format(
  'postgres', 'postgres', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_questions_endpoint(self):
        res = self.client().get('/questions?page=1')
        data = res.get_json()

        total_questions_count = len(Question.query.all())

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['total_questions'], total_questions_count)
        self.assertTrue(data['questions'])
        self.assertEqual(data['categories']['2'], 'Art')

    def test_get_questions_per_specific_category(self):
        res = self.client().get('/categories/2/questions')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['total_questions'], 4)
        self.assertEqual(data['current_category'], 2)
        self.assertTrue(data['questions'])

    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])
        self.assertEqual(data['categories']['3'], 'Geography')

    def test_create_new_question(self):

        new_question = {
            "question": "The Big Apple is in which state?",
            "answer": "New York",
            "difficulty": 1,
            "category": 3
        }

        total_questions_before = len(Question.query.filter(Question.category == 3).all())

        res = self.client().post('/questions', json=new_question)
        data = res.get_json()

        total_questions_after = len(Question.query.filter(Question.category == 3).all())

        self.assertEqual(res.status_code, 200)
        self.assertEqual(total_questions_before+1, total_questions_after)
        self.assertEqual(data['success'], True)

    def test_delete_question(self):

        question_before = Question.query.filter(Question.id == 4).one_or_none()
        self.assertTrue(question_before)

        res = self.client().delete('/questions/4')
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

        question_after = Question.query.filter(Question.id == 4).one_or_none()
        self.assertFalse(question_after)

    def test_search_title(self):
        res = self.client().post('/questions', json={"searchTerm": "title"})
        data = res.get_json()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(len(data['questions']), 2)

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()