import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app, ToDoList

# 1. Test the add_task method in the ToDoList class.
# 2. Test the delete_task method in the ToDoList class.
# 3. Test the index route in Flask application.
class TestToDoList(unittest.TestCase):
    def setUp(self):
        self.app = app
        self.client = self.app.test_client()
        self.to_do_list = ToDoList()

    def test_add_task(self):
        initial_task_count = len(self.to_do_list.view_tasks())
        self.to_do_list.add_task('Test Task', '2023-12-31')
        final_task_count = len(self.to_do_list.view_tasks())
        self.assertEqual(final_task_count, initial_task_count + 1)
        print(f"Test add_task: initial={initial_task_count}, after adding task={final_task_count}")

    def test_delete_task(self):
        self.to_do_list.add_task('Test Task for Deletion', '2023-12-31')
        initial_task_count = len(self.to_do_list.view_tasks())
        self.to_do_list.delete_task(initial_task_count - 1)
        final_task_count = len(self.to_do_list.view_tasks())
        self.assertEqual(final_task_count, initial_task_count - 1)
        print(f"Test delete_task: initial={initial_task_count}, after deleting task={final_task_count}")

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        print(f"Test index_route: status code={response.status_code}")

if __name__ == '__main__':
    unittest.main()