import mysql.connector


# Store the user information in mysql database
def store_user_info(name, age, mobile, email, place):

    # Connect to mysql database
    conn=mysql.connector.connect(
    host="localhost",
    user="root",
    password="Password1",
    database="mydb1"
    )
    c =conn.cursor()
    c.execute("INSERT INTO user2(Name,Age,Mobile_Number,Email,Place) VALUES(%s,%s,%s,%s,%s)", (name, age, mobile, email, place))
    conn.commit()
    conn.close()

#displaying database       
def sel_data():
    conn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="Password1",
        database="mydb1"
        )
    curse=conn.cursor()
    curse.execute("SELECT * FROM user2")

    pri=curse.fetchall()

    return pri

