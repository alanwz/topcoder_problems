def countSubstrings(string):
	substrings = []
    length = len(str)
    left_sum = 0
    right_sum = 0
    total = 0
    for i in range(length):
        for j in range(i, length):
        	substrings.append(string[i:j+1])
    for s in substrings:
        for i in range(1, len(s)-1):
      		left = string[0:i]
        	right = string[i:len(s)]
        	for c in range(len(left)):
        		if (left[c] == '1'):
        			left_sum += (i-c)
        	for d in range(len(right)):
        		if (right[d] == '1'):
        			right_sum += (c-i)
    if (left_sum == right_sum):
        total += 1
	return total