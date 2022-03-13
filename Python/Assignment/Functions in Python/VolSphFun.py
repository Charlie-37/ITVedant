
#   //*------Function to Find Volume Of Shere----*//
def VolSph(r):

    vol = (4/3) * 3.141 * (r**3)
    return vol

r= float(input("Enter the Radius Of Sphere : "))

print(f"Volume is :",VolSph(r))