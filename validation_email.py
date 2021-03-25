#Email validation
##Let's say you've created a registration form for people wanting to take part in your online book club. In order to send them invitations, you need to know their email address, so you are writing a program to check whether the field "email" is filled correctly.

#Write a function that takes a string and checks that:

#it doesn't contain spaces,
#it contains the @ symbol,
#after @, there's a dot, but in a correct address a dot shouldn't stand immediately after @,
#(@. should not be in the string).
#Note that dots may also occur before @!

#The function should return True if all of the conditions are true, and False otherwise.

#You are not supposed to handle input or call your function, just implement it.
import re
def check_email(string):
    return bool(re.fullmatch(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", string)) and True
