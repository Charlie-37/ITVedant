x= int(input("Enter the Year : "))

if x%4==0:
   if x%100==0:
       if x%400==0:
           print("Leap Year")
       else:
           print("Not a Leap year")
   else:
       print("Leap Year")
else:
   print("Not a Leap Year")