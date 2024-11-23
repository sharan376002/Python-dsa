# merger  Sort
#  o(n)   - space
#0(nlongn)   - time 

def MergeSort(array):
    if len(array)>1:
        mid = len(array)//2
        left = array[0:mid]
        right = array[mid:]

        MergeSort(left)      
        MergeSort(right)

        left_point = 0 
        right_point = 0 
        final_array = 0

        while(left_point<len(left)) and (right_point<len(right)):
            if left[left_point]<right[right_point]:
                array[final_array] = left[left_point]
                left_point+=1
            else:
                array[final_array] = right[right_point]
                right_point+=1
            final_array+=1
        while left_point<len(left):
            array[final_array] =left[left_point]
            final_array+=1
            left_point+=1            

        while right_point < len(right):
            final_array+= 1
            right_point+=1



array = [3,2,55,66,7,8,8,5,4,3,4,6,88,6,4,43]   
print(array)
MergeSort(array)
print(array)
