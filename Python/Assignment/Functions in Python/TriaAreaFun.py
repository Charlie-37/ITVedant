
# //*---- Function To Find Area Of Triangle


def AreaTri(base,height):

    area = (1/2) * base * height
    return area

base= float(input("Enter the Base of the Triangle : "))
height= float(input("Enter the Height of the Triangle : "))


area = AreaTri(base,height)
print("Area of the Triangle is :",area)





