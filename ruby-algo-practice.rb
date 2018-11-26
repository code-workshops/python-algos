# Given an array of values, return them in reverse the order.
def reverse(list)
  result = []
  while list.length > 0
    result << list.pop()
  end
  result
end


def reverse_string(str)
	result = ''
	last_index = str.length - 1
	while result.length < str.length
		result += str[last_index]
		last_index -=1
	end
	result
end

# Given an array of integers, join them and add 1 to the number. 
# Example: join_ints([1,3,9,4]) => 1395

def join_ints(nums)
	nums.join() + 1
end
