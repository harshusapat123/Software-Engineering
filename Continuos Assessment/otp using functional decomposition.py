#program for sending and generating OTP with Functional Decomposition

import random
import re
import smtplib
import time

#method for validation of Email
def check_email(email):
    
    p= "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    if(re.search(p,email)):   
         #regular expression is used here
        print("Email id is valid!")
        return True
    else:
        print(email+"- is not valid email id.\nPlease Enter valid Email Id!!")
        return False

#Method for Generation of OTP
otp_size = random.randint(4,8)
def generate_otp(size):
    otp=''
    for i in range(size):
        value = random.randint(0,9)
        otp = otp + str(value) 
    return otp

        
    

#Method for Sending OTP
def send_otp(mailid,otp):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    password ="ifzf chii aafz jpgy"
    sender_mail = "harshusapat123@gmail.com"
    msg = 'Hello, Your OTP is ' + str(otp)
    server.login(sender_mail,password)
    server.sendmail('harshusapat123@gmail.com', mailid , msg)
    print("OTP send !!")
    server.quit()

#Method for validating OTP
def validate_otp(otp):
    test_time= 30
    begnining_time = time.time()
    current_time = time.time()
    original_otp = otp
    input_otp = 0
    if input_otp == original_otp:
        pass
    else:
        while input_otp != original_otp and int(current_time)-int(begnining_time)<=test_time:
            if current_time - begnining_time <= test_time:
                input_otp = input("Enter Valid OTP :")
            current_time = time.time()
    if input_otp == original_otp:
        print("\nOTP is Valid!!")
    else:
        print("\nOut Of Time! OTP is valid for 30 seconds.")


email'harshusapat123@gmail.com'
if (check_email(email)):
        
        otp_size = random.randint(4,8)
        otp = generate_otp(otp_size)
        send_otp(email,otp)
        validate_otp(otp)
    


