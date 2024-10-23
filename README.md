# cen4350c
Todo list built using Python/Flask. Features include remidners and task completion statistics.

## Prerequisites

- Python 3.10
- MySQL 8.xx
- PyCharm or similar IDE/text editor installed on your machine.
- A web browser to run the server in localhost.

## Setup

1. **Clone the repository:**

   ```
   git clone https://github.com/sneseric/cen4350c.git
   ```

2. **Install the dependencies**

   ```
   pip install -r requirements.txt
   ```
   

3. **Edit this code in The app.py file for your local MySQL credentials**

   ```
   user="root",
   password="password",
   ```

4. Run wsgi.py

5. In your web browser, navigate to http://localhost:5000/

## Usage

1. From left-hand column, add and delete tasks as needed.
2. In middle column, toggle the daily task summary button on/off as desired to view notifications due today and tommorow (will show on page refresh and add/delete task).
