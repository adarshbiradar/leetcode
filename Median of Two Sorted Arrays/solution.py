class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newNums = [] 
        i = 0
        j = 0
        while(i < len(nums1) and j < len(nums2)):
            if(nums1[i]<nums2[j]):
                newNums.append(nums1[i])
                i+=1
            elif(nums1[i]>nums2[j]):
                newNums.append(nums2[j])
                j+=1
            else:
                newNums.append(nums1[i])
                newNums.append(nums2[j])
                j+=1
                i+=1
        while(i!=len(nums1)):
            newNums.append(nums1[i])
            i+=1
        while(j!=len(nums2)):
            newNums.append(nums2[j])
            j+=1
        print(newNums)
        
        if(len(newNums)%2==0):
            mid = int(len(newNums)//2)
            return (newNums[mid-1]+newNums[mid])/2
        else:
            return newNums[len(newNums)//2]
