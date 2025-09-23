import mysql.connector
try:
    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="crud_task"
    )
except:
    print("Error!")

mycursor=mydb.cursor()
# mycursor.execute("create table user_info (id int auto_increment primary key, name varchar(50) not null,Email varchar(100) not null,password varchar(100) not null,Roll varchar(50) not null)")


sql = "INSERT INTO user_info (name, Email, password, Roll) VALUES (%s, %s, %s, %s)"
vals =[]
print("1: data entery ")
print("2: Update data ")
x=int(input("Enter your choice "))
if x==1:
    n=int(input("How many persons data you want to add  "))
    for i in range(n):
        print(f"\nUser {i+1}")
        name = input("Enter name: ")
        email = input("Enter email: ")
        password = input("Enter password: ")
        roll = input("Enter roll (admin/user): ")
        
        vals.append((name, email, password, roll))

    mycursor.executemany(sql, vals)
    mydb.commit()
elif x==2:
    n=input("You want to update or not (Yes/No) ").lower()
    if n=="yes":
        print("1: Name ")
        print("2: Email ")
        print("3: password ")
        print("4: User Roll ")
        up=int(input("What you want to update "))




