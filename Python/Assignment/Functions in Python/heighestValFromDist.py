'''Q.Item with highest value count
items = [{'apple': 5}, {'banana': 8}, {'orange': 7}, {'grapes': 4}]
def itemWithHighestValue(items):
pass'''

item = [{'apple': 5}, {'banana': 8}, {'orange': 7}, {'grapes': 4}]

def itemWithHighestValue(item):
    n = -999999
    name=''
    for k in item:
        
        for i,j in k.items():
            if j >  n:
                name=i
                n = j
    return(name,n)


print(itemWithHighestValue(item))
