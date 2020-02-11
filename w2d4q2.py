input_string=input("enter the string:")
x=0
y=0
for i in input_string:
  if(i.islower()):
    x=x+1
  elif(i.isupper()):
    y=y+1

print("the number of upper case are ",+y)
print("the number of lower case are," ,+x)