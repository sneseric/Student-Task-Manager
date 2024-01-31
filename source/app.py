from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

class ToDoList:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="password",
            database="py_todo_db"
        )
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS py_todo_items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                task VARCHAR(255),
                due_date DATE
            )
        """
        self.cursor.execute(create_table_query)
        self.conn.commit()

    def add_task(self, task, due_date):
        insert_query = "INSERT INTO py_todo_items (task, due_date) VALUES (%s, %s)"
        self.cursor.execute(insert_query, (task, due_date))
        self.conn.commit()

    def delete_task(self, index):
        select_query = "SELECT id FROM py_todo_items"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()

        if 0 <= index < len(rows):
            task_id = rows[index][0]
            delete_query = "DELETE FROM py_todo_items WHERE id = %s"
            self.cursor.execute(delete_query, (task_id,))
            self.conn.commit()
        else:
            print("Invalid task number.")

    def view_tasks(self):
        select_query = "SELECT task, due_date FROM py_todo_items ORDER BY due_date ASC"
        self.cursor.execute(select_query)
        tasks = self.cursor.fetchall()
        return tasks

    def close_connection(self):
        self.conn.close()

to_do_list = ToDoList()

@app.route('/')
def index():
    tasks = to_do_list.view_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add_task', methods=['POST'])
def add_task():
    task_to_add = request.form.get('task')
    due_date = request.form.get('due_date')
    to_do_list.add_task(task_to_add, due_date)
    return redirect(url_for('index'))

@app.route('/delete_task', methods=['POST'])
def delete_task():
    task_index_to_delete = int(request.form.get('task_index'))
    to_do_list.delete_task(task_index_to_delete - 1)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
