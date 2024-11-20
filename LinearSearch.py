# linear Search
# it return th eidex of the element

arr = [1,2,3,4,8,9,77]

searching_element = 77

for i in  range(0,len(arr)):
   if arr[i] == searching_element:
     print(i," in the searching element ")
     break
else:
   print("Searching Element not Found !! ")  # y putting the elsei in down the for loop becz ,  
                                             #  when searcing if not element finds first 2 cases it goes to the else statement 
                                           
