import mysql.connector
import re

email_pattern = r'^[a-zA-Z0-9._%+-]+@gmail\.com$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$'

try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_task"
    )
except mysql.connector.Error as e:
    print("Error!")
    exit()

mycursor=mydb.cursor()
mycursor.execute("create table user_info (id int auto_increment primary key, name varchar(50) not null,Email varchar(100) not null,password varchar(100) not null,Roll varchar(50) not null)")


sql = "INSERT INTO user_info (name, Email, password, Roll) VALUES (%s, %s, %s, %s)"

while True:
    print("------- Welcom! ------ ")
    print("1: data entery ")
    print("2: Update data ")
    print("3: Read data ")
    print("4: Delete data ")
    print("5:Exit")
    print("-"*40)
    x=int(input("Enter your choice ").strip())
    print("-"*40)
    if x==1:
        vals =[]
        print("-"*40)
        n=int(input("How many persons data you want to add  ").strip())
        print("-"*40)
        print("_"*40)
        print("\nNote:  Name save exactly as you write! ")
        print("_"*40)
        for i in range(n):
            print("*"*40)
            print(f"\nUser {i+1}")
            name = input("Enter name: ").strip()
            email = input("Enter email: ").strip()
            if not re.match(email_pattern, email):
              print(" Invalid email! Please enter a valid Gmail address.")
              continue
                  

            password = input("Enter password: ")
            if not re.match(password_pattern, password):
             print(" Weak password! Must be 8+ chars, include A-Z, a-z, 0-9, and a special char.")
             continue

            roll = input("Enter roll (admin/user): ").strip()
            print("*"*40)
            vals.append((name, email, password, roll))
        if vals:
          mycursor.executemany(sql, vals)
          mydb.commit()
          print("-"*40)
          print("Data save successfully!")
          print("-"*40)
        else:
            print("data not save plz entery valid information")
    elif x==2:
        print("-"*40)
        n=input("You want to update or not (Yes/No) ").lower().strip()
        print("-"*40)
        if n=="yes":
            print("1: Name ")
            print("2: Email ")
            print("3: password ")
            print("4: User Roll ")
            print("-"*40)
            up=int(input("What you want to update ").strip())
            print("-"*40)
            if up ==1:
                print("-"*40)
                id=int(input("Enter your id to update ").strip())
                name=input("Enter your new name  ").strip()
                print("-"*40)
                sql="update user_info set name=%s  where id=%s"
                val=(name,id)
            elif up==2:
                print("-"*40)
                id=int(input("Enter your id to update ").strip())
                email=input("Enter your new Email  ").strip()
                if not re.match(email_pattern, email):
                 print(" Invalid email! Please enter a valid Gmail address.")
                 continue   

                print("-"*40)
                sql="update user_info set Email=%s  where id=%s"
                val=(email,id)
            elif up==3:
                print("-"*40)
                id=int(input("Enter your id to update ").strip())
                pa=input("Enter your new password  ").strip()
                password = input("Enter password: ")
                if not re.match(password_pattern, password):
                  print(" Weak password! Must be 8+ chars, include A-Z, a-z, 0-9, and a special char.")
                  continue

                print("-"*40)
                sql="update user_info set password=%s  where id=%s"
                val=(pa,id)
            elif up==4:
                print("-"*40)
                id=int(input("Enter your id to update ").strip())
                rol=input("Enter your new Roll  ").strip()
                print("-"*40)
                sql="update user_info set Roll=%s  where id=%s"
                val=(rol,id)
            mycursor.execute(sql,val)
            mydb.commit()
            
            if mycursor.rowcount > 0:  
                print(">"*40)
                print(" Updated successfully!")
                print(">"*40)
            else:
                print("<"*40)
                print(" No record found with this ID!")
                print("<"*40)
            
        else:
            print("-"*40)
            print("Upadation cancel!")
            print("-"*40)
    elif x==3:
        print("-"*40)
        print("You want to read full data or limited")
        print("-"*40)
        print("1:Read all ")
        print("2: limited data ")
        print("-"*40)
        y=int(input("what you want  ").strip())
        print("-"*40)
        if y==1:
            mycursor.execute("select * from user_info")
            rows=mycursor.fetchall()
            print("\n---------- Record --------")
            for row in rows:
                print(row)
        elif y==2:
            print("-"*40)
            print("What you want to see in limited data ")
            print("-"*40)
            print("1:Names")
            print("2:Emails")
            print("3:Passwords")
            print("4:Roll")
            print("5:See All in limit ")
            print("-"*40)
            n=int(input("Enter your choice ").strip())
            print("-"*40)
            if n==1:
                print("-"*40)
                limitinput=input("You want to add limit (yes/no)").lower().strip()
                print("-"*40)
                if limitinput=="yes":
                    li=int(input("Enter your limit ").strip())
                    mycursor.execute(f"select name from user_info limit {li}")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                        print(row[0])
                elif limitinput=="no":
                    mycursor.execute("select name from user_info")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
                    
            elif n==2:
                print("-"*40)
                limitinput=input("You want to add limit (yes/no)").lower().strip()
                print("-"*40)
                if limitinput=="yes":
                    li=int(input("Enter your limit").strip())
                    mycursor.execute(f"select Email from user_info limit {li}")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
                elif limitinput=="no":
                    mycursor.execute("select Email from user_info")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
            elif n==3:
                print("-"*40)
                limitinput=input("You want to add limit (yes/no)").lower().strip()
                print("-"*40)
                if limitinput=="yes":
                    li=int(input("Enter your limit").strip())
                    mycursor.execute(f"select password from user_info limit {li}")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
                elif limitinput=="no":
                    mycursor.execute("select password from user_info")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
            elif n==4:
                print("-"*40)
                limitinput=input("You want to add limit (yes/no)").lower().strip()
                print("-"*40)
                if limitinput=="yes":
                    li=int(input("Enter your limit").strip())
                    mycursor.execute(f"select Roll from user_info limit {li}")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
                elif limitinput=="no":
                    mycursor.execute("select Roll from user_info")
                    rows=mycursor.fetchall()
                    print("\n---------- Record --------")
                    for row in rows:
                     print(row[0])
            elif n==5:
                print("-"*40)
                limit=int(input("Enter your limit ").strip())
                print("-"*40)
                mycursor.execute(f"select * from user_info limit {limit}")
                rows=mycursor.fetchall()
                print("\n---------- Record --------")
                for row in rows:
                 print(row)
    elif x==4:
        print("-"*40)
        id=int(input("Enter your id to delete your record  ").strip())
        print("-"*40)
        sql=f"delete from user_info where id={id}"
        mycursor.execute(sql)
        mydb.commit()
        if mycursor.rowcount > 0:  
            print(">"*40)
            print(" deleted successfully!")
            print(">"*40)
        else:
            print("<"*40)
            print(" No record found with this ID!")
            print("<"*40)
        
        
    elif x==5:
        exit()
    
            
            
        
        
        




