#!/usr/bin/python3
import argparse
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.utils import formataddr
import time

class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'

def initialize():
    parser = argparse.ArgumentParser("phishbot operators")
    parser.add_argument("-e", "--email", type=str, help="enter email of recipient")
    parser.add_argument("-f", "--file", type=str, help="enter file with list of recipients")
    parser.add_argument("-r", "--report", action="store_true", help="run report of phish statistics")
    args = parser.parse_args()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()
    email = args.email
    file = args.file
    report = args.report
    return(email,file,report)

def single_phish(email):
    logo_gen()
    print(colors.GREEN + "\n <>< <><  Sending Phishbot email to " + email + "  <>< <>< \n" + colors.ENDC)
    t = str(round(time.time()))
    f = open("/var/www/html" + t + ".html", "w")
    f.close
    user,password = get_cred()
    smtp_port = 587
    smtp_server = "smtp.gmail.com"
    email_from = user
    email_to = email
    pswd = password
    subject = "Email Test #1!"
    body = '<h1>This is the Body of Email</h1><br /><a href="http://3.19.16.86/'+t+'.html">free offer</a><br />'

    msg = MIMEMultipart()
    msg['From'] = formataddr(('your best friend', email_from))
    msg['To'] = email_to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'html'))

    ##uncomment below section if attachment required
    #filename = "/Users/radspyder/Downloads/spider.png"
    #attachment = open(filename, 'rb')
    #attachment_package = MIMEBase('application', 'octet-stream')
    #attachment_package.set_payload((attachment).read())
    #encoders.encode_base64(attachment_package)
    #attachment_package.add_header('Content-Disposition', "attachment; filename= " + filename)
    #msg.attach(attachment_package)
    ##end of attachment section

    text = msg.as_string()
    print(colors.GREEN + "Connecting to mail server ... \n" + colors.ENDC)
    mail_server = smtplib.SMTP(smtp_server, smtp_port)
    mail_server.starttls()
    mail_server.login(email_from, pswd)
    print(colors.GREEN + "Successfully connected to mail server ... \n" + colors.ENDC)
    print(colors.GREEN + "<>< <><  Successfully sent Phishbot email to " + email_to + "  <>< <>< \n" + colors.ENDC)
    mail_server.sendmail(email_from, email_to, text)
    mail_server.quit()
    t = str(round(time.time()))
    f = open("/var/www/html" + t + ".html", "w")
    f.close

def multi_phish(file):
    logo_gen()
    print(file)
    print("sending multiple emails")

def create_report():
    print("generating report")

def logo_gen():
    print(colors.YELLOW + "                           __    _      __    __          __")
    print(colors.YELLOW + " __                 ____  / /_  (_)____/ /_  / /_  ____  / /_")
    print(colors.YELLOW + "/o \\/    __        / __ \\/ __ \\/ / ___/ __ \\/ __ \\/ __ \\/ __/")
    print(colors.YELLOW + "\\__/\\   /o \\/     / /_/ / / / / (__  ) / / / /_/ / /_/ / /_  ")
    print(colors.YELLOW + "        \\__/\\    / .___/_/ /_/_/____/_/ /_/_.___/\\____/\\__/  ")
    print(colors.YELLOW + "                /_/ ")

def get_cred():
    file = open("/opt/phishbot/auth/.cred","r")
    lines = file.readlines()
    user = lines[0].rstrip("\n")
    password = lines[1].rstrip("\n")
    return(user,password)

email,file,report = initialize()
if email:
    single_phish(email)
if file:
    multi_phish(file)
if report:
    create_report()