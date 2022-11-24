#time complexity is O(n*n) - nested loop i of n duration each
def func(n):
		for i in range(n):
				for j in range(n): 
						if j < I:
								break
#time complexity is O(n*v) - for loop is v duration, inner function is n duration
def func(L):
            for v in L:
                # helper func time complexity is O(n)
                helper_func(v)
#time complexity is O(log n) - for each j cut in half run next loop for 1/2 times
def func(n):
		j = n
		while j > 0:
				j = j // 2
		while j<n:
				j = j + 3
				n = n - 5
		return j
#time complexity is O(n*n) - while loop duration is n, sum (range) is O(n) as well
def func(n):
		total = 0
		while n > 5:
				n = n // 2
				# Remember the time complexity of the sum and range methods
				total += sum(range(n))
		return total
#time complexity is O(n) - for loop duration is O(n)
def func(n):
	for i in range(2,n):
			if n % i == 0:
					return True
			if i > n/i:
					return False

#time complexity is O(n*n) - 1st and 2nd loops duration is O(n)
def func(n):
    for i in range(n):
        for j in range(i):
            if j * j > I:
                break
#time complexity is O(n*n/2) -
def func(n):
		k=0
		for i in range(n//2, n):
				j=1
		    while (j <= n):
		        k += 1
						j *= 2
		return k
#time complexity is O(n) x O(n) - for loop is O(n) and the recursive function runs n-2 times O(n)
def helper_func(x):
		for i in range(x):
				print(i)
		return x

def func(n):
		if n == 2:
				return 0
		else:
				return helper_func(n - 1) + helper_func(n - 2)


# time complexity is O(2n) x O(2n) = o(4n*n)- for 1st loop is O(2n) and 2nd for loop is O(2n)
def helper_func(n):
		for i in range(n**2):
		        print(i)
def func(n):
		for i in range(n**2):
				print(helper_func(100))
		return 0