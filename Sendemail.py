import smtplib

 # creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)

 # start TLS for security   
s.starttls()

 # Authentication  
s.login("Enter Your email here", "Email password")

 # message to be sent   
SUBJECT = "Enter the subject here"
TEXT = "Enter the text here"

message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)

 # sending the mail    
s.sendmail("Enter your email here", "Enter the email that you want the message to it", message)

 # terminating the session    
s.quit()

