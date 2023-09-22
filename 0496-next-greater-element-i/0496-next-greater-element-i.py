class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        print(nums2)
        
        stack = list()
        result = []

        for i in range(len(nums2)-1,-1,-1):
          
            # if stack is empty, add -1 in result(means no element on right or greater element)
            if not len(stack):
                result.append(-1)

            # if stack is not empty
            else:

                # if stack top element is greater then the current element, add in result
                if stack[-1] > nums2[i]:
                    result.append(stack[-1])

                # if the stack top element is less than current element,
                # loop through stack pop until stack top is greater than current element, and stack
                else:
                    while len(stack) != 0 and stack[-1] <= nums2[i]:
                        stack.pop()

                    # there may be two cases after loop, stack empty or stack top greater than current element

                    # stack empty, add -1 in result(means no element on right)
                    if not len(stack):
                        result.append(-1)
                    
                    else:
                        result.append(stack[-1])

                    # at last append the current element in stack
            
            stack.append(nums2[i])
                
        result.reverse()
        print(result)

        # get nums1 index in nums2
        final_result = []
        for i in nums1:
            final_result.append(result[nums2.index(i)])
        return final_result