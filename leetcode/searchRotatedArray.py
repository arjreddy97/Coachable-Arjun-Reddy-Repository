class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return shiftedBinarySearch(nums,target)
        
        
        
def shiftedBinarySearch(array, target):
	
	left = 0
	right = len(array) - 1
	
	while left <= right:
		leftBound = array[left]
		rightBound = array[right]
		mid = (left + right) // 2
		potential = array[mid]
		
		if potential == target:
			return mid
		
		elif leftBound <= potential:
			if leftBound <= target and target < potential:
				right = mid - 1
			else:
				left = mid + 1
		
		else:
			if rightBound >= target and target > potential:
				left = mid + 1
			else:
				right = mid - 1
		
			pass
		
		
	return -1
