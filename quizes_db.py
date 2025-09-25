import mysql.connector
import re
try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="quiz_task"
    )
except mysql.connector.errors as e:
    print("Error!")
    exit()

password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'
mycursor=mydb.cursor()
mycursor.execute("create database if not exists quiz_task")
mycursor.execute("create table if not exists user(user_id int auto_increment not null unique primary key,user_name varchar(50) not null,password varchar(50) not null )")
mycursor.execute("create table if not exists quizes(quiz_id int auto_increment not null unique primary key,quiz_name varchar(50) not null,created_by int not null,foreign key (created_by) references user(user_id)) ")
mycursor.execute("create table if not exists questions(question_id int auto_increment not null unique primary key,quiz_id int not null,question_text varchar(250) not null,option_a varchar(50) not null,option_b varchar(50) not null,option_c varchar(50) not null,option_d varchar(50) not null,correct_option int not null,foreign key (quiz_id) references quizes(quiz_id))")
mycursor.execute("create table if not exists score(score_id int auto_increment not null unique primary key,user_id int not null,quiz_id int not null,score int not null,date datetime ,foreign key (user_id) references user(user_id),foreign key (quiz_id) references quizes(quiz_id))")
mycursor.execute("alter table user add column if not exists role enum('admin','student') default 'student'")
mydb.commit()

try:
    print("\n-----Welcome---\n")
    print("Plz select your  Admin Or Student ?\n")
    print("1: Admin")
    print("2:Student")
    n=int(input(">>>>>>>  ").strip())
    if n>2 or n<=0:
     print("select a valid option")
except:
    print("Select in integers plz")
while True:
    if n==1:
        print("\n---- Admin information ----\n")
        name=input("Enter your name ").strip().capitalize()
        
        try:
            password=input("Enter your password ").strip()
            if not re.match(password_pattern, password):
                print(" Weak password! Must be 8+ chars, include A-Z, a-z, 0-9, and a special char.")
                continue
        except:
            print("\npassword,roll and name save successfully!\n")
        roll=input("Enter your roll (admin/student) ").strip().lower()
        sql="insert into user(user_name,password,role) values(%s,%s,%s)"
        val=(name,password,roll)
        mycursor.execute(sql,val)
        mydb.commit()
        admin_id=mycursor.lastrowid
        while True:
            try:
                print("\n----- Admin planel -----\n")
                print("1: Add Quizes ")
                print("2: Add Questions ")
                print("3: View Quizes ")
                print("4: View leaderborad ")
                print("5: back to main menu ")
                ad=int(input("Enter your choice ").strip())
                if ad>5 or ad<=0:
                    print("Plz chosse valid option ")
            except:
                print("Plz enter integers (1-5)")
            
            if ad==1:
                
                    try:
                        n=int(input("how many quizs you want to add or not press 'a'").strip())
                        for i in range(n):
                            print(f"\nQuiz {i+1}")
                            try:
                                tex=input("Enter quiz name >>  ").capitalize().strip()
                                sql="insert into quizes(quiz_name,created_by) Values(%s,%s)"
                                val=(tex,admin_id)
                                mycursor.execute(sql,val)
                                mydb.commit()
                                mycursor.execute("select * from quizes")
                                quizz=mycursor.fetchall()
                                for i in (quizz):
                                    print(f"your quiz id id {i[0]}/ your quiz name is {i[1]}/ and your your id is {i[2]}")
                            except:
                                print("enter text plz!")
                    except:
                        print("Enter in integers ")
                        
                
            elif ad==2:
                
                    try:
                        id=int(input("Enter your quiz id"))
                        q=int(input("Enter how many questions you want to add or press a  "))
                        for i in range(q):
                            print(f"\nQuestion {i+1}")
                            tex=input("Enter your text : ").capitalize().strip()
                            print("Now print options :  ")
                            a=input("A: ").capitalize().strip()
                            b=input("B: ").capitalize().strip()
                            c=input("C: ").capitalize().strip()
                            d=input("D: ").capitalize().strip()
                            correct=int(input("Right option (A=1,B=2,C=3,D=4) ").strip())
                            sql="insert into questions(quiz_id,question_text,option_a,option_b,option_c,option_d,correct_option) values(%s,%s,%s,%s,%s,%s,%s)"
                            val=(id,tex,a,b,c,d,correct)
                            mycursor.execute(sql,val)
                            mydb.commit()
                    except:
                        print("Fill details carefully!")
                        
            elif ad==3:
                
                    try:
                        id=int(input("Enter question id  "))
                        sql="select question_text,option_a,option_b,option_c,option_d,correct_option from questions where question_id=%s"
                        val=(id,)
                        mycursor.execute(sql,val)
                        result=mycursor.fetchone()
                        if result:
                            
                            print(f"Question: {result[0]}")
                            print(f"A: {result[1]}")
                            print(f"B: {result[2]}")
                            print(f"C: {result[3]}")
                            print(f"D: {result[4]}")
                            print(f"Correct Option: {result[5]}")
                        else:
                            print("No found")
                        
                        
                    except:
                        print("Enter in integer ")
            elif ad==4:
                
                sql = """SELECT s.score_id, u.user_name, q.quiz_name, s.score, s.date 
                        FROM score s
                        JOIN user u ON s.user_id = u.user_id
                        JOIN quizes q ON s.quiz_id = q.quiz_id
                        ORDER BY s.score DESC"""
                mycursor.execute(sql)
                show = mycursor.fetchall()

                if show:
                    print("\n--- Leaderboard ---")
                    for row in show:
                        print(f"Score ID: {row[0]} | Student: {row[1]} | Quiz: {row[2]} | Score: {row[3]} | Date: {row[4]}")
                else:
                    print("No scores available yet.")
            elif ad==5:
                print(f"---thanks for using Mr/Ms{name} ------")
                exit()
                        
                    
                
    if n==2:
        print("\n-------Student panal -------\n")
        name=input("Enter your name ").strip()
        
        try:
            password=input("Enter your password ").strip()
            if not re.match(password_pattern, password):
                print(" Weak password! Must be 8+ chars, include A-Z, a-z, 0-9, and a special char.")
                continue
        except:
            print("\npassword and name save successfully!\n")
        sql="insert into user(user_name,password) values(%s,%s)"
        val=(name,password)
        mycursor.execute(sql,val)
        mydb.commit()
        print("------- Aavilable quizs are ------")
        print("\n--- Available Quizzes ---")
        sql = """SELECT q.quiz_id, q.quiz_name,u.user_id, u.user_name 
                FROM quizes q 
                JOIN user u ON q.created_by = u.user_id"""
        mycursor.execute(sql)
        quizzes = mycursor.fetchall()

        if quizzes:
            for q in quizzes:
                print(f"Quiz ID: {q[0]} | Quiz Name: {q[1]} | Created By: {q[3]} (user id {q[2]})")
        else:
            print(" No quizzes available yet.")
        
        score=0
        while True:
    
            user_id=int(input("enter your user id  ").strip()) 
            quiz_id = int(input("Enter quiz id you want to attempt: "))

            
            sql = "SELECT question_id, question_text, option_a, option_b, option_c, option_d, correct_option FROM questions WHERE quiz_id = %s"
            val = (quiz_id,)
            mycursor.execute(sql, val)
            questions = mycursor.fetchall()

            score = 0
            for q in questions:
                qid, text, a, b, c, d, correct = q
                print(f"\nQuestion: {text}")
                print(f"1. {a}")
                print(f"2. {b}")
                print(f"3. {c}")
                print(f"4. {d}")
                
                try:
                    ans = int(input("Enter your answer (1-4): ").strip())
                    if ans == correct:
                        score += 1
                        print(" Correct!")
                    else:
                        print(" Wrong!")
                except:
                    print("Invalid input, skipped question.")

            print(f"\nYour final score: {score}/{len(questions)}")

            
            sql = "INSERT INTO score(user_id, quiz_id, score, date) VALUES (%s, %s, %s, NOW())"
            val = ( user_id,quiz_id, score)
            mycursor.execute(sql, val)
            mydb.commit()


                       
                
            

            
                
            
            
                






      
