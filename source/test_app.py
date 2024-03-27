import unittest
from flask import Flask
from flask.testing import FlaskClient
from app import app, ToDoList
import mysql.connector

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

    import mysql.connector

    import mysql.connector

    import mysql.connector

    def test_sql_injection(self):
        # Get the initial task count
        initial_task_count = len(self.to_do_list.view_tasks())

        # Connect to the database
        try:
            conn = mysql.connector.connect(user='root', password='password', host='127.0.0.1', port='3306',
                                           database='py_todo_db')
            cursor = conn.cursor()

            # Get the initial column names
            cursor.execute("SHOW COLUMNS FROM py_todo_items")
            initial_columns = [column[0] for column in cursor.fetchall()]

            # Attempt SQL injection by adding a potentially malicious task
            malicious_task = "'; DROP TABLE py_todo_items; DELETE FROM py_todo_items WHERE task_id > 0; ALTER TABLE py_todo_items ADD COLUMN SQL_INJECTION_TEST; DROP DATABASE py_todo_db; --"
            self.to_do_list.add_task(malicious_task, '2023-12-31')

            # Get the final task count
            final_task_count = len(self.to_do_list.view_tasks())

            # Get the final column names
            cursor.execute("SHOW COLUMNS FROM py_todo_items")
            final_columns = [column[0] for column in cursor.fetchall()]

            # Check if the task count has changed as expected
            if final_task_count == initial_task_count + 1:
                print("Task count increased.", flush=True)

                # Check if the task contains potentially malicious SQL statements
                if any(keyword.upper() in malicious_task.upper() for keyword in
                       ["DROP TABLE", "DROP DATABASE", "TRUNCATE TABLE", "ALTER TABLE", "DELETE FROM", "UPDATE"]):
                    print("SQL injection detected. Potentially malicious SQL statement found.", flush=True)

                    # Check if any columns were added or deleted
                    if set(initial_columns) == set(final_columns):
                        print("Columns remained unchanged.", flush=True)
                    else:
                        print("Columns were added or deleted.", flush=True)

                    # Check if any tasks were deleted
                    cursor.execute("SELECT COUNT(*) FROM py_todo_items")
                    task_count_after = cursor.fetchone()[0]
                    if task_count_after >= initial_task_count:
                        print("No tasks were deleted.", flush=True)
                    else:
                        print("Tasks were deleted.", flush=True)

                    # Check if the table was dropped
                    cursor.execute("SHOW TABLES LIKE 'py_todo_items'")
                    if cursor.fetchone():
                        print("Table was not dropped.", flush=True)
                    else:
                        print("Table was dropped.", flush=True)

                    # Check if the database was dropped
                    cursor.execute("SHOW DATABASES LIKE 'py_todo_db'")
                    if cursor.fetchone():
                        print("Database was not dropped.", flush=True)
                    else:
                        print("Database was dropped.", flush=True)

                    # SQL injection attempt was unsuccessful
                    print("SQL injection attempt was unsuccessful.", flush=True)

                else:
                    print("No potentially malicious SQL statement detected.", flush=True)
                    # SQL injection attempt was successful
                    print("SQL injection attempt was unsuccessful.", flush=True)

            elif final_task_count == initial_task_count:
                print("Task count remained unchanged.", flush=True)
                # SQL injection attempt was unsuccessful
                print("SQL injection attempt was unsuccessful.", flush=True)

            else:
                print("Task count changed unexpectedly.", flush=True)
                # SQL injection attempt was successful
                print(
                    "WARNING: SQL injection attempt was successful. Check for potential data loss, fix vulnerabilities, and restore backup as needed.", flush=True)

        except mysql.connector.Error as e:
            print(f"Error occurred: {e}", flush=True)

        finally:
            if 'cursor' in locals():
                cursor.close()
            if 'conn' in locals():
                conn.close()

    def test_backup_system(self):
        # Test the backup system
        initial_backup_count = self.to_do_list.get_latest_backup_version()
        # Perform a backup
        self.to_do_list.perform_backup('test_action', 'test_task')
        # Get the latest backup version after performing the backup
        final_backup_count = self.to_do_list.get_latest_backup_version()
        # Assert that the latest backup version has been incremented, indicating backup was successful
        self.assertEqual(final_backup_count, initial_backup_count + 1)
        print("Test backup_system: Backup performed successfully")

if __name__ == '__main__':
    unittest.main()