class Solution:
    def trap(self, height: List[int]) -> int:
        answer = 0
        left_max, right_max = 0, 0
        left, right = 0, len(height) - 1

        while left < right:
            left_value, right_value = height[left], height[right]

            if left_value < right_value:
                if left_value >= left_max:
                    left_max = left_value
                else:
                    answer += left_max - left_value

                left += 1
            else:
                if right_value >= right_max:
                    right_max = right_value
                else:
                    answer += right_max - right_value

                right -= 1

        return answer
