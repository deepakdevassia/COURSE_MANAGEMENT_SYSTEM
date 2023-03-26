# COURSE MANAGEMENT SYSTEM (-ADD - VIEW - DELETE - COURSE DETAIL TO/FROM sql DATABASE)
import os
import platform
import mysql.connector
#import pandas as pd
mydb = mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="root",
                               database="course_match")
mycursor = mydb.cursor()
def course_Insert():
    L=[]
    c_id=int(input("Enter the course id :"))
    L.append(c_id)
    stream=input("Enter the Stream Name:")
    L.append(stream)
    C_name=(input("Enter the mode of course :"))
    L.append(C_name)
    course=(L)
    sql="insert into course_details (c_id, stream, c_name) values (%s,%s,%s)"
    mycursor.execute(sql,course)
    mydb.commit()
def cView():
    print("Select the search criteria :")
    print("1. BASED ON COURSE ID")
    print("2. BASED ON STREAM")
    print("3. TO VIEW All THE ENTRIES")
    ch = int(input("ENTER YOUR OPTION HERE :"))
    if ch == 1:
       s = int(input("c_id :"))
       c = (s,)
       sql = "select * from course_details where c_id=%s"
       mycursor.execute(sql,c)
    elif ch == 2:
       name = input("Enter stream Name :")
       n = (name,)
       sql = "select * from course_details where c_name=%s"
       mycursor.execute(sql,n)
    elif ch == 3:
       sql = "select * from course_details"
       mycursor.execute(sql)
    res = mycursor.fetchall()
    print("The course details are as follows :")
    print("(course_id, Stream_Name,Course_opportunities)")
    for x in res:
       print(x)
def removecourse():
    cid = int(input("Enter the course_id of the course to be deleted :"))
    ci =(cid,)
    sql="Delete from course_details where c_id=%s"
    mycursor.execute(sql,ci)
    sql="Delete from course_details where c_id=%s"
    mycursor.execute(sql,ci)
    mydb.commit()
def MenuSet(): #Function For The course match
    print("Enter 1 : To Insert a new  course")
    print("Enter 2 : To View an existing course")
    print("Enter 3 : To Remove an existing course")
    try:
        userInput = int(input("PLEASE ENTER YOUR OPTION HERE :")) #Will Take Input From User
    except ValueError:
        exit("\nHy! That's Not A Number") #Error Message
    else:
        print("\n") #Print New Line
        if userInput == 1:
            course_Insert()
        elif userInput == 2:
            cView()
        elif userInput == 3:
            removecourse()
        else:
            print("WRONG CHOICE!!!!")
MenuSet()
def runAgain():
    runAgn = input("TRY AGAIN !! Y/N:")
    while(runAgn.lower() == "y"):
        if(platform.system() == "Windows"):
            print(os.system("cls"))
        else:
            print(os.system("clear"))
        MenuSet()
        runAgn = input("TRY AGAIN !! Y/N:")
runAgain()