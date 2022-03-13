''' Create a lambda function to sort the name list according to their surname.
name = ["jay A kumar",'deepak N sharma','rohit N yadav','mithilesh singh','payal vasave','Fahad Momin']'''



name = ["jay A kumar",'deepak N sharma','rohit N yadav','mithilesh singh','payal vasave','Fahad Momin']
name.sort(key = lambda surn: surn.lower().split()[-1])
print(name)