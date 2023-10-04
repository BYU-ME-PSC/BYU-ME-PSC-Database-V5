import smtplib
import sys

def sendEmail(Message, Sender, Password, Recipient, Subject): 
    #Subject = "Checked Out Items Follow Up, CB 154, ME Department"
    Body = "From: %s\r\n" % Sender +  "To: %s\r\n" % Recipient +  "Subject: %s\r\n" % Subject +  "\r\n" +  Message
    try:
        smtpObj = smtplib.SMTP('mail.byu.edu', 587)
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login("ksc@byu.edu",Password)
        try:
            smtpObj.sendmail(Sender, Recipient, Body)
            print("successfully sent email")
        except Exception as e:
            print(e)
            print("ERROR: unable to send email")
            smtpObj.quit()
        #smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    except Exception as e:
        print(e)
        #smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        #smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    #smtpObj.starttls()
if __name__ == "__main__":
    sendEmail(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
