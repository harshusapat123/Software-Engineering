import unittest
import smtplib
import otp_version1 as O1

class BetweenAssertMixin(object):
    def assertBetween(self, x, low, hi):
        if not (low <= x <= hi):
            raise AssertionError('Length of OTP is %r should be in between %r and %r' % (x, low, hi))
        
class Test_otp(unittest.TestCase,BetweenAssertMixin):
    def testcase1(self):
        print("TestCase_No.1")
        #Checking Email
        Name="Harshala"
        Email="harshusapat123@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        otp = O1.generate_otp(4)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O1.send_email(Name,Email)
        print()

    def testcase2(self):
        #Checking Email with wrong email id
        print("TestCase_No.2")
        Name="Harshala"
        Email="harshusapat123gmail.com"

        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "@" and "." and "com" and "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        otp = O1.generate_otp(5)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O1.send_email(Name,Email)
        print()

    def testcase3(self):
        #Checking Email
        print("TestCase_No.3")
        Name="Harshala"
        Email="harshusapat123@gmail.com"
        self.assertIn("@",Email)
        self.assertIn(".",Email)
        self.assertIn("com",Email)

        True_Str1 = "gmail" in Email        
        if True_Str1 :
            print("No Error Found in Email!")
        else:
            self.assertTrue(True_Str1)

        #Checking OTP
        # Here i will Enter invalid otp length
        otp = O1.generate_otp(9)
        self.assertBetween(len(otp),4,8)

        #Calling Sendmail Function
        O1.send_email(Name,Email)
        
unittest.main()
