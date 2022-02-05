#https://developers.google.com/gmail/api/guides/sending
# r u working from here?
# this is what I was gonna use because it comes straight from google but I can just let you do your thing if you want.


#https://docs.python.org/3/library/smtplib.html
#https://docs.python.org/3/library/email.examples.html
#im googling everything lol
## haha at this point me too
import imghdr
import email
import smtplib

msg = email.message.EmailMessage()

msg["Subject"] = "mer christmas"
msg["From"] = "valentinesphotos879@gmail"
msg["To"] = "ttourne1@binghamton.edu"## Theo"s email for testing

msg.set_content("testing")

#add image attachment
#msg.add_attachment(file_data, maintype="image", subtype=file_type, filename=file_name)


server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("valentinesphotos879@gmail.com", "Picsforvalentines$$(2")

## yeah but we"ll need to install it too.

## attach image to file
file_pointer = open("cat_pic.png","rb")
pic = file_pointer.read()
msg.add_attachment(pic, maintype = "image",subtype=imghdr.what(None, pic))

server.send_message(msg)
server.quit()
