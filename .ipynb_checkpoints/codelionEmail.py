import smtplib 
from email.message import EmailMessage # transfers to MIME
import imghdr
import reg

def SendEmail(addr):
    reg = "^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9]+/.[a-zA-Z]{2,3}$"
    if bool(re.match(reg,addr)): # This validates the email address
        smtp.send_message()
        print("Email sent successfully")
    else:
        print("Not valid email")
    
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 465 # we need to use 465 to access gmail server

message = EmailMessage() # MAke MIME 통
message.set_content("") # 본문 입력하기

message["Subject"] = "This is the title"
message["From"] = "jjpark067@gmail.com"
message["To"] = "shan8017@gmail.com"

image = open("codelion.png", "rb")

with open("codelion.png", "rb") as image: # safer way of opening files
    image_file = image.read()
    
    image_type = imghdr.what('codeloin', image_file)
    message.add_attachment(image_file, maintype='image', subtype = image_type)


smtp = smtplib.SMTP_SSL(SMTP_SERVER, SMTP_PORT) # connects to server (We need address and port number)
smtp.login("jjpark067@gmail.com", "~~~~~~~~~~")

SendEmail(message["To"])


smtp.quit()