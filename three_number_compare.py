# amnolan
# nums is an array like [1,9,3,7,4,8]
def find_sum_of_three(nums, target):

   # becomes  [1,3,4,7,8,9]
   nums.sort()


   #[1,3,4,7,8,9]
   # ^
   # c
   # start your compare index at 0
   compare = 0

   # since there are is an extra compare items you subtract 2 instead of one
   while compare < len(nums) - 2:
      # first iteration looks like this
      #[1,3,4,7,8,9]
      # ^ ^       ^
      # c l       r
      left = compare + 1
      right = len(nums) - 1
     
      # while the pointers have not crossed over
      while left < right:
         # sum of all three items
         sum_of_three = nums[compare] + nums[left] + nums[right]

         # if the items are equal we have found a match for instance if we were looking for 14 the numbers
         # 3,4,7 = 14 you would return true
         if sum_of_three == target:
            return True
         # otherwise we need to check if the sum is smaller, if it is (since it's sorted), move the left pointer to the right
         elif sum_of_three < target:
            left = left + 1
         # otherwise we need to check if the sum is bigger, if it is (since it's sorted), move the right pointer to the left
         else:
            right = right - 1
           
      # advance the "compare" pointer
      # at the end of the first iteration it looks like this (if I did this by hand correctly)
      # then the c pointer will move to the right by one and l will then start at position 2
      # the r pointer will again start at the end
      #[1,3,4,7,8,9]
      # ^     ^ ^
      # c     l r
     
      compare = compare + 1
   # if you made it here there is no match
   return False
