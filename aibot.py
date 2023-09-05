import imaplib
import email

def get_email():
    user, password = get_cred()
    imap = imaplib.IMAP4_SSL("imap.gmail.com")
    result = imap.login(user, password)
    imap.select("INBOX")
    result, data = imap.search(None, '(UNSEEN)')

    for num in data[0].split():
        result, data = imap.fetch(num, '(RFC822)')
        print(data)
        for response in data:
            if isinstance(response, tuple):
                data = email.message_from_bytes(response[1])
                print(data["Date"])
                print(data["From"])
                print(data["Subject"])
                print(data["To"])
        for part in data.walk():
            if part.get_content_type() == "text/plain":
                body = part.get_payload(decode=True)
                print(f'Body: {body.decode("UTF-8")}', )

def get_cred():
    file = open("/opt/phishbot/auth/.gmcred","r")
    lines = file.readlines()
    user = lines[0].rstrip("\n")
    password = lines[1].rstrip("\n")
    return(user,password)

get_email()