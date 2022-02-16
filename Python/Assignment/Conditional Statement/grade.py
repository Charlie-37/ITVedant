# //*----------Grade------------------*//

x = int(input("Enter the Percentage : "))

if x>=75 and x<100:
   print("Grade is A ")

elif x>=60 and x<75:
   print("Grade is B ")

elif x>35 and x<60:
   print("Grade is C ")

elif x<35 :
   print("Fail ")

else:
   print("Invalid Percentage ")