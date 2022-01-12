password=input()
length=len(password)

upper=0
lower=0
digit=0
special=0
if(length>=6 and length<=16):
    for i in password:
        if(i.isupper()):
            upper=upper+1 
        elif(i.islower()):
            lower=lower+1 
        elif(i.isdigit()):
            digit=digit+1
        else:
            special=special+1 
else:
    print("password word must be in limit")
if(upper>=1 and lower>=1 and digit>=1 and special>=1):
    print("valid password")
else:
    print("Invalid password")
