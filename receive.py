import imaplib
import email
from email.header import decode_header
import handle
import time

mail = ""

def login(army):
    global mail
    # IMAP server settings for Gmail
    imap_server = 'imap.gmail.com'
    email_address = 'mckaygonefishing@gmail.com'
    email_password = 'srkkpktzgbaydxoo'  # Generate an app password for your Gmail account

    # Connect to the Gmail IMAP server
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(email_address, email_password)



    ## configure which folder it looks at
    mail.select('Inbox')
    receive_mail(army)
    

## Get email IDS
def receive_mail(army):
    global mail
    tmp, email_ids = mail.search(None, "ALL")
    
    for email_id in email_ids[0].split():
        result, data = mail.fetch(email_id, '(RFC822)')
        raw_email = data[0][1]

        # Parse the raw email into a message object
        msg = email.message_from_bytes(raw_email)

        # Decode email subject
        subject, encoding = decode_header(msg['Subject'])[0]
        if isinstance(subject, bytes):
            subject = subject.decode(encoding)

        # Print email details
        print(f"From: {msg['From']}")
        print(f"To: {msg['To']}")
        print(f"Subject: {subject}")

        # Check if the email contains multiple parts (text, attachments, etc.)
        if msg.is_multipart():
            for part in msg.walk():
                content_type = part.get_content_type()
                content_disposition = str(part.get("Content-Disposition"))

                # Print email content
                if content_type == "text/plain" and "attachment" not in content_disposition:
                    body = part.get_payload(decode=True).decode()
                    print("Message Body:")
                    print(body)

                    delete_email(msg, subject, body, email_id, army)
                    #function to handle sender
        else:
            # Single-part email
            content_type = msg.get_content_type()
            body = msg.get_payload(decode=True).decode()
        
            delete_email(msg, subject, body, email_id, army)


        print("=" * 40)
        delete_email(msg, subject, body, email_id, army)

    return
        

        
def delete_email(msg, subject, body, email_id, army): ##take email id of email to be deleted, then store it then handle the message
    global mail
    mail.store(email_id, '+FLAGS', '\\Deleted')
    time.sleep(.5)
    sender = msg["from"]
    print(sender)
    handle.handle_message(msg['from'], subject, body, army)
    return
    
def logout(): ##This isn't working since there is an order issue 
    global mail
    mail.select('INBOX')
    
    mail.close()
    mail.logout()
    # Logout from the email server
    return
