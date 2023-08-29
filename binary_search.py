def binary_search(arr,search):
   l = 0
   r = len(arr)-1
   
   while l <= r:
         mid = l + (r - l) // 2
         
         if search == arr[mid]:
             return True
         elif arr[mid] < search:
             l= mid + 1
         else:
             r = mid-1
   return False
    
print(binary_search([1,2,3,4,5,6,7,8], 9))
