#!/usr/bin/python3

class colors:
    RED = '\033[31m'
    ENDC = '\033[m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'


print(colors.YELLOW + "                           __    _      __    __          __")
print(colors.YELLOW + " __                 ____  / /_  (_)____/ /_  / /_  ____  / /_")
print(colors.YELLOW + "/o \\/    __        / __ \\/ __ \\/ / ___/ __ \\/ __ \\/ __ \\/ __/")
print(colors.YELLOW + "\\__/\\   /o \\/     / /_/ / / / / (__  ) / / / /_/ / /_/ / /_  ")
print(colors.YELLOW + "        \\__/\\    / .___/_/ /_/_/____/_/ /_/_.___/\\____/\\__/  ")
print(colors.YELLOW + "                /_/ ")

recipient = input(colors.GREEN + 'Enter destination email address:\n' + colors.ENDC)

print(recipient)