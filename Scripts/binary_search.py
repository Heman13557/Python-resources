Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@atrishabhsharma 
aniketsharma00411
/
algorithmsUse
1
1
64
Code
Issues
3
Pull requests
9
Actions
Projects
Wiki
Security
Insights
algorithmsUse/Python/Searching/binarySearch.py /
@aniketsharma00411
aniketsharma00411 Directories created
Latest commit 14d2f25 6 hours ago
 History
 1 contributor
38 lines (28 sloc)  982 Bytes
 
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

# Python 3 program for recursive binary search. 
  
# Returns index of x in arr if present, else -1 
def binary_search(arr, low, high, x): 
  
    # Check base case 
    if high >= low: 
  
        mid = (high + low) // 2
  
        # If element is present at the middle itself 
        if arr[mid] == x: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif arr[mid] > x: 
            return binary_search(arr, low, mid - 1, x) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binary_search(arr, mid + 1, high, x) 
  
    else: 
        # Element is not present in the array 
        return -1
  
# Test array 
arr = [ 2, 3, 4, 10, 40 ] 
x = 10
  
# Function call 
result = binary_search(arr, 0, len(arr)-1, x) 
  
if result != -1: 
    print("Element is present at index", str(result)) 
else: 
    print("Element is not present in array") 
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About

