
import re

RegexLength=re.compile(r'^\S{8,}$')
RegexDigit=re.compile(r'\d')
RegexLower=re.compile(r'[a-z]')
RegexUpper=re.compile(r'[A-Z]')


def IsStrongPW(password):
    if RegexLength.search(password) == None or RegexDigit.search(password) == None or RegexUpper.search(password) == None or RegexLower.search(password) == None:
        return False
    else:
        return True

while True:
    userpw=input("please input your passord to check: \n")
    if userpw == "exit":
        break
    else:
        print(IsStrongPW(userpw))

