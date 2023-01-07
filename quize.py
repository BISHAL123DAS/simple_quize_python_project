print("-----WELCOME TO QUIZE COMPTITIONS-----")
playing=input('Are you participated in quize compitisions:? ')
count=0
if(playing!='yes'):
    quit()
ans=input("what is the full from of cpu? ")
if(ans=='central processing unit'):
    print('correct!')
    count+=1
else:
    print("incorrect!")

ans=input("which year discoverd computer? ")
if(ans=='1942'):
    print('correct!')
    count+=1
else:
    print("incorrect!")

ans=input("what is the full from of pdf? ")
if(ans=='portable document format'):
    print('correct!')
    count+=1
else:
    print("incorrect!") 

ans=input("Father of computer? ")
if(ans=='chalse babeje'):
    print('correct!')
    count+=1
else:
    print("incorrect!")

ans=input("what is the full from of RAM? ")
if(ans=='random acess memory'):
    print('correct!')
    count+=1
else:
    print("incorrect!")

ans=input("what is the full from of ROM? ")
if(ans=='read only memory'):
    print('correct!')
    count+=1
else:
    print("incorrect!")  

ans=input("city of joy? ")
if(ans=='kolkata'):
    print('correct!')
    count+=1
else:
    print("incorrect!")


print("your result  out of 10 is=",count)


print("---THANKYOU FOR PARTICIPATED THE QUIZE COMPITISIONS---")