class Solution:
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        max_water = 0

        while left < right:
            h = min(height[left], height[right])
            w = right - left
            max_water = max(max_water, h * w)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_water

# Example usage
sol = Solution()
print sol.maxArea([1,8,6,2,5,4,8,3,7])  # Output: 49
