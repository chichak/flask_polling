# app.py
import psycopg2
import psycopg2.extras 
import os
from flask import Flask, render_template, request, url_for, redirect, jsonify, flash

# https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-20-04


app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='polling_db',
                            user="ichrak",
                            password="keybfr")
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    cur.execute("SELECT * FROM prg_languages ORDER BY id ASC")
    webframework = cur.fetchall()
    return render_template('index.html', webframework = webframework)

@app.route('/polldata', methods=('GET', 'POST'))
def polldata():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    query = "SELECT * from tbl_poll"
    cur.execute(query)
    total_poll_row = int(cur.rowcount)
    cur.execute("SELECT * FROM prg_languages ORDER BY id ASC")
    framework = cur.fetchall()
    frameworkArray = []
    for row in framework:
        get_title = row['title']
        cur.execute("SELECT * FROM tbl_poll WHERE web_framework =  %s", [get_title])
        row_poll = cur.fetchone()
        total_row = cur.rowcount
        #print(total_row)
        percentage_vote = round((total_row/total_poll_row)*100)
        print (percentage_vote)
        if percentage_vote >= 40:
            progress_bar_class = 'progress-bar-success'
        elif percentage_vote >= 25 and percentage_vote < 40 :
            progress_bar_class = 'progress-bar-info'
        elif percentage_vote >= 10 and percentage_vote < 25 :
            progress_bar_class = 'progress-bar-warning'
        else : 
            progress_bar_class = 'progress-bar-danger'
        frameworkObj = {
            'id': row['id'],
            'name': row["title"],
            'percentage_vote': percentage_vote,
            'progress_bar_class': progress_bar_class 
        }
        frameworkArray.append(frameworkObj)
    print(frameworkArray)
    return jsonify({'htmlresponse': render_template('response.html', frameworklist = frameworkArray)})

@app.route("/insert", methods=["GET", "POST"])
def insert():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor) 
    if request.method == "POST":
        poll_option = request.form["poll_option"]
        print(poll_option)
        cur.execute("INSERT INTO tbl_poll (web_framework) VALUES  (%s)", [poll_option])
        conn.commit()
        cur.close()
        msg = 'success'
    return jsonify(msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=5007)