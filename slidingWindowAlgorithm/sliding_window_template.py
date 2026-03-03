arr =[]

window_invalid =True
left = 0
for right in range(len(arr)):
    
    # expand window
    #add(arr[right])
    
    # shrink while invalid
    while window_invalid:
        #remove(arr[left])
        left += 1
    
    # update result
    result = max(result, right - left + 1)


    # very import template !!!! 