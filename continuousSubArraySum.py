'''
Thursday, April 13, 2017

AUTHOR: JINTAO HE

PROBLEM OF CONTINOUS SUBARRAY:
Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k,
that is, sums up to n*k where n is also an integer.

EXAMPLE1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

EXAMPLE2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.

NOTES:
The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.
'''
def ContinuesSubarraySum(array,k):
    # initialize the Sublist length to 10,000 since the length of array won't exceed 10,000
    Sublist = [None]*10000
    # initialize the first element to be zero to distinguish the case of [21,14,1] and [21,1,14]
    Sublist[0]=0
    #since we set the first element in Sublist to be zero, we start at index 1
    index = 1
    #initialize the Sum to be zero 
    Sum = 0
    #initialize the modual to be -1 to distinguish from 0
    mod= -1

    #use for loop to go through every element in the array 
    for i in array:
        # add up sums
        Sum = Sum +i
        
        #calculate the mod
        mode = Sum % k
        
        
        # insert the mod into Sublist 
        Sublist[index]=mod
        #increment the index 
        index = index +1
        
        #if the mod is already in the arry 
        if(mod in Sublist):
            #find the index of the mud 
            indexOfMod = Sublist.index(mod)
            #since we initialize the frist element in Sublist to be 0; the difference between "continuous subarray" should be 2 
            if((index-indexOfMod)>2):
                return True
            
    return False
            
        
