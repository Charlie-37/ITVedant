library = [('book1',2002),('book2',2012),('book3',2007),('book4',2015),('book5',2005),('book6',2018)]


books = [(i,j) for i,j in library if(j>=2010)]
print(books)