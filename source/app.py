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

    def total_tasks(self):
        query = "SELECT MAX(id) FROM task_statistics"
        self.cursor.execute(query)
        total = self.cursor.fetchone()[0]
        print("Total tasks:", total)
        return total

    def total_completed_tasks_week(self):
        today = date.today()
        week_ago = today - timedelta(days=7)
        query = "SELECT COUNT(*) FROM task_statistics WHERE date_completed IS NOT NULL AND DATEDIFF(%s, date_completed) <= 7"
        self.cursor.execute(query, (today,))
        total_completed_week = self.cursor.fetchone()[0]
        print("Total completed tasks in the last week:", total_completed_week)
        return total_completed_week

    def total_completed_tasks_week_percentage(self):
        total_tasks = self.total_tasks()
        total_completed_tasks_week = self.total_completed_tasks_week()
        percentage = (total_completed_tasks_week / total_tasks) * 100
        print("Percentage of completed tasks in the last week:", "{:.2f}%".format(percentage))
        return percentage

    def total_completed_tasks_month(self):
        today = date.today()
        month_ago = today - timedelta(days=30)
        query = "SELECT COUNT(*) FROM task_statistics WHERE date_completed IS NOT NULL AND DATEDIFF(%s, date_completed) <= 30"
        self.cursor.execute(query, (today,))
        total_completed_month = self.cursor.fetchone()[0]
        print("Total completed tasks in the last month:", total_completed_month)
        return total_completed_month

    def total_completed_tasks_month_percentage(self):
        total_tasks = self.total_tasks()
        total_completed_tasks_month = self.total_completed_tasks_month()
        percentage = (total_completed_tasks_month / total_tasks) * 100
        print("Percentage of completed tasks in the last month:", "{:.2f}%".format(percentage))
        return percentage

    def average_completion_time(self):
        query = "SELECT ROUND(AVG(DATEDIFF(date_completed, date_added)), 2) FROM task_statistics WHERE date_completed IS NOT NULL"
        self.cursor.execute(query)
        average_time = self.cursor.fetchone()[0]
        print("Average completion time:", "{:.2f}".format(average_time), "days")
        return average_time

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





if __name__ == "__main__":
    total_tasks = to_do_list.total_tasks()
    total_completed_tasks_week = to_do_list.total_completed_tasks_week()
    total_completed_tasks_week_percentage = to_do_list.total_completed_tasks_week_percentage()
    total_completed_tasks_month = to_do_list.total_completed_tasks_month()
    total_completed_tasks_month_percentage = to_do_list.total_completed_tasks_month_percentage()
    average_completion_time = to_do_list.average_completion_time()
    app.run(debug=True)


