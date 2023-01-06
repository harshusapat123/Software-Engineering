
#Laboratory Assesment progarm no:2
#Implement at least three features for Birthday greeting server application

import datetime
import imghdr
import mysql.connector
import os
import pywhatkit as pwt
import smtplib
from email.message import EmailMessage


now = str(datetime.date.today())
#to get date and month like 1112 
Today = now[8:10]+now[5:7]   
#print(Today)

#coonect to database
mydb = mysql.connector.connect(host="localhost",user="root",password="",database = "bday_data")


mycursor = mydb.cursor()

#method for inserting data into database
def add_data():
    mycursor1 = mydb.cursor()
    print("Enter details of person")
    name = input("Enter name:")
    birth_date = input("Enter birthdate in format datemonth like 1112 :")
    number = input("Enter mobile number :")
    email = input("Enter Email id: ")
    sql = "INSERT INTO data (name, birth_date,mobile_no,email_id ) VALUES (%s, %s, %s,%s)"
    person = (name,birth_date,number,email)
    mycursor1.execute(sql, person)
    mydb.commit()
    print("Data added!!")

#method for displaying data from databse    
def show_data():
    show = mydb.cursor()
    show.execute("select * from data")
    persons_list = show.fetchall()
    for i in persons_list:
        print(i)


'''def send_whatsappText(data,hour,minute):
    number = '+91'+data[2]
    name = data[0]
    msg ='hello' +name +'!! \n Wish you a Happiest Birtday!'
    pwt.sendwhatmsg(number, msg ,hour,minute,15)
'''

#method for sending whatsapp message  
def send_whatsappImage(data):
    name = data[0]
    number = '+91'+data[2]
    img ="C:\\Users\\Harshu\\OneDrive\\Desktop\\Laboratory Assessment\\bday.jpg"
    pwt.sendwhats_image(number,img,'Heyy '+ name + '!!! Wish you happiest birthday!',15,False,3)



#method for sending image on email
def send_EmailImage(data):
    with open ("bday_greet.jpg",'rb') as m:
        file_data = m.read()
        file_type = imghdr.what(m.name)
        file_name = m.name

    password ="ifzf chii aafz jpgy"
    sender_mail = "harshusapat123@gmail.com"
    receiver_mail = data[3]
    msg = EmailMessage()
    msg['Subject'] = 'Sending Birthday Greeting'
    msg['From']= sender_mail
    msg['to'] = receiver_mail
    msg.set_content("Hii " + data[0] +"!!\n Wish you many many happy returns of day!!")
    msg.add_attachment(file_data,maintype='image',subtype =file_type,filename = file_name)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender_mail,password)
    server.send_message( msg)
    print("message send !!")
    server.quit()

#method for sending text message on email
def send_EmailText(data):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password ="ifzf chii aafz jpgy"
    sender_mail = "harshusapat123@gmail.com"
    receiver_mail = data[3]
    msg = 'Hii' + data[0] +"!\n Wish you a happiest Birthday!!" 
    server.login(sender_mail,password)
    server.sendmail(sender_mail,receiver_mail , msg)
    print("Email send !!")
    server.quit()



    

add_data()
show_data()
mycursor.execute(f"select * from data where birth_date = {Today}")
list1= mycursor.fetchall()
for i in list1:
    #send_whatsappText(i,22,10)
    send_whatsappImage(i)
    send_EmailImage(i)
    send_EmailText(i)
    

'''num=9112974690
send_text(num)'''
    
    
