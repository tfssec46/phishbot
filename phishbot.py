#!/usr/bin/python3
import argparse
import sys

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
    user,password = get_cred()

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