
import statistics as st
help = dir(st)
print(help)  # all Directory in th statistics module

# //*------------Mean----------*//
# //* It will give the mean of given number, Here I have used a list which having a numbers as elements
list1 = [20,20,20,16,85]
meanList = st.mean(list1)
print(f"Mean of the list {list1} is : ",meanList)


# //*----------Median----------*///
# //* It will give the median from the given argument

list2 = [40,0,14,16,85,56]
medianList = st.median(list2)
print(f"Median of the list {list2} is : ",medianList)

# //*---------- Mode----------*///
# //* It will give the mode(repeating numbers) from the given argument

list3 = [10,0,14,56,85,56]
modeList = st.mode(list3)
print(f"Mode of the list {list3} is : ",modeList)

# //*---------- Variance----------*///
# //* It will give the variance from the given argument

list4 = [10,5,15,20,25]
varList = st.variance(list4)
print(f"Mode of the list {list4} is : ",varList)