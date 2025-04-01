def findMedianSortedArrays(nums1, nums2):
    # Ensure nums1 is the shorter array to optimize the solution
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1
    
    m, n = len(nums1), len(nums2)
    left, right = 0, m
    
    while left <= right:
        # Binary search on the shorter array
        partition1 = (left + right) // 2
        partition2 = (m + n + 1) // 2 - partition1
        
        # Get the four boundary numbers
        maxLeft1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
        minRight1 = float('inf') if partition1 == m else nums1[partition1]
        maxLeft2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
        minRight2 = float('inf') if partition2 == n else nums2[partition2]
        
        # Check if we found the correct partition
        if maxLeft1 <= minRight2 and maxLeft2 <= minRight1:
            # If total length is odd
            if (m + n) % 2 == 1:
                return max(maxLeft1, maxLeft2)
            # If total length is even
            return (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2
        # If we're too far on the right side
        elif maxLeft1 > minRight2:
            right = partition1 - 1
        # If we're too far on the left side
        else:
            left = partition1 + 1
    
    return 0.0  # This case should never be reached 
