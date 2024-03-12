from flask import Flask, render_template, request, redirect, url_for, jsonify, send_file
from flask_cors import CORS
import mysql.connector
from datetime import date, timedelta
from datetime import datetime
import subprocess
import requests
import matplotlib.pyplot as plt
import numpy as np
import os
from urllib.parse import quote

app = Flask(__name__)
CORS(app)

class ToDoList:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="password",
                database="py_todo_db"
            )
            self.cursor = self.conn.cursor()
            self.create_table()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def create_table(self):
        try:
            create_table_query = """
                CREATE TABLE IF NOT EXISTS py_todo_items (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    task VARCHAR(255),
                    due_date DATE
                )
            """
            self.cursor.execute(create_table_query)
            self.conn.commit()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def add_task(self, task, due_date):
        try:
            insert_query = "INSERT INTO py_todo_items (task, due_date) VALUES (%s, %s)"
            self.cursor.execute(insert_query, (task, due_date))
            self.conn.commit()
            # add database backup after adding a task
            self.perform_backup('add', task)  # Perform database backup after adding a task
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def delete_task(self, index):
        try:
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
                self.perform_backup('delete', task_name)  # Perform database backup after deleting a task
            else:
                print("Invalid task number.")
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def view_tasks(self):
        try:
            select_query = "SELECT task, due_date FROM py_todo_items ORDER BY due_date ASC"
            self.cursor.execute(select_query)
            tasks = self.cursor.fetchall()
            return tasks
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def total_tasks(self):
        try:
            query = "SELECT MAX(id) FROM task_statistics"
            self.cursor.execute(query)
            total = self.cursor.fetchone()[0]
            print("Total tasks:", total)
            return total
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def total_completed_tasks_week(self):
        try:
            today = date.today()
            week_ago = today - timedelta(days=7)
            query = "SELECT COUNT(*) FROM task_statistics WHERE date_completed IS NOT NULL AND DATEDIFF(%s, date_completed) <= 7"
            self.cursor.execute(query, (today,))
            total_completed_week = self.cursor.fetchone()[0]
            print("Total completed tasks in the last week:", total_completed_week)
            return total_completed_week
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def total_completed_tasks_week_percentage(self):
        try:
            total_tasks = self.total_tasks()
            total_completed_tasks_week = self.total_completed_tasks_week()
            percentage = (total_completed_tasks_week / total_tasks) * 100
            print("Percentage of completed tasks in the last week:", "{:.2f}%".format(percentage))
            return percentage
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def total_completed_tasks_month(self):
        try:
            today = date.today()
            month_ago = today - timedelta(days=30)
            query = "SELECT COUNT(*) FROM task_statistics WHERE date_completed IS NOT NULL AND DATEDIFF(%s, date_completed) <= 30"
            self.cursor.execute(query, (today,))
            total_completed_month = self.cursor.fetchone()[0]
            print("Total completed tasks in the last month:", total_completed_month)
            return total_completed_month
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def total_completed_tasks_month_percentage(self):
        try:
            total_tasks = self.total_tasks()
            total_completed_tasks_month = self.total_completed_tasks_month()
            percentage = (total_completed_tasks_month / total_tasks) * 100
            print("Percentage of completed tasks in the last month:", "{:.2f}%".format(percentage))
            return percentage
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def average_completion_time(self):
        try:
            query = "SELECT ROUND(AVG(DATEDIFF(date_completed, date_added)), 2) FROM task_statistics WHERE date_completed IS NOT NULL"
            self.cursor.execute(query)
            average_time = self.cursor.fetchone()[0]
            print("Average completion time:", "{:.2f}".format(average_time), "days")
            return average_time
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def generate_pie_chart(self):
        try:
            total_completed_tasks_week = self.total_completed_tasks_week()
            total_tasks = self.total_tasks()
            data = [total_completed_tasks_week, total_tasks - total_completed_tasks_week]
            labels = ['Completed', 'Pending']
            plt.figure(figsize=(8, 8), facecolor='#E4ECF0')
            plt.pie(data, labels=labels, autopct='%1.1f%%', textprops={'fontsize':17.5})
            plt.title('Total Tasks Completed in Last Month', fontsize=28)

            # Use os.path.join to create the image path
            image_path_pie = os.path.join('static', 'assets', 'pie_chart.png')
            plt.savefig(image_path_pie)
            plt.close()
            return image_path_pie
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def add_current_date(self, date):
        try:
            # Check if the date already exists
            select_query = "SELECT COUNT(*) FROM completion_time WHERE date = %s"
            self.cursor.execute(select_query, (date,))
            count = self.cursor.fetchone()[0]
            if count == 0:
                insert_query = "INSERT INTO completion_time (date) VALUES (%s)"
                self.cursor.execute(insert_query, (date,))
                self.conn.commit()
                print(f"Date {date} added successfully.")
            else:
                print(f"Date {date} already exists in the table.")
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def update_current_date(self):
        try:
            # Query to update NULL values in avg_completion_time column
            update_query = """
                UPDATE completion_time 
                SET avg_completion_time = (
                    SELECT ROUND(AVG(DATEDIFF(date_completed, date_added)), 2) 
                    FROM task_statistics 
                    WHERE date_completed IS NOT NULL
                ) 
                WHERE avg_completion_time IS NULL
            """
            self.cursor.execute(update_query)
            self.conn.commit()
            print("Average completion times updated.")
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def generate_trend_line_graph(self):
        try:
            # Fetch data from the completion_time table
            cursor = to_do_list.cursor
            cursor.execute("SELECT date, avg_completion_time FROM completion_time ORDER BY date")
            results = cursor.fetchall()
            dates = [result[0] for result in results]
            completion_times = [result[1] for result in results]

            # adjust size of the graph
            fig_width_px = 533
            fig_height_px = 400
            plt.figure(figsize=(fig_width_px / 100, fig_height_px / 100), dpi=100, facecolor='#E4ECF0')

            plt.axes().set_facecolor('#E4ECF0')  # Change background color of the graph

            # Formatting x-axis ticks to display only month and day
            plt.gca().xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%m-%d'))

            # Generate the trend line graph
            plt.plot(dates, completion_times, marker='o')
            plt.xlabel('Date')
            plt.ylabel('Average Completion Time (Days)')
            plt.title('Average Completion Time Trends', fontsize=14)

            # Set x-axis ticks to display at 7-day intervals
            plt.gca().xaxis.set_major_locator(plt.MultipleLocator(7))

            plt.xticks(rotation=45,
                       fontsize=10)  # Rotate x-axis ex: rotation=90 for labels vertically and change font-size

            # Use os.path.join to create the image path
            trend_line_graph_path = os.path.join('static', 'assets', 'trend_line_graph.png')
            plt.savefig(trend_line_graph_path)
            plt.close()
            return trend_line_graph_path
        except mysql.connector.Error as err:
            print("Error occurred:", err)

    def backup_database(self, version, action, task_name):
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        try:
            # Quote the task_name to handle special characters and spaces
            quoted_task_name = quote(task_name, safe='')
        except Exception as e:
            print(f"Error occurred while quoting task name: {e}")
            return
        backup_filename = f"db_backup/py_todo_db_{timestamp}_v{version}_{action}_{quoted_task_name}.sql"
        try:
            # Construct the mysqldump command
            command = f"mysqldump -u root -ppassword py_todo_db > {backup_filename}"
            subprocess.run(command, check=True, shell=True)
            print(f"Backup successful: {backup_filename}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred during backup: {e}")

    def get_latest_backup_version(self):
        # List all backup files in the db_backup directory
        backup_files = os.listdir('db_backup')
        # Extract version numbers from files
        versions = []
        for file in backup_files:
            if file.startswith('py_todo_db_'):
                try:
                    version = int(file.split('_v')[-1].split('_')[0])
                    versions.append(version)
                except ValueError:
                    print(f"Unexpected file format: {file}")
        # Return the highest version number
        return max(versions) if versions else 0

    def perform_backup(self, action, task_name):
        version = self.get_latest_backup_version() + 1
        self.backup_database(version, action, task_name)

    def close_connection(self):
        try:
            self.conn.close()
        except mysql.connector.Error as err:
            print("Error occurred:", err)

to_do_list = ToDoList()

@app.route('/')
def index():
    try:
        tasks = to_do_list.view_tasks()

        # Generate pie chart image
        pie_chart_image = to_do_list.generate_pie_chart()

        # add today's date to completion_time table
        today = date.today()
        to_do_list.add_current_date(today)

        # Update average completion times
        to_do_list.update_current_date()

        # Generate trend line graph image
        trend_line_graph_path = to_do_list.generate_trend_line_graph()

        # Fetch task statistics
        stats_response = requests.get('http://127.0.0.1:5000/get_task_statistics')
        if stats_response.status_code == 200:
            stats = stats_response.json()
        else:
            stats = None
        return render_template('index.html', tasks=tasks, stats=stats, pie_chart_image=pie_chart_image, trend_line_graph_path=trend_line_graph_path)
    except Exception as e:
        print(f"Error occurred while loading index page: {e}")
        return jsonify({'error': 'An error occurred while loading index page'}), 500


@app.route('/add_task', methods=['POST'])
def add_task():
    try:
        task_to_add = request.form.get('task')
        due_date = request.form.get('due_date')
        to_do_list.add_task(task_to_add, due_date)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error occurred while adding task: {e}")
        return jsonify({'error': 'An error occurred while adding task'}), 500


@app.route('/delete_task', methods=['POST'])
def delete_task():
    try:
        task_index_to_delete = int(request.form.get('task_index'))
        to_do_list.delete_task(task_index_to_delete - 1)
        return redirect(url_for('index'))
    except Exception as e:
        print(f"Error occurred while deleting task: {e}")
        return jsonify({'error': 'An error occurred while deleting task'}), 500


@app.route('/toggle_notification', methods=['POST'])
def toggle_notification():
    try:
        data = request.get_json()
        new_status = 1 if data['status'] else 0

        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="password", database="py_todo_db")
        cursor = conn.cursor()
        cursor.execute("UPDATE notification_status SET `on` = %s, `off` = %s;", (new_status, 1 - new_status))
        conn.commit()
        cursor.close()
        conn.close()
        return jsonify({'success': True})
    except Exception as e:
        print(f"Error occurred while toggling notification: {e}")
        return jsonify({'error': 'An error occurred while toggling notification'}), 500


@app.route('/get_notification_status')
def get_notification_status():
    try:
        conn = mysql.connector.connect(host="127.0.0.1", user="root", password="password", database="py_todo_db")
        cursor = conn.cursor()
        cursor.execute("SELECT `on` FROM notification_status;")
        status = cursor.fetchone()[0]
        cursor.close()
        conn.close()
        return jsonify({'status': status})
    except Exception as e:
        print(f"Error occurred while getting notification status: {e}")
        return jsonify({'error': 'An error occurred while getting notification status'}), 500


@app.route('/due_tasks')
def due_tasks():
    try:
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
    except Exception as e:
        print(f"Error occurred while getting due tasks: {e}")
        return jsonify({'error': 'An error occurred while getting due tasks'}), 500

@app.route('/get_task_statistics')
def get_task_statistics():
    try:
        total_tasks = to_do_list.total_tasks()
        total_completed_tasks_week = to_do_list.total_completed_tasks_week()
        total_completed_tasks_month = to_do_list.total_completed_tasks_month()
        total_completed_tasks_week_percentage = to_do_list.total_completed_tasks_week_percentage()
        total_completed_tasks_month_percentage = to_do_list.total_completed_tasks_month_percentage()
        average_completion_time = to_do_list.average_completion_time()

        statistics = {
            'total_tasks': total_tasks,
            'completed_last_week': total_completed_tasks_week,
            'completion_percentage_week': total_completed_tasks_week_percentage,
            'completed_last_month': total_completed_tasks_month,
            'completion_percentage_month': total_completed_tasks_month_percentage,
            'average_completion_time': average_completion_time
        }

        return jsonify(statistics)
    except Exception as e:
        print(f"Error occurred while getting task statistics: {e}")
        return jsonify({'error': 'An error occurred while getting task statistics'}), 500


if __name__ == "__main__":
    #total_tasks = to_do_list.total_tasks()
    #total_completed_tasks_week = to_do_list.total_completed_tasks_week()
    #total_completed_tasks_week_percentage = to_do_list.total_completed_tasks_week_percentage()
    #total_completed_tasks_month = to_do_list.total_completed_tasks_month()
    #total_completed_tasks_month_percentage = to_do_list.total_completed_tasks_month_percentage()
    #average_completion_time = to_do_list.average_completion_time()
    app.run(debug=True)