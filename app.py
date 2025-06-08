from flask import Flask, request, redirect, render_template
import sqlite3

app=Flask(__name__)
tasks=[]

def get_db_connection():
    conn=sqlite3.connect('database.db')
    conn.row_factory=sqlite3.Row # 結果を辞書っぽく扱える
    return conn

@app.route("/", methods=["GET", "POST"])
def index():
    conn=get_db_connection()
    # name = None
    if request.method == "POST":
        task = request.form["task"]
        conn.execute("INSERT INTO tasks (content) VALUES (?)", (task,))
        conn.commit()
        return redirect("/")
    
        # tasks.append(task)
        # name = request.form["username"]
    tasks = conn.execute("SELECT * FROM tasks").fetchall()
    conn.close()
    return render_template("index.html", tasks=tasks)
    
if __name__=="__main__":
    app.run(debug=True)