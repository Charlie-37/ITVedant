
# //* Write a function in python to count the number of lines from a text file "story.txt" which is not starting with an alphabet "T".

def readLine():
    file = open("story.txt","r")
    cont = file.readlines()
    
    count = 0
    for i in cont:
        
        if i.startswith("T"):
            pass
        else:
            count+=1
    print("Number of Line is :",count)
    file.close()
readLine()

print("-*-"*20)
print("\n")


# //* 2. Write a function display_words() in python to read lines from a text file "story.txt", and display those words, which are less than 4 characters.

def display_words():
    file = open("story.txt","r")
    cont = file.read()
    word=cont.split()
    #print(cont)

    for i in word:
        if len(i)<4:
            print(i)
    file.close()
display_words()
print("-*-"*20)


# //* 3.Write a function in Python to copy the content of stroy.txt into story2.txt file.

def CopyPst():
    f1 = open("story.txt","r")
    lines = f1.read()
    
    f2 = open("story2.txt","w")
    f2.write(lines)
    
    f2.close()
    f1.close()
CopyPst()
    
