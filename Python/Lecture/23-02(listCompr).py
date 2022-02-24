
# //*--------List Comprehension-----*//


# //*-----Creation of list without typing the value----//

##x = [i for i in range(1,10) if(i%2==0)]
##print(x)
##
##
##sq = [i**2 for i in range(10)]
##print(sq)
##
##l = list(range(1,100))
##print(l)
##
##

# //*---Get the books whose year is greater than 2010------*//

##Lib = [("Book1",2002 ),("Book2",2021 ),("Book3",2009 ),("Book4",2014 ),("Book5",2005)]
##
##books = [(book,year) for book,year in Lib if(year>2010)]
##print(books)


# //*------get the negative word in new list----*//
##grammer = "is am are not was no never will shall nor does neither do none did not".split()
##
##negword = [word for word in grammer if (word.startswith("n"))]
##print(negword)



##x = [(i,j) for i in range(1,4) for j in range()]

##x1 = [1,2,3]
##x2 = ["a", "b","c"]
##
##lisx = [(i,j) for i in x1 for j in x2]
##print(lisx)
##


# //*-----Pattern-------*//

##for i in range(1,5):
##    for j in range(0,i):
##        print("*",end = "")
##    print("")
'''
*
**
***
****
'''


##row = 5
##
##for i in range(1, row):
##    for j in range(row, i, -1):
##        print("*", end="")
##    print()

'''
****
***
**
*
'''


##row = 5
##
##for i in range(1, row):
##    for j in range(0, row):
##        if j%2 ==0:
##            print("*", end=" ")
##        else:
##            print("#", end=" ")
##    print(" ")

'''
* # * # *  
* # * # *  
* # * # *  
* # * # *  

'''



##row = 5
##
##for i in range(1,row):
##    for j in range(row-1, i,-1):
##        print(" ",end="")
##    for k in range(1,i+1):
##        print("*", end="")
##    print("")

'''
    *
   **
  ***
 ****
'''









































