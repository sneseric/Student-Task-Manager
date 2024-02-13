from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import date, timedelta
import requests

app = Flask(__name__)
CORS(app)


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
        select_query = "SELECT id, task FROM py_todo_items"
        self.cursor.execute(select_query)
        rows = self.cursor.fetchall()

        if 0 <= index < len(rows):
            task_id, task_name = rows[index]

            # Delete the task from py_todo_items
            delete_query = "DELETE FROM py_todo_items WHERE id = %s"
            self.cursor.execute(delete_query, (task_id,))
            self.conn.commit()

            # Update task completion date in task_statistics
            update_query = "UPDATE task_statistics SET date_completed = CURDATE() WHERE task = %s"
            self.cursor.execute(update_query, (task_name,))
            self.conn.commit()
        else:
            print("Invalid task number.")

    def view_tasks(self):
        select_query = "SELECT task, due_date FROM py_todo_items ORDER BY due_date ASC"
        self.cursor.execute(select_query)
        tasks = self.cursor.fetchall()
        return tasks

    def count_completed_tasks(self, days):
        query = "SELECT COUNT(*) FROM task_statistics WHERE date_completed >= %s"
        date_threshold = date.today() - timedelta(days=days)
        self.cursor.execute(query, (date_threshold,))
        count = self.cursor.fetchone()[0]
        return count

    def count_total_tasks(self):
        query = "SELECT COUNT(*) FROM py_todo_items"
        self.cursor.execute(query)
        count = self.cursor.fetchone()[0]
        return count

    def close_connection(self):
        self.conn.close()


to_do_list = ToDoList()


@app.route('/')
def index():
    tasks = to_do_list.view_tasks()

    # Fetch task statistics
    stats_response = requests.get('http://127.0.0.1:5000/get_task_statistics')
    if stats_response.status_code == 200:
        stats = stats_response.json()
    else:
        stats = None

    return render_template('index.html', tasks=tasks, stats=stats)



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


@app.route('/toggle_notification', methods=['POST'])
def toggle_notification():
    data = request.get_json()
    new_status = 1 if data['status'] else 0

    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="password", database="py_todo_db")
    cursor = conn.cursor()
    cursor.execute("UPDATE notification_status SET `on` = %s, `off` = %s;", (new_status, 1 - new_status))
    conn.commit()
    cursor.close()
    conn.close()
    return jsonify({'success': True})


@app.route('/get_notification_status')
def get_notification_status():
    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="password", database="py_todo_db")
    cursor = conn.cursor()
    cursor.execute("SELECT `on` FROM notification_status;")
    status = cursor.fetchone()[0]
    cursor.close()
    conn.close()
    return jsonify({'status': status})


@app.route('/due_tasks')
def due_tasks():
    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="password", database="py_todo_db")
    cursor = conn.cursor()
    cursor.execute("SELECT `on` FROM notification_status;")
    notify_status = cursor.fetchone()
    if notify_status and notify_status[0] == 1:
        today = date.today()
        tomorrow = today + timedelta(days=1)
        query = """
        SELECT task, due_date FROM py_todo_items
        WHERE due_date BETWEEN %s AND %s
        ORDER BY due_date ASC;
        """
        cursor.execute(query, (today, tomorrow))
        tasks = cursor.fetchall()
        # Format tasks for JSON response
        tasks_formatted = [{'task': task[0], 'due_date': task[1].strftime('%Y-%m-%d')} for task in tasks]
        cursor.close()
        conn.close()
        return jsonify(tasks_formatted)
    else:
        cursor.close()
        conn.close()
        return jsonify([])


@app.route('/get_task_statistics')
def get_task_statistics():
    conn = mysql.connector.connect(host="127.0.0.1", user="root", password="password", database="py_todo_db")
    cursor = conn.cursor()

    # Get counts of completed tasks in the last week and last month
    completed_last_week = to_do_list.count_completed_tasks(7)
    completed_last_month = to_do_list.count_completed_tasks(30)

    # Get total tasks in the to-do list
    total_tasks = to_do_list.count_total_tasks()

    # Calculate completion percentages
    if total_tasks > 0:
        completion_percentage_week = (completed_last_week / total_tasks) * 100
        completion_percentage_month = (completed_last_month / total_tasks) * 100
    else:
        completion_percentage_week = 0
        completion_percentage_month = 0

    cursor.close()
    conn.close()

    return jsonify({
        'completed_last_week': completed_last_week,
        'completed_last_month': completed_last_month,
        'completion_percentage_week': completion_percentage_week,
        'completion_percentage_month': completion_percentage_month
    })


if __name__ == "__main__":
    app.run(debug=True)

