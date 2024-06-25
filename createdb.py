import sqlite3

def create_db():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text, duration text, charges text, description )")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,description text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS result(roll INTEGER PRIMARY KEY AUTOINCREMENT,name,course,marks_ob,full_marks,per)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS admin ( id INTEGER PRIMARY KEY AUTOINCREMENT,f_name TEXT NOT NULL,l_name TEXT NOT NULL,contact TEXT NOT NULL,email TEXT NOT NULL UNIQUE,question TEXT NOT NULL,answer TEXT NOT NULL,password TEXT NOT NULL)")
    con.commit()

create_db()
